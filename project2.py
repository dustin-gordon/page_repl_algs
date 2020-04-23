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

    global page_ref_str
    global page_frames
    global fifo_faults
    fifo_list = list(page_ref_str)  # Make an unlinke copy
    page_frames_amt = 1
    for ref in page_ref_str:         # iterate page reference list
        #print('\n** Next page ref = ' + str(ref) + ' **')  # debug
        page_found = False
        for index in range(page_frames_amt):       # look for page in active frames
            if ref == page_frames[index]:            # page found in existing frame
                print('Page found! ref = ' + str(ref) + '; ' + ' frame ' + str(index) + ' = ' + str(page_frames[index]))  # debug
                page_found = True
                break

        if not page_found:  # page fault:
            free_frame_found = False
            frame_counter = 0
            fifo_faults += 1
            
            for index in range(page_frames_amt):         # look for empty frames
                if page_frames[index] == 0:               # found a free frame
                    page_frames[index] = ref  # replace free frame
                    print('Replaced free frame ' + str(frame_counter) + ' with page ' + str(ref))  # debug
                    free_frame_found = True
                    break
                frame_counter += 1
                
            if not free_frame_found:  # page fault: need to replace a non-empty frame via FIFO
                frame_to_swap = fifo_list.pop(0)   # pop frame to be swapped from FIFO queue
                print('Page fault! FIFO faults = ' + str(fifo_faults) + ' Next page in FIFO queue to swap is ' + str(frame_to_swap))
                for index in range(page_frames_amt):
                    if page_frames[index] == frame_to_swap:   # found frame to be swapped
                        page_frames[index] = ref
                        print('Replaced existing frame ' + str(index) + ' = ' + str(page_frames[index]) + ' with page ' + str(ref))  # debug

    print('\nPage faults using FIFO: ' + str(fifo_faults))
# ------------------------------------


# LRU Algorithm (Lest Recently Used)
# TODO: implement LRU
def lru():
    global lru_faults
    
    lru_q = list(page_ref_str)
    
    for index in range(page_frames_amt):
        
    
    
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


# initialize page frames
counter = 1
page_frames_amt = 1
for frame in range(page_frames_amt):
    temp = counter * -1  # debug
    page_frames.append(temp)  # -1 == empty
    print('Frame ' + str(counter) + ' = ' + str(temp))  # debug
    counter += 1

# ----------------------


# call FIFO replacement method
fifo()


# call LRU replacement method
lru()


# call OPT replacement method
opt()

