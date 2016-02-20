"""
CSC 59927-B: Big Data Management & Analysis
Instructor: Huy T. Vo
Author: Weifan Lin
Homework 1b, task 2
"""

import sys
import json
import urllib2
import csv

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


	with open(sys.argv[3], 'wb') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow(['Latitude', 'Longitude', 'Stop Name', 'Stop Status'])

		for bus in vehicle_activity_list:
			vehicle_location = bus['MonitoredVehicleJourney']['VehicleLocation']
			latitude = vehicle_location['Longitude']
			longitude = vehicle_location['Longitude']

			onwardCall = bus['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall']
			if onwardCall:
				next_stop_info = onwardCall[0]
				stopName = next_stop_info['StopPointName']
				stopStatus = next_stop_info['Extensions']['Distances']['PresentableDistance']
			else:
				stopName = 'N/A'
				stopStatus = 'N/A'

			row = [latitude, longitude, stopName, stopStatus]
			writer.writerow(row)

			