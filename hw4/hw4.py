import csv
import mapreduce as mr

# task 1
def mapper1(row):
    stations = [row['start_station_name'], row['end_station_name']]
    for station in stations:
        yield (station, 1)

def reducer1(k2v2):
    station, counts = k2v2
    return (station, sum(counts))

with open('citibike.csv', 'r') as fi:
    reader = csv.DictReader(fi)
    output1 = list(mr.run(reader, mapper1, reducer1))

print output1[:10]


# task 2
def mapper2((station,count)):
    if count>1000:
        yield (station,count)

with open('citibike.csv', 'r') as fi:
    reader = csv.DictReader(fi)
    output2 = list(mr.run(mr.run(reader, mapper1, reducer1), mapper2))

print output2

# task 3

def mapper3(row):
    sortedList = sorted([row['start_station_name'], row['end_station_name']])
    pair = tuple(sortedList)
    yield (pair, 1)

def reducer3(k2v2):
    pair, counts = k2v2
    return (pair, sum(counts))

with open('citibike.csv', 'r') as fi:
    reader = csv.DictReader(fi)
    output3 = list(mr.run(reader, mapper3, reducer3))

print output3[:10]


# task 4
def mapper4((station_pair, count)):
    if count>=35:
        for station in list(station_pair):
            yield (station, 1)
    
def reducer4(k2v2):
    station, counts = k2v2
    return (station, sum(counts))

output4 = list(mr.run(output3, mapper4, reducer4))
print output4

# task 5
with open('citibike.csv', 'r') as fi:
    reader = csv.DictReader(fi)
    output5 = list(mr.run(mr.run(reader, mapper3, reducer3), mapper4, reducer4))
print output5


# task 6
def mapper5(row):
    if row['gender'] == '1':
        yield (('Male', row['start_station_name']), 1)
    elif row['gender'] == '2':
        yield (('Female', row['start_station_name']), 1)
    else:
        yield (('Unknown', row['start_station_name']), 1)

def reducer5(k2v2):
    return (k2v2[0][0], (k2v2[0][1], sum(k2v2[1])))

def mapper6(row):
    yield row[0], row[1]
    
def reducer6(k2v2):
    return k2v2[0], sorted(k2v2[1], key = lambda x : x[1])[-1]

with open('citibike.csv', 'r') as fi:
    reader = csv.DictReader(fi)
    output5 = list(mr.run(mr.run(reader, mapper5, reducer5), mapper6, reducer6))

print output5
