#!/usr/bin/env python3
#This file contains the used functions to create the final document with TeX-Coding

#import used libraries
import functions.py
import tkinter
import pylatex
import pylatex.utils
import pdflatex

#Create Report
def CreateReport():
    geometry_options = {
    "head" : "40pt",
    "margin": "0.39in",
    "bottom" : "0.59in",
    "includeheadfoot" : true
    }
    doc = Document(geometry_options=geometry_options)
    first_page = PageStyle("firstpage")

    #show logo
