# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 09:57:00 2019

@author: maria
"""

import sqlite3
import os
from database_functions import *
import requests
from math import sin, cos, sqrt, atan2, radians
from collections import defaultdict

def main(environment):
    if check_db(environment):
        filter_no=get_no_of_filters()
        if filter_no==1:
            info=run_one_filter(environment)
        elif filter_no==2:
            info=run_two_filters(environment)
        #print(info)
        return info
    else:
        print("No connection to database")
        return "No connection to database"

def check_db(environment):
    if os.path.exists("{}_phoneBookProject2.db".format(environment)):
        return True
    else:
        return False

def get_no_of_filters():
    no_of_filters=int(input("Please type:\n 1. for one filter\n 2. for two filters\n"))
    return no_of_filters

def run_one_filter(environment):
    city_country=choose_option_city_or_country()
    if city_country==1:
        info=get_info_for_city(environment)
    elif city_country==2:
        info=get_info_for_country(environment)
       
    
    print(info)
    return info

def get_info_for_city(environment):
    cursor,connection=connection_factory(environment)
    alpha=get_user_input()
    cursor.execute("SELECT last_name, first_name,telephone_number, adress_line_1,adress_line_2, postcode FROM people WHERE adress_line_2=?", (alpha,))
    results = cursor.fetchall()
    return results

def get_info_for_country(environment):
    cursor,connection=connection_factory(environment)
    alpha=get_user_input()
    cursor.execute("SELECT last_name, first_name,telephone_number, adress_line_2,adress_line_3 postcode FROM people WHERE adress_line_3=?", (alpha,))
    results = cursor.fetchall()
    return results
        
        
        
def run_two_filters(environment):
    option_one=choose_option_surname_or_name()
    option_two=choose_option_city_or_country()
    info=get_something(environment,option_one,option_two)
       
    
    print(info)
    return info
                
        
        
        

    
def choose_option_surname_or_name():
    option=int(input("Do you want to search for surname or name? \nPlease type:\n 1. for surname\n 2. for name\n"))
    print(option)
    return option
def choose_option_city_or_country():
    option=int(input("Do you want to search for a city or a country? \nPlease type:\n 1. for city\n 2. for country\n"))
    print(option)
    return option



def get_something(environment,option_one,option_two):
    cursor,connection=connection_factory(environment)
    alpha= get_user_input()
    beta=get_user_input()
    if option_one==1 and option_two==1:
        
        info=get_info_for_surname_and_city(environment,cursor,alpha,beta)
    elif option_one==1 and option_two==2:
        info=get_info_for_surname_and_country(environment,cursor,alpha,beta)
    elif option_one==2 and option_two==1:
        info=get_info_for_name_and_city(environment,cursor,alpha,beta)
    elif option_one==2 and option_two==2:
        info=get_info_for_name_and_country(environment,cursor,alpha,beta)
    elif option_two==1:
        info=get_info_for_city(environment,cursor,alpha)
        return info
    return info

def get_user_input():
    user_input=input("Please provide the information here: ")
    print(user_input)
    return user_input
    

    
    
def get_info_for_surname_and_city(environment,cursor,alpha,beta):
    cursor,connection=connection_factory(environment)
    cursor.execute("SELECT last_name, first_name,telephone_number, adress_line_1,adress_line_2, postcode FROM people WHERE last_name=? and adress_line_2=?", (alpha,beta,))
    results = cursor.fetchall()
#    people_info=[]
#    print(results)
#    print(type(results))
#    for row in results:
#        print(row)
#        row=list(row)
#        print(type(row))
#        print(row)
#        postcode=row[2]
#        print(postcode)
#        coordinates=get_coordinates_for_postcode(postcode)
#        coordinates=list(coordinates)
#        print(coordinates)
#        row.extend(coordinates)
#        print(row)
#        businesses_info_list.append(row)
#    print(results)
    return results

def get_info_for_surname_and_country(environment,cursor,alpha,beta):
    cursor,connection=connection_factory(environment)
    cursor.execute("SELECT last_name, first_name,telephone_number, adress_line_1,adress_line_2, postcode FROM people WHERE last_name=? and adress_line_3=?", (alpha,beta,))
    results = cursor.fetchall()

    return results

def get_info_for_name_and_city(environment,cursor,alpha,beta):
    cursor,connection=connection_factory(environment)
    cursor.execute("SELECT last_name, first_name,telephone_number, adress_line_1,adress_line_2, postcode FROM people WHERE first_name=? and adress_line_2=?", (alpha,beta,))
    results = cursor.fetchall()

    return results
def get_info_for_name_and_country(environment,cursor,alpha,beta):
    cursor,connection=connection_factory(environment)
    cursor.execute("SELECT last_name, first_name,telephone_number, adress_line_1,adress_line_2, postcode FROM people WHERE first_name=? and adress_line_3=?", (alpha,beta,))
    results = cursor.fetchall()

    return results


main("mariana")