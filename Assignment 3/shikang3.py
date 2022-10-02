#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 12:44:02 2022

@author: lucian
"""

#Variable Operation Exercrises
#1
sub_code = 'sub'
subnr_int = 2
subnr_str = '2'
#2
print(sub_code + ' ' + subnr_str)
print(sub_code + ' ' + subnr_str * 3)
print((sub_code + subnr_str) * 3)
print(sub_code * 3 + subnr_str * 2)


#List Operations exercises
#1
numlist = [1,2,3]
print(numlist * 2)
#2
import numpy as np
numarr = np.array([1,2,3])
print(numarr * 2)
#3
strlist = ['do', 're', 'mi', 'fa']

a=[]
for m in range(len(strlist)):
   a.append(strlist[m] * 2)
print(a)



print(strlist * 2)

c = []
for m in range(len(strlist)):
    b.append(strlist[m])
    b.append(strlist[m])
print(b)

d = []
for m in range(len(strlist)):
    d.append([strlist[m], strlist[m]])
print(d)

#Zipping exercises
face = ['face1.png', 'face2.png', 'face3.png', 'face4.png', 'face5.png'] * 10
house = ['house1.png', 'house2.png', 'house3.png', 'house4.png', 'house5.png'] * 10
cue = ['cue1', 'cue2'] * 50
import numpy as np
np.random.shuffle(face)
np.random.shuffle(house)
fh1 = list(zip(face, house, cue))
fh2 = list(zip(house, face, cue))
np.random.shuffle(fh1)
np.random.shuffle(fh2)
final = fh1 + fh2
np.random.shuffle(final)
print(final)

#Indexing exercises
color = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
print(color[-2])
print(color[-2][2:4])
color.remove('purple')
color.insert(6,'indigo')
color.insert(7,'violet')
print(color)

#Slicing exercise
list100 = list(range(0,100))
print(list100[:10])
print(list100[::-2])
print(list100[:-5:-1])
print(list100[39:44] == [39,40,41,42,43])











