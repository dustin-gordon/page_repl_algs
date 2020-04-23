#!/usr/bin/env python
#################
#   Program 2   #
#################
"""
CS 4328.253 
Operating Systems

Dustin Gordon (dmg210)
Jose Mayorga (jmm498)
"""
import random
#import Queue

# initialize variables
REF_STR_SIZE = 100
page_ref_str = []
page_frames_amt = 0
page_frames = []
fifo_faults = 0
lru_faults = 0
opt_faults = 0
# --------------------


# generate random page reference string
def create_ref_string():
    #global page_ref_str
    counter = 0
    while counter < REF_STR_SIZE:
        rand_int = random.randint(0, 49)
        page_ref_str.append(rand_int)
        counter += 1
# -------------------------------------

# display contents of page reference string
def print_ref_string():
    print('Page Reference String:')
    for page in page_ref_str:
        print(str(page) + ',')
    print('')
# -----------------------------------------

# FIFO Algorithm (First In, First Out)
# TODO: implement FIFO
def fifo():


    print('\nPage faults using FIFO: ' + str(fifo_faults))
# ------------------------------------


# LRU Algorithm (Lest Recently Used)
# TODO: implement LRU
def lru():
    global lru_faults
    global page_frames
    
    lru_stack = list(page_ref_str) # LRU 'stack'
    
    page_frames_amt = 3
    
    # Initialize page frames
    for frame in range(page_frames_amt):
        page_frames.append(lru_stack.pop(0))
        lru_faults += 1 # all empty is a fault
    
    remaining_pgs_1 = len(lru_stack) 
    
    for index in range(remaining_pgs_1):
    
        found = False    
    
        for frame_val in page_frames:
            if frame_val == lru_stack[0]:
                found = True
                lru_stack.pop(0)
                break
        
        if found != True:
        
            lru_faults += 1    
        
            replaced = False    
        
            remaining_pgs_2 = len(lru_stack)
            
            temp_page_frame = list(page_frames)
            
            for page in range(remaining_pgs_2):  # iterate through the pages
                
                for value in temp_page_frame:  # iterate through the frames
                    
                    if lru_stack[page] == value:
                        temp_page_frame.remove(value) # assuming no repeated values
    
    
                if len(temp_page_frame) == 1:
                    location = page_frames.index(temp_page_frame[0]) # finds the location of the frame to be replaced
                    page_frames[location] = lru_stack.pop(0)
                    replaced = True
                    break
        
            # Replaces in a random location within the bounds of what is left
            if replaced != True:
                rand_loc = random.randint(0, len(temp_page_frame) - 1)
                loc = page_frames.index(temp_page_frame[rand_loc])
                page_frames[loc] = lru_stack.pop(0) # Finds the page in the frame and replaces it 
                                                                                            # with the new page
            
        
    
    print('\nPage faults using LRU: ' + str(lru_faults))
# ----------------------------------


# OPT Algorithm (Optimal)
# TODO: implement OPT
def opt():
    global opt_faults
    print('\nPage faults using OPT: ' + str(opt_faults))
# -----------------------


# main #
print '#############################################'
print '#  Project 2 - Page Replacement Algorithms  #'
print '#############################################'
print '\n'
print 'Enter an integer for random seed: ',
random.seed = int(raw_input())
create_ref_string()
print_ref_string()

# determine number of page frames
validInput = False
while not validInput:
    print 'Enter amount of physical memory page frames (1 to 30),'
    print 'or enter -1 for a random amount: ',
    temp_input = raw_input()
    if int(temp_input) == -1:
        page_frames_amt = random.randint(1, 30)
        validInput = True
    elif 1 <= int(temp_input) <= 30:
        page_frames_amt = int(temp_input)
        validInput = True
    else:
        print 'Invalid input! Try again.\n'

print 'Number of page frames = ' + str(page_frames_amt)
# -------------------------------




# ----------------------


# call FIFO replacement method
fifo()


# call LRU replacement method
lru()


# call OPT replacement method
opt()

