'''

Name: Ping_Test.py 

Count the number of geohash in the Master_Dataset(63 files) 
(Doesn't do anything with the BOB_Dataset)
Result = about 1 million rows are generated from this

'''

# Libraries 
import pandas as pd 
import numpy as np
import os 
import glob 
from py_geohash_any import geohash as gh # To get geohash neighbor 
import time
from collections import defaultdict

### Path
path = 'C:/Users/User/Desktop/Geohash/'
path_save = 'C:/Users/User/Desktop/'
os.chdir(path)

remember = 'memory_test.csv'

## Read file in the directory
dir_list = os.listdir(path)
name_day = []
for file in dir_list:
    if file[-4:] == '.csv':
        name_day.append(file)

## Dictionary
memroy_dictionary = defaultdict(list) 

i = 0
for file_name in name_day: # read 63 file here
    i += 1
    start_time = time.perf_counter()
    table = pd.read_csv(file_name)['geo_hash']
    for row in table: # read each row in
        read_geohash = row
        if memroy_dictionary.get(read_geohash, False):
            memroy_dictionary[read_geohash][0] += 1
        else:
             memroy_dictionary[read_geohash].append(1)
    end_time = time.perf_counter()
    print("execution time: file number " + str(i))
    print(f"Execution Time: {end_time - start_time: 0.6f}")

new_memory = pd.DataFrame(memroy_dictionary).transpose()
print(new_memory)
new_memory.to_csv(path_save + remember)
print('finished executing')
