import datetime
import operator
import os
import sys
import time
import pyspark
from operator import add

def indexZones(shapeFilename):
    import rtree
    import fiona.crs
    import geopandas as gpd
    index = rtree.Rtree()
    zones = gpd.read_file(shapeFilename).to_crs(fiona.crs.from_epsg(2263))
    for idx,geometry in enumerate(zones.geometry):
        index.insert(idx, geometry.bounds)
    return (index, zones)
def findN(p, index, zones):
    match = index.intersection((p.x, p.y, p.x, p.y))
    for idx in match:
        if any(map(lambda x: x.contains(p), zones.geometry[idx])):
            return zones['neighborhood'][idx]
    return -1

def findB(p, index, zones):
    match = index.intersection((p.x, p.y, p.x, p.y))
    for idx in match:
        if any(map(lambda x: x.contains(p), zones.geometry[idx])):
            return zones['borough'][idx]
    return -1

def mapToZone(parts):
    import pyproj
    import shapely.geometry as geom
    proj = pyproj.Proj(init="epsg:2263", preserve_units=True)    
    index, zones = indexZones('neighborhoods.geojson')
    
    for line in parts:
        if line.startswith('vendor_id'): continue 
        fields = line.strip('').split(',')
        if fields ==['']: continue
        if all((fields[5],fields[6],fields[9],fields[10])):

            passenger_count = int(fields[3])
            pickup_location  = geom.Point(proj(float(fields[5]), float(fields[6])))
            dropoff_location = geom.Point(proj(float(fields[9]), float(fields[10])))

            pickup_zone = findN(pickup_location, index, zones)
            dropoff_zone = findB(dropoff_location, index, zones)

            if pickup_zone>=0 and dropoff_zone>=0:
                yield ((dropoff_zone, pickup_zone), 1)

def mapper2(k2v2):
    from heapq import nlargest
    k, values = k2v2
    top3 = nlargest(3, values,key=lambda a: a[1])
    return (k,top3)

if __name__=='__main__':
    if len(sys.argv)<3:
        print "Usage: <input files> <output path>"
        sys.exit(-1)

    sc = pyspark.SparkContext()

    trips = sc.textFile(','.join(sys.argv[1:-1]))
    output = trips.mapPartitions(mapToZone).reduceByKey(add).map(lambda x: (x[0][0],(x[0][1],x[1]))).groupByKey().map(mapper2)
    output.saveAsTextFile(sys.argv[-1])