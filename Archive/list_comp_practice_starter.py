#!/usr/bin/env python
# must use ./executable.py
import pandas as pd

import csv
import sys
import datetime
# In this exercise, we are going ot explore a "Beach Water Quality" dataset
# -- a set of hourly measurements of sevearl beach water metrics from the
# Chicago Park District's automated sensors at Lake Michigan beaches.  This
# data was obtained form teh Chicago Open Data Portal.

# 0. Edit this file so that it can be run without error from the commandline
#    using only the executable name (i.e. >  list_comp_practice_starter.py
#    instead of python list_comp_practice_starter.py).  You may need to make
#    some changes to your environment too.


# 1.  Using the csv module, fill in the following function to read in the
#     Sensors.csv dataset and remove the header.  Your function should return
#     an array of all of the rows in the dataset.  DO NOT return the header row.
#     Each row should be an array of length 10 containing 10 strings.
#     FROM HERE ON, WE'LL CALL A ROW OF DATA IN THIS FORMAT, A 'READING'


def read_input(path):
    f=open(path)
    data = [row for row in csv.reader(f.read().splitlines())]
    del data[0]
    return data



#  2.  Fill in the following function to find the low battery readings.
#      Using a list comprehension, return an
#      array of readings such that each reading has a lower battery life than
#      the threshold.  The function should take an array of readings and a
# #      threshold of type 'float.'
def find_low_battery_readings(readings, threshold):
    data = [reading for reading in readings if float(reading[7]) < threshold]
    return data



#  3.  Fill in the following function to make an array of dictionaries.  Each
#      dictionary should have two keys:  battery_life and id, corresponding to
#      the fields 'Battery Life' and "Measurement ID" respectively.  The
#      function should take an array of readings.
def battery_dict(readings):
    my_dict = {}
    for i in readings:
        my_dict[i[9]] = i[7]
    return my_dict


#  4.  Fill in the following function to create an array of readings for a
#      given month.  Your function should take an array of readings and a month
#      number (e.g. 5 for May).  It should return an array of only the readings
#      for that month.  Your function must use the datetime module.
def month_readings(readings, month_num):
    # date = readings[876][1]
    # date = datetime.datetime.strptime(date,'%m/%d/%y %H:%S')
    # month = date.month
    # print month
    # data = [row [1] for row in readings]
    # data = [datetime.datetime.strptime(row[1],'%m/%d/%y %H:%S').month for row in readings]
    data = [row for row in readings if datetime.datetime.strptime(row[1],'%m/%d/%y %H:%S').month == month_num]
    return data

  #
  # datetime.strptime('12-07-1941', '%m-%d-%Y')

    # 12/8/14 10:00

#  5.  Before submitting this file, make sure it contains only the functions
#      and import statements required.  IMPORTANT:  remove or comment-out
#      any print statements or calls to the functions you made.  This is
#      necessary for grading.

threshold = 9.6
read_input(sys.argv[1])[0]
find_low_battery_readings(read_input(sys.argv[1]),threshold)
battery_dict(read_input(sys.argv[1]))
month_readings(read_input(sys.argv[1]), 10)
