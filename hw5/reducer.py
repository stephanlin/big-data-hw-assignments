# Weifan Lin
#!/usr/bin/env python
import itertools, operator, sys, heapq

def parsePairs():
    for line in sys.stdin:
        yield tuple(line.strip('\n').split('\t'))

def reducer():
    dic = {}
    for key, pairs in itertools.groupby(parsePairs(), operator.itemgetter(0)):
        count = sum(int(i[1]) for i in pairs)
        dic[key] = count

    for k, v in heapq.nlargest(3, dic.iteritems(), key=operator.itemgetter(1)):
        print k, v

if __name__=='__main__':
    reducer()