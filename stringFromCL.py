# Program to get a single string from the command line

import sys


def getStringFromCL():
    '''takes in no arguments, returns string that user inputted from command line'''
    userString = ''

    while True:
        userString = input("Please enter payee name: ")
        if userString == '':
            print("Enter one string as input")
            continue
        else:
            break
    return userString
