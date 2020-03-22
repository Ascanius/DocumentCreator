#!/usr/bin/env python3
#Contains the Starupfile
#Loads all used files and starts the UI

#import used libraries
import functions.py as fkt
import tkinter
import os

#Startup sequence
#Check for config file

if not os.path.exists("config.txt") then:
    fkt.CreateConfigFile()
    fkt.AddToConfigFile(0,"NULL","NO","NO","database.db")

#Load Language File
prestartup = tk()
prestartup.title("")
file = open ("config.txt","r")
lang = file.readline(4)
langarray  = ""
IF lang = 0 THEN:
    language = open ("DEU.txt","r")
    langarray = language.readline()
ELIF lang = 1 THEN:
    language = open ("ENU.txt","r")
    langarray = language.readline()
ELSE:
    messagebox.showerror("Error","CODE SP 0001")
prestartup.mainloop()



startup = tk()

startup.title(langarray[2])



startup.mainloop()
