#!/usr/bin/env python
import itertools, operator, sys, heapq

def parsePairs():
	for line in sys.stdin:
		yield tuple(line.strip('\n').split('\t'))


dic = {}

def reducer():
	for key, pairs in itertools.groupby(parsePairs(), operator.itemgetter(0)):
		count = sum(int(i[1]) for i in pairs)
		dic[key] = count
	sortedList = (sorted(dic.iteritems(), key=operator.itemgetter(1)))[::-1] # reversed

	for k, v in sortedList[:3]:
		print k, v

if __name__=='__main__':
    reducer()