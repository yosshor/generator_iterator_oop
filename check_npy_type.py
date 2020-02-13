# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 22:53:59 2020

@author: Yossi
"""

import numpy as np
import pandas as pd
import time

N = 10000000
with open('data.txt', 'w') as data:
    for _ in range(N):
        data.write(str(10 * np.random.random()) + ',')


#checking times for reading a txt file
start = time.time()
with open('data.txt', 'r') as data:
    string_data = data.read()
list_data = string_data.split(',')
list_data.pop()
data_array = np.array(list_data, dtype = float).reshape(10000, 1000)
end = time.time()
print("### 10 million points of data ###")
print("\nData summary : \n", data_array)
print("\nData shape : \n", data_array.shape)
print("\nTime to read : {}.seconds ".format(round(end - start, 5)))


#checking times for reading a .npy file
np.save('data.npy', data_array)
start = time.time()
data_array = np.load('data.npy')
end = time.time()
print("### 10 millions points of data ###")
print("\n Data summary : \n", data_array)
print("\nData shape : ", data_array.shape)
print("\n Time to read : {}.seconds".format(round(end - start, 5)))


#chacking times for reading a .csv file
data = pd.DataFrame(data_array)
data.to_csv('data.csv', index = None)
start = time.time()
data = pd.read_csv('data.csv')
end = time.time()
print("### 10 millions points of data ###")
#print("\nData summary : \n", data)
print("\nData summary : \n", data.info())
print("\nData shape :", data.shape)
print("\n Time in seconds : {}.seconds".format(round(end - start, 5)))


data_array = np.load('data.npy')
data = pd.DataFrame(data_array)



for dirpath, dirnames, filenames in os.walk('..'):
  print('path: ', dirpath)
  print('directories: ', dirnames)
  print('files: ', filenames)
  print()




