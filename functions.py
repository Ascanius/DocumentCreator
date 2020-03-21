#!/usr/bin/env python3
#This are the main functions of the programm. To use this functions you have to import this file into all of your main files
#Every function must have a comment!

#Imports used libraries

import sqlite3


#Creates the config file or rewrite the config file header
def CreateConfigFile ():
    config = open("config.txt","w")
    config.write("This is the config file for the DocumentCreator-Programm\n")
    config.write("DO NOT CHANGE THIS FILE! ONLY THE  PROGRAMM SHOULD CHANGE THIS FILE!\n")
    config.close()


#Reads from the config
def ReadConfigFile():
    config = open("config.txt","r")
    config.readline(3)
    #add more used lines
    config.close()

#Add Settings to config file
def AddConfigToFile(lang,User,PrintDirekt,Watermark,Database):
    lang1  = lang
    User1 = User
    PrintDirekt1 = PrintDirekt
    Watermark1 = Watermark
    Database1 = Database
    config = open("config.txt","a")
    config.write(lang1)
    config.write(User1)
    config.write(PrintDirekt1)
    config.write(Watermark1)
    config.write(Database1)
    config.close()

def ConnectToDatabase ()
    db = ""
    db = config.readline(7)
    connection = sqlite3.connect(db)
