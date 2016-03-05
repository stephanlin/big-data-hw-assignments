import sys
import csv
from dateutil.parser import parse

def get_first(record1, record2):
	st2 = record2['starttime'].split(' ')[0]
	if record1 == []:
		record1.append(st2+','+record2['birth_year'])
		return record1
	elif record1[-1].split(',')[0] != st2:
		record1.append(st2+','+record2['birth_year'])
		return record1
	else:
		return record1


with open('citibike.csv','r') as fi:
	reader = csv.DictReader(fi)
	first_birth_years = map(lambda x: x.split(',')[1], reduce(get_first, reader, []))
print first_birth_years