"""
#################
#   Program 2   #
#################

CS 4328.253 
Operating Systems

Dustin Gordon (dmg210)
Jose Mayorga (jmm498)
"""
import random

# initialize variables
REF_STR_SIZE = 100
page_ref_str = []
page_frames_amt = 1
page_frames = []
fifo_faults = 0
fifo_faults_total = 0
lru_faults = 0
lru_faults_total = 0
opt_faults = 0
opt_faults_total = 0
# --------------------


# generate random page reference string
def create_ref_string():
    global page_ref_str
    counter = 0
    while counter < REF_STR_SIZE:
        rand_int = random.randint(0, 49)
        page_ref_str.append(rand_int)
        counter += 1
    print ''
    print 'Generated random page reference string.'
# -------------------------------------


# display contents of page reference string
def print_ref_string():
    logfile = open('page_ref_string.txt', 'w')  # clear existing log
    logfile.close()
    logfile = open('page_ref_string.txt', 'a+')
    print 'Page References:'
    for page in page_ref_str:
        print str(page) + ',',
        logfile.write(str(page))  # save to log file
        logfile.write(',')
    logfile.close()
    print ''
    print '(Page reference string saved to file "page_ref_string.txt")'
    print ''
# -----------------------------------------


# FIFO Algorithm (First In, First Out)
def fifo():
    global fifo_faults
    global page_frames

    fifo_q = list(page_ref_str)  # opt 'stack'

    # Initialize page frames
    for frame in range(page_frames_amt):
        page_frames.append(fifo_q.pop(0))
        fifo_faults += 1  # all empty is a fault

    remaining_pgs_1 = len(fifo_q)

    for index in range(remaining_pgs_1):

        found = False

        for frame_val in page_frames:
            if frame_val == fifo_q[0]:
                found = True
                fifo_q.pop(0)
                break

        # Replace values in page frames
        if not found:
            fifo_faults += 1
            page_frames.pop(0)
            page_frames.append(fifo_q.pop(0))

    # save page fault data to CSV file
    if page_frames_amt == 1:
        logfile = open('data_fifo.csv', 'w')  # clear existing log
        logfile.close()
    logfile = open('data_fifo.csv', 'a+')
    logfile.write(str(fifo_faults))
    logfile.write(',')
    logfile.close()
# ------------------------------------


# LRU Algorithm (Least Recently Used)
def lru():
    global lru_faults
    global page_frames

    lru_stack = list(page_ref_str[::-1])  # reversed of page refs

    # initialize page frames
    for frame in range(page_frames_amt):
        page_frames.append(lru_stack.pop(0))
        lru_faults += 1  # all empty is a fault

    rem_pgs_1 = len(lru_stack)

    for index in range(rem_pgs_1):
        found = False
        for frame_val in page_frames:
            if frame_val == lru_stack[0]:
                found = True
                lru_stack.pop(0)
                break

        if not found:
            lru_faults += 1
            replaced = False
            rem_pgs_2 = len(lru_stack)
            temp_page_frame = list(page_frames)
            for page in range(rem_pgs_2):      # iterate through the pages

                for value in temp_page_frame:  # iterate through the frames
                    if lru_stack[page] == value:
                        temp_page_frame.remove(value)  # assuming no repeated values

                if len(temp_page_frame) == 1:
                    location = page_frames.index(temp_page_frame[0])  # find location of frame to replace
                    page_frames[location] = lru_stack.pop(0)
                    replaced = True
                    break

            if not replaced:  # Replaces in a random location within the bounds of what is left
                rand_loc = random.randint(0, len(temp_page_frame) - 1)
                loc = page_frames.index(temp_page_frame[rand_loc])
                page_frames[loc] = lru_stack.pop(0)  # Finds the page in the frame and replaces it with the new page

    # save page fault data to CSV file
    if page_frames_amt == 1:
        logfile = open('data_lru.csv', 'w')  # clear existing log
        logfile.close()
    logfile = open('data_lru.csv', 'a+')
    logfile.write(str(lru_faults))
    logfile.write(',')
    logfile.close()
