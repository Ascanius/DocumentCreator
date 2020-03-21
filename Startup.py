#!/usr/bin/env python3
#Contains the Starupfile
#Loads all used files and starts the UI

#import used libraries
import functions.py
import tkinter

#Startup sequence
#Load Language File
lang = 0
file = open ("config.txt","r")
lang = file.readline(3)

IF lang = 0 THEN
    language = open ("DEU.txt","r")
ELIF lang = 1 THEN
    language = open ("ENU.txt","r")
ELSE
    messagebox.showerror("Error","CODE SP 0001")


startup = tk()

startup.title(language.readline(1))

startup.mainloop()
