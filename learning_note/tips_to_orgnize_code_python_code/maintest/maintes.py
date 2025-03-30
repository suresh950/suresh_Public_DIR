# This is a script to demonstrate how to import a module from a sibling directory
# This is a Python script that demonstrates how to import functions from a module located in a parent directory.
# This is a script to demonstrate how to import a module from a sibling directory
# In maintes.py
# Method 1: Import the entire module
import sys
import os
# Get the path to the parent directory of maintest
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

import test_package.bike

print("Printing from maintest directory from maintest.py file")
# Now you can call functions like this:
test_package.bike.Bike()