# ----------------------------------


# OPT Algorithm (Optimal)
def opt():
    global opt_faults
    global page_frames
    
    opt_stack = list(page_ref_str)  # opt 'stack'
    
    # Initialize page frames
    for frame in range(page_frames_amt):
        page_frames.append(opt_stack.pop(0))
        opt_faults += 1  # all empty is a fault
    
    remaining_pgs_1 = len(opt_stack) 
    
    for index in range(remaining_pgs_1):
    
        found = False    
    
        for frame_val in page_frames:
            if frame_val == opt_stack[0]:
                found = True
                opt_stack.pop(0)
                break
        
        if not found:
        
            opt_faults += 1    
        
            replaced = False    
        
            remaining_pgs_2 = len(opt_stack)
            
            temp_page_frame = list(page_frames)
            
            for page in range(remaining_pgs_2):  # iterate through the pages
                
                for value in temp_page_frame:  # iterate through the frames
                    
                    if opt_stack[page] == value:
                        temp_page_frame.remove(value)  # assuming no repeated values

                if len(temp_page_frame) == 1:
                    location = page_frames.index(temp_page_frame[0])  # finds the location of the frame to be replaced
                    page_frames[location] = opt_stack.pop(0)
                    replaced = True
                    break
        
            # Replaces in a random location within the bounds of what is left
            if not replaced:
                rand_loc = random.randint(0, len(temp_page_frame) - 1)
                loc = page_frames.index(temp_page_frame[rand_loc])
                page_frames[loc] = opt_stack.pop(0)  # Finds the page in the frame and replaces it with the new page

    # save page fault data to CSV file
    if page_frames_amt == 1:
        logfile = open('data_opt.csv', 'w')  # clear existing log
        logfile.close()
    logfile = open('data_opt.csv', 'a+')
    logfile.write(str(opt_faults))
    logfile.write(',')
    logfile.close()
# -----------------------


# main #
print '#############################################'
print '#  Project 2 - Page Replacement Algorithms  #'
print '#############################################'
print '\n'
print 'Enter an integer for the random seed '
print '>> ',
user_input = raw_input()
random.seed = int(user_input)
print 'Seed = ' + str(user_input)

create_ref_string()
print_ref_string()  # debug

# call page replacement methods
for run in range(30):
    print 'Page frame amount = ' + str(page_frames_amt) + ','

    print '  -> Running FIFO... ',
    fifo()
    fifo_faults_total += fifo_faults  # save fault count to grand total
    fifo_faults = 0                   # reset per-run fault count
    page_frames = []                  # reinitialize to empty for next run

    print 'LRU... ',
    lru()
    lru_faults_total += lru_faults  # save fault count to grand total
    lru_faults = 0                  # reset per-run fault count
    page_frames = []                # reinitialize to empty for next run

    print 'OPT...'
    opt()
    opt_faults_total += opt_faults  # save fault count to grand total
    opt_faults = 0                  # reset per-run fault count

    page_frames_amt += 1            # incr frame count for next run

print ''
print 'Algorithm tests completed!'

# output results
raw_avg_fifo = float(fifo_faults_total / 30.0)
print ''
print 'Total page faults with FIFO: ' + str(fifo_faults_total)
print 'Average # faults with FIFO: %.2f' % raw_avg_fifo
print '(Page fault data saved to file "data_fifo.csv")'

raw_avg_lru = float(lru_faults_total / 30.0)
print ''
print 'Total page faults with LRU: ' + str(lru_faults_total)
print 'Average # faults with LRU: %.2f' % raw_avg_lru
print '(Page fault data saved to file "data_lru.csv")'

raw_avg_opt = float(opt_faults_total / 30.0)
print ''
print 'Total page faults with OPT: ' + str(opt_faults_total)
print 'Average # faults with OPT: %.2f' % raw_avg_opt
print '(Page fault data saved to file "data_opt.csv")'
print ''
# -------------------------------
