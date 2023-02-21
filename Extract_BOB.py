'''
Name: Extract_BOB.py 

Extract pings from Master_Dataset (contains 63 files) - dictionary = BOB_Dataset 
1. Create dictionary using BOB_Dataset 
2. Find the same geohash (based on BOB_Dataset) in Master_Dataset

11/20/2022
Note: 
There are some duplicated geohash locations in the BOB_Dataset - I assume that the precision scores -
too low, which is why some shops share the same geohash location 
Result = only 262 stores are displayed with the precision = 9

'''

# Libraries 
print('Import Important Library')
import pandas as pd 
import numpy as npi
import os 
import glob 
import time
from collections import defaultdict

### Path
print('Start setting up location name')
path = 'C:/Users/User/Desktop/Geohash/' # [definition] [path --> String] name of the location of the folder that conta 63 files to read 
path_save = 'C:/Users/User/Desktop/' # [definition] [path_save --> String] name of the location of the folder that conta Bob and where to save 
os.chdir(path) # [action] [none] set the current working space to path 
remember = 'memory.csv' # [definition] [remember --> string] name of output file 

## Read file in the directory
print('Start reading all 63 files') 
dir_list = os.listdir(path) # [definition] [dir_list --> list(string)] contain names of the 63 files 
name_day = [] # [definition] [name_day --> list(empty)] 
for file in dir_list: # [loop] [file = element in dir_list --> string] each individual name of the 63 file
    if file[-4:] == '.csv': # [checking] if the last 4 letter in file == .csv then go in
        name_day.append(file) # [action] [none] put file inside name_day

## Dictionary
print('Start initializing Bob geohash dictionary')
memmory_pd = pd.read_csv( 'C:/Users/User/Desktop/'+'BoB_with_Geohash.csv')['geohash'] # [definition] [memory_pd --> dataframe(one col - geohash)] 400 x 1 (each row represents one geohash code)
memroy_dictionary = {} # [definition] [memory_dictionary --> dictionary] From BOB :) 
for row in memmory_pd: # [loop] [row = individual row in dataframe(memory_pd), contains 1 column] 
    if not memroy_dictionary.get(row): # [checking] 1. if geohash is not in dictionary - go in | 2. if geohash is already in dictionary - dont go in 
        memroy_dictionary[row] = [0] # [definition --> key in dictionary] + set value == 0 

## start the process of summing
print('Starting the process')
i = 0 # [definition] [i --> int] value = 0
for file_name in name_day: # [loop] [file_name = individual element in list, which is called name_day --> string] each individual 63 files name 
    print('processing file: ' + file_name)
    i += 1 # [definition] [i --> int] value i + 1 (i = i + 1)
    start_time = time.perf_counter() # [definition] [time object (start time)] get start time 
    table = pd.read_csv(file_name)['geo_hash'] # [definition] [table --> dataframe(one col - geo_hash)] n x 1 (each row represents one geohash code) -- from 63 files* 
    for row_63 in table: # [loop] [row = element in dataframe(table) contains 1 column --> string] ** if contains 2++ columns == list, if 1 == string **
        if memroy_dictionary.get(row_63): # [checking] 1. if geohash is already in list - go in
            memroy_dictionary[row_63][0] += 1 # [definition] [value in memory_dictionary + 1] add value + 1 **[0] = is to debug the code 
            # Note for above line: memory_dictionary contains geohash from BOB thus start with "<= 400 rows" from BOB
    end_time = time.perf_counter()
    print("execution time: file number " + str(i))
    print(f"Execution Time: {end_time - start_time: 0.6f}")


## saving result
print(memroy_dictionary)
new_memory = pd.DataFrame(memroy_dictionary).transpose() # transpose = transform the dictionary from 261 x 2 to 2 x 261 [กลับด้านกัน]
print(new_memory)
new_memory.to_csv(path_save + remember)
print('finished executing')
