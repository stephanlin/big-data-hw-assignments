"""
CSC 59927-B: Big Data Management & Analysis
Instructor: Huy T. Vo
Author: Weifan Lin
Homework 1b, task 1
"""

import sys
import json
import urllib2

if __name__ == '__main__':
    mta_key = sys.argv[1]
    bus_line = sys.argv[2]
    url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?'+\
    		'key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (mta_key, bus_line)
    try:
    	request = urllib2.urlopen(url)
    except:
	    print 'ERROR!! Unable to request the api, api key is invalid.'
	    sys.exit(1)

    metadata = json.loads(request.read())

    try: 
	    vehicle_activity_list = metadata['Siri']['ServiceDelivery']\
	    						['VehicleMonitoringDelivery'][0]['VehicleActivity']
    except:
	    print 'ERROR!! No such route, bus line is invalid.'
	    sys.exit(1)


    print 'Bus Line : %s \nNumber of Active Buses : %d ' % \
    		(bus_line, len(vehicle_activity_list))
	
    n = 0
    for bus in vehicle_activity_list:
    	vehicle_location = bus['MonitoredVehicleJourney']['VehicleLocation']
    	print 'Bus %d is at latitude %f and longitude %f' % \
    	(n, vehicle_location['Longitude'], vehicle_location['Longitude'])
    	n+=1
