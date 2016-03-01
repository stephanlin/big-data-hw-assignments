"""
CSC 59927-B: Big Data Management & Analysis
Instructor: Huy T. Vo
Author: Weifan Lin
Homework 2, task 1
"""

import csv
import sys
from datetime import date
import collections

if __name__=='__main__':
	if len(sys.argv)<2:
		sys.stderr.write('USAGE: python %s <INPUT_CSV>\n' % sys.argv[0])
		sys.exit(1)


	total = 0
	count = {}

	with open(sys.argv[1], 'r') as fi:
		reader = csv.DictReader(fi)
		for row in reader:
			if row['usertype'] == 'Subscriber':  # we only want age of subscribers
				b_year = row['birth_year']
				count[b_year] = count.get(b_year, 0) + 1
				total += 1


	d = collections.OrderedDict(sorted(count.iteritems()))
	'''
	note that when b-year is sorted, eg. 1990, 1991, 1992, ...
	the age is in a list of from oldest to youngest
	but it does not matter for finding median of age
	'''

	# using the same method to find median as in class
	median_age = 0
	agg = 0
	for k, v in d.iteritems():
		agg += v
		if agg * 2 > total:
			median = k 	# median found but it is b-year, we want age.
			median_age = date.today().year - int(median) # age = today's year - b-year
			break	# once median is found break the for loop

	print median_age
