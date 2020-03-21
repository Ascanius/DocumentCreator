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
IF lang = 0 THEN:
    language = open ("DEU.txt","r")
ELIF lang = 1 THEN:
    language = open ("ENU.txt","r")
ELSE:
    messagebox.showerror("Error","CODE SP 0001")
prestartup.mainloop()



startup = tk()

startup.title(language.readline(2))



startup.mainloop()
