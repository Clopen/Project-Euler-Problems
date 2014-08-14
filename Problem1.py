#!/usr/bin/env python

"""Problem 1: Find the sum of all multiples of 3 or 5 between 0 and 1000
         	Solved in python"""

counter = 0

for x in range (0,1000):
	if x%3 == 0 or x%5 == 0:
		counter = counter + x
print counter
