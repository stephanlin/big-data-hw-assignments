#!/usr/bin/env python
import sys, time, operator

def parseRecords():
    for line in sys.stdin:
        line = line.strip('\n')
        yield line.split()

def mapper():
	for words in parseRecords():
		for w in words:
			print '%s\t%s' % (w,1)


if __name__=='__main__':
    mapper()
