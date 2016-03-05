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


delayUpdates = filter(lambda x: x.split(' : ')[1]=='Delays', status)
print delayUpdates
# After this, your delayUpdates should be
# ['4,5,6 : Delays', 'G : Delays', 'J,Z : Delays']

delayLineList = map(lambda x: x.split(' : ')[0].split(','), delayUpdates)
print delayLineList
# After this, your delayLineList should be
# [['4', '5', '6'], ['G'], ['J', 'Z']]


import operator
delayLines = reduce(lambda x,y: operator.add(x,y), delayLineList, [])
print delayLines
# After this, your delayLines should be
# ['4', '5', '6', 'G', 'J', 'Z']

delayLineCount = reduce(lambda x,y: x+1, delayLines, 0)
print delayLineCount
# After this, your delayLineCount should be
# 6