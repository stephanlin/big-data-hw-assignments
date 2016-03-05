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

def mapper(x):
    line = x.split(" : ")[0].split(',')
    lineStatus = x.split(" : ")[1]
    newList = map(lambda x: x + ' : ' + lineStatus, line)
    return newList

newUpdates = reduce(lambda x,y: x+y, map(mapper, status), [])

print newUpdates
# The expected value of newUpdates is the list shown below
'''
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
 '''