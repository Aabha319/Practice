#It lets us access system-specific parameters and functions.
import sys
sys.modules
#This function provides the name of the
#existing python modules which have been imported.
sys.argv
#This function returns a list
#of command line arguments passed to a Python script. 
sys.maxsize
#This function returns the largest integer of a variable.
sys.path
#This function shows the PYTHONPATH set in the current system.
sys.executable
#The value of this function is the absolute path to a Python interpreter.
#It is useful for knowingwhere python is installed on someone else machine.
sys.exit
#This function is used to exit from either the Python console or command prompt,
#and also used to exit from the program in case of an exception.
sys.platform
#This value of this function is used to identify the platform
on which we are working.


import os
#This module offers a portable way of using operating system dependent functionality.
#The Python OS module lets us work with the files and directories.

os.mkdir("d:\\abha")
#used to create new directory

print(os.getcwd())
#It returns the current working directory(CWD) of the file.

os.rmdir("d:\\abha")
#removes specified dictionary







