# page_repl_algs

	CS 4328 Operating Systems
	Programming Assignment 2

	Dustin Gordon - dmg210
	Jose Mayorga  - jmm498

"The page replacement algorithm" is a program written to test several virtual-memory page replacement algorithms, specifically
First-In, First-Out (FIFO), Least Recently Used (LRU) and Optimal (OPT). The goalis to asses the performance of the algorithms 
with respect to the amount of page faults incurred accross  varying numbers of physical-memory page frames available. Each
algorithm is tested with 1-30 page frames, using a ramdonly generated page reference string of 100 numeric values 
in the range of 0 - 49, the page faults incurred are written to corresponding output files in CSV format.

# To compile and run:

Please copy "project2.py" to a Linux environment, and enter the following command to compile and run:

	python project2.py
