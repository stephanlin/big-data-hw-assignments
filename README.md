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

