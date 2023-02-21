import pandas as pd 
import numpy as np 
import os 
import glob 
import time
from collections import defaultdict

# Path 
print('Start setting up location name')
path = 'C:/Users/User/Desktop/Geohash/' 
path_save = 'C:/Users/User/Desktop/'
os.chdir(path)
remember = 'Bob_New.csv'

# Read file in the directory 
print('Start reading all 63 files here:')
dir_list = os.listdir(path)
name_day = []
for file in dir_list:
    if file[-4:] == '.csv': 
        name_day.append(file)

# Dictionary 
print('Start initializing sample_dataset here') # Sample dataset contains 40 rows and 2 columns 
memmory_pd = pd.read_csv('C:/Users/User/Desktop/' + 'Bob_with_geohash_new.csv')['geohash']
memroy_dictionary = {}
for row in memmory_pd: 
    if not memroy_dictionary.get(row): 
        memroy_dictionary[row] = [0]

## start the process of summing
print('Starting the process')
i = 0 
for file_name in name_day: 
    print('processing file: ' + file_name)
    i += 1 
    start_time = time.perf_counter() 
    table = pd.read_csv(file_name)['geo_hash']  
    for row_63 in table: 
        if memroy_dictionary.get(row_63):
            memroy_dictionary[row_63][0] += 1 
    end_time = time.perf_counter()
    print("execution time: file number " + str(i))
    print(f"Execution Time: {end_time - start_time: 0.6f}")

## saving result
new_memory = pd.DataFrame(memroy_dictionary).transpose() 
new_memory.to_csv(path_save + remember)
print('finished executing')