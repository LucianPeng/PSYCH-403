#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 20:41:05 2022

@author: lucian
"""

#=====================
#IMPORT MODULES
#=====================
import numpy as np
from psychopy import visual, core, gui, visual, event
import json
import os
import random

#=====================
#PATH SETTINGS
#=====================
#-define the main directory where you will keep all of your experiment files
os.chdir('/Users/Lucian/Downloads/PSYCH403_Exp')
#-define the directory where you will save your data
main_dir = os.getcwd()
#-if you will be presenting images, define the image directory
image_dir = os.path.join(main_dir, 'images')
data_dir = os.path.join(main_dir, 'data')

#-check that these directories exist
os.path.isdir(image_dir)
os.path.isdir(data_dir)
if not os.path.isdir(image_dir):
    raise Exception('Could not find the path!')
#=====================
#COLLECT PARTICIPANT INFO
#=====================
#-create a dialogue box that will collect current participant number, age, gender, handedness
#get date and time
#-create a unique filename for the data

#=====================
#STIMULUS AND TRIAL SETTINGS
#=====================
#-number of trials and blocks *
nTrials = 10
nBlocks = 2
#-stimulus names (and stimulus extensions, if images) *
stimName = 'face'
stimExtensiom = '.jpg'
#-stimulus properties like size, orientation, location, duration *
stimSize = [200, 200]
stimOrien = 'landscape'
stimPos = [0.5, 0]
stimDur = [1]
#-start message text *
startMsg = 'Welcome to the experiment! Please press any key to start.'
#=====================
#PREPARE CONDITION LISTS
#=====================
#-check if files to be used during the experiment (e.g., images) exist
pics = []
count = 0
for number in range(10):
    count += 1
    if count < 10:
        pics.append('face0%i.jpg' %count)
    else:
        pics.append('face%i.jpg' %count)

ims_in_dir = sorted(os.listdir(image_dir))
count = 0
n = 0
if not pics == ims_in_dir:
    raise Exception('The image list do not match up!')
else:
    for m in pics:
        count += 1
        if m == ims_in_dir[n]:
            if count < 10:
                print('cat0%i.jpg was found!' %count)
            else:
                print('cat%i.jpg was found!' %count)
            n += 1
        
#-create counterbalanced list of all conditions *
pics
#We don't need to create the counterbalanced list for all conditions as we only have 1 condition, therefore list 'pics' is enough
#=====================
#PREPARE DATA COLLECTION LISTS
#=====================
#-create an empty list for correct responses (e.g., "on this trial, a response of X is correct") *
corrResp = []
#-create an empty list for participant responses (e.g., "on this trial, response was a X") *
Resp = []
#-create an empty list for response accuracy collection (e.g., "was participant correct?") *
accuResp = []
#-create an empty list for response time collection *
timeResp = []
#-create an empty list for recording the order of stimulus identities *
stimID = []
#-create an empty list for recording the order of stimulus properties *
stimID_order = []

#=====================
#CREATION OF WINDOW AND STIMULI
#=====================
#-define the monitor settings using psychopy functions
#-define the window (size, color, units, fullscreen mode) using psychopy functions
#-define experiment start text unsing psychopy functions
#-define block (start)/end text using psychopy functions
#-define stimuli using psychopy functions
#-create response time clock
#-make mouse pointer invisible

#=====================
#START EXPERIMENT
#=====================
#-present start message text
#-allow participant to begin experiment with button press

#=====================
#BLOCK SEQUENCE
#=====================
#-for loop for nBlocks *
for block in nBlocks:
    #-present block start message
    print('Block: ', str(block + 1))
    #-randomize order of trials here *
    np.random.shuffle(pics)
    #-reset response time clock here
    
    #=====================
    #TRIAL SEQUENCE
    #=====================    
    #-for loop for nTrials *
    for trial in nTrials:
        #-set stimuli and stimulus properties for the current trial
        #-empty keypresses
        
        #=====================
        #START TRIAL
        #=====================   
        #-draw stimulus
        #-flip window
        #-wait time (stimulus duration)
        #-draw stimulus
        #-...
        
        #-collect subject response for that trial
        #-collect subject response time for that trial
        #-collect accuracy for that trial
        
#======================
# END OF EXPERIMENT
#======================        
#-write data to a file
#-close window
#-quit experiment