import sqlite3
import os
from database_functions import *
import requests
from math import sin, cos, sqrt, atan2, radians
from collections import defaultdict

def check_db(environment):
    if os.path.exists("static/db/{}_phoneBookProject2.db".format(environment)):
        return True
    else:
        return False

def get_cursor(environment):
    cursor, connection = connection_factory(environment)
    return cursor, connection

def check_if_input_business_type_is_in_database(cursor,business_type):

    cursor.execute("SELECT business_category FROM businesses WHERE business_category=?", (business_type,))
    results = cursor.fetchall()
    for index in range(len(results)):

        if business_type in results[index]:
    #                    print("Mariana is the best.")
            return business_type
        else:
            msg="Your search does not appear in our database."
#
def get_coordinates_for_postcode(postcode):


            postcode=postcode.replace(" ","")
            endpoint_postcode="https://api.postcodes.io/postcodes/"
            postcode_response=requests.get(endpoint_postcode+postcode)
            data_postcode=postcode_response.json()
            if data_postcode['status'] ==200:
                lat1=data_postcode['result']['latitude']
                long1=data_postcode["result"]["longitude"]
#                print(long1, lat1)
                return long1, lat1
            else:

                print("The postcode you provided is not valid!")
def get_information_for_businesses_with_input_business_type(cursor,business_type):

    cursor.execute("SELECT business_name, telephone_number, postcode,adress_line_1,adress_line_2,adress_line_3 FROM businesses WHERE business_category=?", (business_type,))
    results = cursor.fetchall()
    print(results)
    mari=[]
#    print(results)
#    print(type(results))
    for row in results:
#        print(row)
        row=list(row)
#        print(type(row))
#        print(row)
        postcode=row[2]
#        print(postcode)
        coordinates=get_coordinates_for_postcode(postcode)
        coordinates=list(coordinates)
#        print(coordinates)
        row.extend(coordinates)
#        print(row)
        mari.append(row)
    print(mari)
    return mari

#get_information_for_businesses_with_input_business_type(get_cursor("mariana"),"Toys")
def distance(businesses_info_list,long1,lat1):


    for index in range(len(businesses_info_list)):
        long2=businesses_info_list[index][6]
        lat2=businesses_info_list[index][7]
        R = 6373.0 # approximate radius of earth in km

        dlon, dlat = radians(long2) - radians(long1), radians(lat2) - radians(lat1)
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        a=abs(a)
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        hdist = R * c
        hdist=int(hdist)
    #        print(hdist)
    #        print(businesses_info_list[index])

        businesses_info_list[index].append(hdist)
#        print(businesses_info_list[index])
#    print (businesses_info_list)

#    print("I'm here")
    return businesses_info_list
def convert_businesses_info_list_into_dictionary(businesses_info_list ):

    d = defaultdict(list)
    for index in range(len(businesses_info_list)):
        list1= businesses_info_list[index]
#    print(list1)
        d[list1[0]] += list1[1:]
    #print(dict(d))
    d=dict(d)
    return d
def sort_result_by_distance(result):

    sorted_result = sorted(result.items(),key=lambda kv:kv[1][-1])
    print(sorted_result)
    return sorted_result
