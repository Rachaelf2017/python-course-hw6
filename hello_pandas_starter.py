#!/usr/bin/env python
# must use ./executable.py



import glob
import pandas as pd
import math

# Housing prices vary over time in different cities.  In this exercise we are
# going to see sales prices from four different US cities including Atlanta,
# Chicago, Dallas and Oakland.  This data is published by economist Robert
# Shiller.

# For this homework download the four datasets in the shiller_data folder
# on Canvas.  You will want to keep these four datasets in their own directory
# with nothing else in it.

# There are four columns in each of the CSV files.  They are the 'first sale
# price' (purchase price), 'second sale price' (sale price), 'first sale date'
# (purchase date) and 'second sale date' (sale date).  The date in the last
# two columns is indicated in quarters, which will be further explained in the
# following instructions.  There are no headers in these documents.  More
# information on this data can be found at:
# http://www.econ.yale.edu/~shiller/data.htm

# 0. Edit this file so that it can be run without error from the commandline
#    using only the executable name (i.e. >  hello_pandas_starter.py
#    instead of python hello_pandas_starter.py).  You may need to make
#    some changes to your environment too.



# 1. Complete the function below to read multiple files into a single pandas
#    data frame.  This function takes three arguments:
#    - a string 'dir_path'
#    - an array of strings that will be used as column names
#    - a string name of a new column
#    Your function should return a single DataFrame with the column names
#    as specified in the column_names argument.  The resulting frame should
#    be indexed with unique integers, starting at 0.  For now, you can ignore
#    the third argument.
#    A sample data row is:
#    0     2550     3300       38   54
def read_all_files(dir_path, column_names, source_column) :
	data_files = glob.glob(dir_path)
	frames = []
	for f in data_files:
		new_frame=pd.read_csv(f, header = None, names = [column for column in column_names])
		add_source_column(new_frame,'City', f)
		append_year(new_frame,'purchase_date')
		append_year(new_frame,'sale_date')
		#FILL THIS IN
		#CREATE A NEW DATAFRAME CALLED new_frame FROM FILE f and columns
		frames.append(new_frame)

	return pd.concat(frames, ignore_index=True)








# 2.  In a comment in this file, describe in your own words what this function
#     does, assuming file_path is a string file path.
def add_source_column(frame, col_name, file_path):
	frame[col_name] = file_path.split('/')[-1].split('.')[0]
	return frame
    # IF YOU ARE ON WINDOWS, REPLACE THE LINE ABOVE WITH:
    # frame[col_name] = file_path.split('\\')[-1].split('.')[0]
	# print frame

# add_source_column(read_all_files('shiller_data/*.csv', column_names ,'source'), 'City','shiller_data/*.csv')




# ['shiller_data/atlanta.csv', 'shiller_data/chicago.csv', 'shiller_data/dallas.csv', 'shiller_data/oakland.csv']



# 3.  Now call the function in (2) from inside the for loop of the function in
#     (1) such that a sample row of your DataFrame is:
#    0     2550     3300       38   54  atlanta

# 4.  Fill in the following function to add a year column.
#     This dataset contains data columns that are the
#     number of the quarter since 1970.  We want to know which year the quarter
#     number indicates.  For instance, '54' means the 54th quarter starting
#     from Q1:1970, i.e. year 1983.  Fill in the function below where the
#     arguments are the frame and the string name of an existing column.
#     Your function should return the frame with a new column called whose name
#     depends on 'col.'  The new column should be called XXXX_year where XXXX is
#     the value of 'col'  If col is quarter_num then the new column should be
#     quarter_num_year
def append_year(frame, col):
	frame[col+ '_year'] = [int(math.floor(quarter/4))+1970 for quarter in frame[col]]
	return frame

# 5.  Fill in the following function to find fast sales.  The function should
#     take a DataFrame 'frame' and an integer 'period' and return all rows
#     for homes that were sold within period quarters of their purchase.
#     Your function can add columns to frame if you wish.
def fast_sales(frame, period):
	# frame['turn_around'] = frame.sale_date - frame.purchase_date
	# fast = frame['turn_around'] < period
	# fast = (frame.sale_date - frame.purchase_date) < period
	return frame[(frame.sale_date - frame.purchase_date) < period]

# 6.  Fill in the following function to find the profit on fast sales.
#     The funtion should return the mean profit (a single number) for homes that
#     that were sole within period quaters of their purchase.  It should
#     take a DataFrame 'frame' and an integer 'period'.
#     Your function can add columns to frame if you wish.  You can
#     call the function from (5).
def profit_on_fast_sales(frame, period):
	frame['profit'] = (frame.sale_price - frame.purchase_price)
	return frame['profit'].mean()


# 7.  Fill in the following function to count the sales by group.
#     The funtion should
#     take a DataFrame 'frame' and a string 'col_name' which is the name
#     of the column to group by.
#     Your function should return the count of sales per group.  For our
#     datasets, using 'city' as the col_name,
#     the function should return 4 rows like:
#  chicago  15530
def sales_by_column(frame, col_name) :
	# return pd.pivot_table(frame, index= [col_name], aggfunc = 'count')
	return pd.crosstab(index=frame[col_name], columns = "Count")



column_names ='purchase_price' ,'sale_price' ,'purchase_date' ,'sale_date'
frame = read_all_files('shiller_data/*.csv', column_names ,'source')
print frame
period = 5
print profit_on_fast_sales(fast_sales(frame,period), period)

sales_by_column(frame, 'City')
