#!/usr/bin/env python3
#This are the main functions of the programm. To use this functions you have to import this file into all of your main files
#Every function must have a comment!

#Imports used libraries

import sqlite3
import os


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

#Connect to database or create database
def ConnectToDatabase ()
    config.open("config.txt","r")
    db = config.readline(7)
    IF db = "" THEN
        global connection = sqlite3.connect(db)
        CreateDbTable()
    ELSE
        EXIT

#Create Tables in the database
def CreateDbTable()
    cursor = connection.cursor()
    sql_command = """
        CREATE TABLE item (
        no Code PRIMARY KEY,
        name VARCHAR (100),
        price DECIMAL,
        vat DECIMAL);"""
    cursor.execute(sql_command)
    sql_command = """
        CREATE TABLE customer (
        fname VARCHAR (50),
        lname VARCHAR (50),
        gender VARCHAR (2),
        address VARCHAR (50),
        city VARCHAR (50),
        plz VARCHAR (25),
        phone VARCHAR (20),
        mail VARCHAR (50));"""
    cursor.execute(sql_command)
    connection.commit()
    connection.close()

#Get the current Customer
def GetCustomer (name)
    cursor = connection.cursor()
    cursor.execute("Select * FROM customer where (lname = name)")
    cust = cursor.fetchone()
    return cust

#Get the Items
def GetItem (number)
    cursor = connection.cursor()
    cursor.execute("Selet * FROM item where (no = number)")
    item = cursor.fetchone()
    return item

#write tempdoc file
def CreateTempDocument()
    tempdoc = open ("doc.txt","w")
    tempdoc.close()

#write into tempdoc file
def WriteTempDocument(Key)
    tempdoc = open("doc.txt","a")
    tempdoc.write(Key)
    tempdoc.close()

#Remove tempdoc file
def DeleteTempDocument()
    os.remove("doc.txt")
