#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 15:31:34 2019

@author: swilson5
"""

# Calculator Class

Now you are going to work with a partner to create a class. 
Your class will take in a list of numbers and then calculate various descriptive statistics for that list. You will also make your object flexible so that it can accept additional lists of numbers and either add or delete them from the original data. 


**Your class should have the following attributes:**

.data - where you will hold your data
.length - that tells you the length of your data list
.mean
.median
.variance
.stand_dev

**Your class should have the following methods:**

.add_data() - which can take in  a list of values and extend the .data attribute
.remove_data() accept a list of numbers and remove any of the numbers in that list from your object data


### Execution:
You will build your class in the `descriptive.py` file. Once you think you have completed the task, you can test your code. Open up a terminal window and navigate to where this folder. Once there run `pytest test_calculator.py` and it will run a python script to test your calculator class. This script will run 5 tests that your code should pass.  IF it fails a test, it should give you some output to let you know what test it failed. 

