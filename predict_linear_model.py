#!/usr/bin/env python

import pickle
import array as arr
import numpy as np

filename='linear_model.pkl'

year = input("Enter year: ")
quarter = input("Enter quarter: ")
sales = input("Enter sales: ")

input_arr = [[year,quarter,sales]]

#load the model from disk
model = pickle.load(open(filename, 'rb'))
res = model.predict(np.array(input_arr,dtype='float64'))
print(res)