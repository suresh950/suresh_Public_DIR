# This is a Python script that demonstrates how to import functions from a module located in a parent directory.
# In maintes.py
# Method 2: Import specific functions (requires adding to path)
import sys
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from test_package.bike import your_function_name, another_function

print("Printing from maintest directory from maintest.py file")
# Now you can call them directly:

your_function_name()
another_function()