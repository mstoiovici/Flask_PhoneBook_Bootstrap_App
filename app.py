# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 14:31:57 2019

@author: maria
"""

from flask import Flask,render_template, request
from engine1 import *
import os

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search_results", methods=["POST"])
def search_results():
    if check_db("mariana"):
        cursor,connection=get_cursor("mariana")
        form_data = request.form
        business_type = form_data["business_type"]
        if business_type:
            checked_business_type=check_if_input_business_type_is_in_database(cursor,business_type.title())

        postcode=form_data["postcode"]
        long1,lat1=get_coordinates_for_postcode(postcode)
        businesses_info_list=get_information_for_businesses_with_input_business_type(cursor,checked_business_type)
        businesses_info_list_with_distance=distance(businesses_info_list,long1,lat1)
        result=convert_businesses_info_list_into_dictionary(businesses_info_list_with_distance)
        sorted_result=sort_result_by_distance(result)

        
    return render_template("search_results.html", **locals())


if __name__=="__main__":
    app.run(debug=True)
