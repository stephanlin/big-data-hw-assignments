## HW1 

###Task 1

You are required to write a Python script to retrieve and reporting information about active vehicle for a bus line. The final hand-in should be a single Python file, named show_bus_locations.py that takes exactly 2 arguments in the following format:
```python show_bus_locations.py <MTA_KEY> <BUS_LINE>```

where you can assume that <MTA_KEY> and <BUS_LINE> are valid and could be used to plug in the MTA URL above. For example, the program could be run as:

SAMPLE INPUT:  

```python show_bus_locations.py xxxx-xxxx-xxxx-xxxx-xxxx B52```

The above command has to fetch data from the MTA website through the SIRI API using the provided key and return information on all available vehicles for the bus line B52. Your program will have to output the following to the console, which consists of the bus name, the number of vehicles and their current position:

SAMPLE OUTPUT:

```
Bus Line : B52
Number of Active Buses : 5
Bus 0 is at latitude 40.687241 and longitude -73.941661
Bus 1 is at latitude 40.690822 and longitude -73.920759
Bus 2 is at latitude 40.688363 and longitude -73.979563
Bus 3 is at latitude 40.688282 and longitude -73.979356
Bus 4 is at latitude 40.686839 and longitude -73.964694 
```

###Task 2
In this assignment, we will build on the previous like to build on the previous assignment by adding more information to the buses. In particular, we would like display information on the next stop location of the bus. For example, whether the bus is approaching a stop, or is 1 stop away from it. Again, all these information are already included in the response JSON. We just need to extract them appropriately. Similar to the lab session, we will output the data to a CSV file instead of the decorated strings on screen. For buses that do not have this information, please output “N/A” in the stop information fields. The final hand-in should be a single Python file, named get_bus_info.py that takes exactly 3 arguments in the following format:

INPUT:

```python get_bus_info.py xxxx-xxxx-xxxx-xxxx-xxxx M7 M7.csv```

SAMPLE OUTPUT CONTENTS OF M7.CSV:

```
Latitude,Longitude,Stop Name,Stop Status
40.755489,-73.987347,7 AV/W 41 ST,at stop
40.775657,-73.982036,BROADWAY/W 69 ST,approaching
40.808332,-73.944979,MALCOLM X BL/W 127 ST,approaching
40.764998,-73.980416,N/A,N/A
40.804702,-73.947620,MALCOLM X BL/W 122 ST,< 1 stop away
40.776950,-73.981983,AMSTERDAM AV/W 72 ST,< 1 stop away
40.737650,-73.996626,AV OF THE AMERICAS/W 18 ST,< 1 stop away
```

## HW2 

###Task 1
Your task is to compute the median age of the Citibike’s subscribed customers. You are required to read data line by line and are not allowed to store the entire data set in memory. Indeed, you should not have any containers (e.g. list, dictionary, DataFrame, etc.) with more than 100 elements in memory. You can use the citibike.csv data file that we have on Blackboard for testing, but we will evaluate your code on a much larger input to ensure its streaming capability.


EXAMPLE:
```
python hw2_task1.py citibike.csv
39
```


### Task 2
Your task is to write a generator to extract the first ride of the day from a Citibike data stream. The data stream is sorted based on starting times (similar to the citibike.csv file uploaded on Blackboard). The first ride of the day is interpreted as the ride with the earliest starting time of a day. For the sample data, which is a week worth of citibike records, your generator should only generate 7 items (one for each day).

EXAMPLE:
```
python hw2_task2.py citibike.csv
1,,801,2015-02-01 00:00:00+00,2015-02-01 00:14:00+00,521,8 Ave & W 31
St,40.75044999,-73.99481051,423,W 54 St & 9 Ave,40.76584941,-
73.98690506,17131,Subscriber,1978,2
...
```
