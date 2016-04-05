## HW1 

######Task 1

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

######Task 2
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

######Task 1
Your task is to compute the median age of the Citibike’s subscribed customers. You are required to read data line by line and are not allowed to store the entire data set in memory. Indeed, you should not have any containers (e.g. list, dictionary, DataFrame, etc.) with more than 100 elements in memory. You can use the citibike.csv data file that we have on Blackboard for testing, but we will evaluate your code on a much larger input to ensure its streaming capability.


EXAMPLE:
```
python hw2_task1.py citibike.csv
39
```


######Task 2
Your task is to write a generator to extract the first ride of the day from a Citibike data stream. The data stream is sorted based on starting times (similar to the citibike.csv file uploaded on Blackboard). The first ride of the day is interpreted as the ride with the earliest starting time of a day. For the sample data, which is a week worth of citibike records, your generator should only generate 7 items (one for each day).

EXAMPLE:
```
python hw2_task2.py citibike.csv
1,,801,2015-02-01 00:00:00+00,2015-02-01 00:14:00+00,521,8 Ave & W 31
St,40.75044999,-73.99481051,423,W 54 St & 9 Ave,40.76584941,-
73.98690506,17131,Subscriber,1978,2
...
```

##HW 3
In this homework, you are expected to familiarize yourself with Python's higher order functions, in particular, map(), filter() and reduce().
```
# This is your input data, a list of subway line status.
# It is a list of string in a specific format

status = [
    '1,2,3 : Good Service',
    '4,5,6 : Delays',
    '7 : Good Service',
    'A,C : Good Service',
    'E : Planned Work',
    'G : Delays',
    'B,D,F,M : Good Service',
    'J,Z : Delays',
    'L : Good Service',
    'N,Q,R : Planned Work',
    'S : Good Service',
]
```
######Task 1
You are provided a list of service status updates scraped from an MTA information website. Each update may indicate Good Service, Planned Work, or Delays for one or more subway lines. Our first objective is to list all the lines that are running with Delays. To guide you through the process, our problem are also split into smaller tasks.
Sub-Task 1
Please complete the lambda expression to filter only the status updates for the lines that run with Delays.
```
delayUpdates = filter(<YOUR EXPRESSION HERE>, status)
# After this, your delayUpdates should be
# ['4,5,6 : Delays', 'G : Delays', 'J,Z : Delays']
```
Sub-Task 2
Please complete the lambda expression below to convert each status line into a list of subway lines, i.e. '4,5,6 : Delays' would become ['4','5','6']
```
delayLineList = map(lambda x: <YOUR EXPRESSION HERE>, delayUpdates)
# After this, your delayLineList should be
# [['4', '5', '6'], ['G'], ['J', 'Z']]
```
Sub-Task 3
Please complete the reduce command below to convert each the list of subway lists given in delayLineList into a single list of subway lines running with delay.
```
delayLines = reduce(lambda x,y: <YOUR EXPRESSION HERE>, delayLineList, <THE INITIAL VALUE OF YOUR REDUCE>)
# After this, your delayLines should be
# ['4', '5', '6', 'G', 'J', 'Z']
```
Sub-Task 4
Please complete the reduce command below to count the number of lines in delayLines.
```
delayLineCount = reduce(lambda x,y: <YOUR EXPRESSION HERE>, delayLines, <THE INITIAL VALUE OF YOUR REDUCE>)
# After this, your delayLineCount should be
# 6
```

######Task 2
In this excercise, we would like to expand the combined service updatse into separate updates for each subway line. For example, instead of having a single line '1,2,3 : Good Service' to indicate that line 1, 2, and 3 are in good service, we would like to convert that into 3 separate updates: '1 : Good Service', '2 : Good Service', and '3 : Good Service'.
You are tasked to write a chain of map(), filter(), and/or reduce() to convert the status variable into a list like below:
```
['1 : Good Service',
 '2 : Good Service',
 '3 : Good Service',
 '4 : Delays',
 '5 : Delays',
 '6 : Delays',
 '7 : Good Service',
 'A : Good Service',
 'C : Good Service',
 'E : Planned Work',
 'G : Delays',
 'B : Good Service',
 'D : Good Service',
 'F : Good Service',
 'M : Good Service',
 'J : Delays',
 'Z : Delays',
 'L : Good Service',
 'N : Planned Work',
 'Q : Planned Work',
 'R : Planned Work',
 'S : Good Service']
 ```
Please note that you may only use higher order functions without access to global variables. Your expression should contain only map(), filter() and/or reduce() and your custom function definitions.
```
<ANY FUNCTION TO BE USED IN YOUR HOF>

newUpdates = <YOUR HOF EXPRESSION> 
# The expected value of newUpdates is the list shown above
```
 
######Task 3
In this excercise, you are tasked to perform a similar task as in Task 2 of Homework 2: extract the first ride of the day from a Citibike data stream. However, instead of iterating through the stream using generators, you are asked to complete the task using higher order functions map(), filter() and/or reduce(). You are free to define additional functions to be used in your higher order functions, however, you are not allowed to use global variables within these functions without being passed in as arguments.
```
<ANY FUNCTION TO BE USED IN YOUR HOF>

with open('citibike.csv','r') as fi:
    reader = csv.DictReader(fi)
    first_birth_years = <YOUR HOF EXPRESSION>
# After this, your first_birth_years should be
# [1978, 1992, 1982, 1969, 1971, 1989, 1963]
```
##HW 5
please write one Hadoop Streaming job, i.e. consisting of a mapper.py and reducer.py file (along with your run_emr.sh code), where you can supply to the Hadoop Streaming framework to produce the top 3 most frequently appeared words in a document (book.txt in this case). For sanity check, please also include your output (the two 3 words and their counts) in your submission.
