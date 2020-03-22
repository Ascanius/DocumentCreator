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

    with forst_page.create(Head("L")) as header_right:
        with header_right.create(MiniPage(width=NoEscape(r"0.49\textwidth"),pos="c")) as logo_wrapper:
            logo_file = os.path.join(os.path.dirname(__file__), "logo.png")
            logo_wrapper.append(StandAloineGraphic(image_options="width=120px",Filename=logo_file))

    #Add footer

    with first_page.create(Foot("C")) as footer:

    doc.preamble.append(first_page)


    #Add Custoemr Information
    with doc.create(Tabu("X[l]" "X[r]")) as first_page_table:
        customer = MiniPage(width=NoEscape(r"0.49\textwidth"),pos="h")
        customer.append("")
        customer.append("\n")
