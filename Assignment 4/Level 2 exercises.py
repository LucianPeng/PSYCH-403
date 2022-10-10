#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 10:17:27 2022

@author: lucian
"""

#Conditional exercises
response = 'NaN'
if response == '1' or response == '2':
    print('OK')
elif response == 'NaN':
    print('subject did not respond')
else:
    print('subject pressed the wrong key')

response = '2'
if response == '1' or response == '2':
    print('OK')
    if response == '1':
        print('Correct!')
    if response == '2':
        print('Incorrect!')
elif response == 'NaN':
    print('subject did not respond')
else:
    print('subject pressed the wrong key')


#For loop exercises
for letter in list('shikang'):
    print(letter)

count = -1
for letter in list('shikang'):
    count = count + 1
    print(letter)
    print('this letter has an index of %i' %count)

count = -1
a = ['Amy', 'Rory', 'River']
for name in a:
    print(name)
    count = count + 1
    for letter in name:
        print(letter)

count = -1
a = ['Amy', 'Rory', 'River']
for name in a:
    print(name)
    count = count + 1
    index = -1
    for letter in a[count]:
        index = index + 1
        print(letter)
        print('This letter has an index of %i' %index)

#while loop exercises
i = 0
while i < 20:
    if i < 10:
        print('image1.png')
    else:
        print('image2.png')
    i = i + 1
        

import random
response = False
i = 0
while not response:
    i = i + 1
    print('Showing an image for %i iterations' %i)
    random_num=random.randint(0,10)
    if random_num == 1 or random_num == 2:
        response  =  True
        print('image.png')


import random
response = False
i = 0
failsafe = 0
while not response:
    failsafe += 1
    if failsafe == 5:
        break
    i = i + 1
    print('Showing an image for %i iterations' %i)
    random_num=random.randint(0,10)
    if random_num == 1 or random_num == 2:
        response  =  True
        print('image.png')
    








