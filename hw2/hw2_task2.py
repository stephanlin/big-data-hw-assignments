"""
CSC 59927-B: Big Data Management & Analysis
Instructor: Huy T. Vo
Author: Weifan Lin
Homework 2, task 2
"""

import csv
import sys

##################################################
##################################################
def first_ride(reader):
    '''
    Please change this function for task 2 of HW2.
    Currently, it only output the first record.
    '''
    currentDay = ''
    for row in reader:
        if (currentDay != row['starttime'].split(' ')[0]):
            yield row
            currentDay = row['starttime'].split(' ')[0]

##################################################
##################################################

if __name__=='__main__':
    if len(sys.argv)<2:
        sys.stderr.write('USAGE: python %s <INPUT_CSV>\n' % sys.argv[0])
        sys.exit(1)
    
    with open(sys.argv[1], 'r') as fi:
        reader = csv.DictReader(fi)
        for row in first_ride(reader):
            print ','.join(map(row.get, reader.fieldnames))