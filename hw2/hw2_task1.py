"""
CSC 59927-B: Big Data Management & Analysis
Instructor: Huy T. Vo
Author: Weifan Lin
Homework 2, task 1
"""

import csv
import sys
import pandas as pd
from datetime import date
import numpy as np
import collections

if __name__=='__main__':
	if len(sys.argv)<2:
		sys.stderr.write('USAGE: python %s <INPUT_CSV>\n' % sys.argv[0])
		sys.exit(1)

	citibike = pd.read_csv(sys.argv[1])
	steam = list(citibike['birth_year']).__iter__()
	total = 0
	count = {}

	for i in steam:
		if not np.isnan(i): # an empty b-year can be read as nan in type of 'numpy.float64'
			count[i] = count.get(i, 0) + 1
			total += 1

	d = collections.OrderedDict(sorted(count.iteritems()))
	'''
	note that when b-year is sorted, eg. 1990, 1991, 1992, ...
	the age is in a list of from oldest to youngest
	but it does not matter for finding median of age
	'''

	# using the same method to find median as in class
	agg = 0
	for k, v in d.iteritems():
		agg += v
		if agg * 2 > total:
			median = k 	# median here is b-year and its in type of 'numpy.float64', we want age.
			break	# once median is found break the for loop

	# age = today's year - b-year
	median_age = date.today().year - int(median)
	print median_age
