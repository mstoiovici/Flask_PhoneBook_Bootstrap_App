# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 14:31:57 2019

@author: maria
"""

from flask import Flask,render_template
from engine import *
import os

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search_results")
def search_results():
    return render_template("search_results.html")


if __name__=="__main__":
    app.run()
