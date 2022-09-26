#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 11:30:39 2022

@author: lucian
"""


for m in list('shikang'):
    print(m)
    

#Operation exercises
print(5/2)
print(5.0/2.0)


#Variable exercise

letter1 = 'S'
letter2 = 'h'
letter3 = 'i'
letter4 = 'k'
letter5 = 'a'
letter6 = 'n'
letter7 = 'g'
letterX = 'S'
letterX = letter1
print(letterX)
print(letter1)
letter1 = 'z'
print(letterX)
print(letter1)

#Boolean exercises
print(1 ==1.0)
print('1' == '1.0')
print(5 == (3+2))


#List exercise
oddlist = [1,3,5,7,9]
print(oddlist)
len(oddlist)
type(oddlist)

intlist = list(range(0,100))
print(intlist)



#Dictionary exercise
about_me = {'name': 'shikang', 'age': 22.0, 'year of study': 4, 'favorite food': 'stinky tofu, lobsters, spicy chicken'}
print(about_me)
print(len(about_me))

import numpy as np
mixnums = np.array([1,2,3,4.0,5.0,6.0])
print(mixnums)

mixtypes = np.array([1,2,3.0,4.0,'a','b'])
print(mixtypes)

oddarray = np.arange(1, 100, 2)
print(oddarray)

logarray = np.logspace(1,5,16)
print(logarray)