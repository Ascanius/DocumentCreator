#!/usr/bin/env python3
#This are the main functions of the programm. To use this functions you have to import this file into all of your main files
#Every function must have a comment!


#Creates the config file or rewrite the config file header
def CreateConfigFile ():
    config = open("config.txt","w")
    config.write("This is the config file for the DocumentCreator-Programm\n")
    config.write("DO NOT CHANGE THIS FILE! ONLY THE  PROGRAMM SHOULD CHANGE THIS FILE!\n")
    configg.write("\n")
    config.close()


#Reads from the config
def ReadConfigFile():
    config = open("config.txt","r")
    config.readline(4)
    #add more used lines

def AddConfigToFile():
    config = open("config.txt","a")
    #add config lines here
    config.close()
