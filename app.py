# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 14:31:57 2019

@author: maria
"""

from flask import Flask,render_template, request
from database_functions import *
from engine1 import *
from engine_people import *
import os

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/businesses")
def businesses():
    return render_template("businesses.html")

@app.route("/people")
def people():
    return render_template("people.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/businesses_results", methods=["POST"])
def businesses_results():
    if check_db("mariana"):
        cursor,connection=get_cursor("mariana")
        form_data = request.form
        business_type = form_data["business_type"]
        if business_type:
            checked_business_type=check_if_input_business_type_is_in_database(cursor,business_type.title())


        postcode=form_data["postcode"]
        long1,lat1=get_coordinates_for_postcode(postcode)
        muna=get_information_for_businesses_with_input_business_type(cursor,checked_business_type)
        businesses_info_list_with_distance=distance(muna,long1,lat1)
        result=convert_businesses_info_list_into_dictionary(businesses_info_list_with_distance)
        sorted_result=sort_result_by_distance(result)


    return render_template("businesses_results.html", **locals())

@app.route("/people_results", methods=["POST"])
def people_results():
    if check_db("mariana"):
        cursor,connection=connection_factory("mariana")
        form_data = request.form
        business_type = form_data["business_type"]
        if business_type:
            checked_business_type=check_if_input_business_type_is_in_database(cursor,business_type.title())


        postcode=form_data["postcode"]
        long1,lat1=get_coordinates_for_postcode(postcode)
        muna=get_information_for_businesses_with_input_business_type(cursor,checked_business_type)
        businesses_info_list_with_distance=distance(muna,long1,lat1)
        result=convert_businesses_info_list_into_dictionary(businesses_info_list_with_distance)
        sorted_result=sort_result_by_distance(result)


    return render_template("people_results.html", **locals())

if __name__=="__main__":
    app.run(debug=True)
