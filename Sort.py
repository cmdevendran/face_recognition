#!/usr/bin/env python3
from operator import itemgetter

x = [3,6,21,1,5,98,4,23,1,6]
x.sort()
print (x)
x = list(reversed(x))
print(x)

words = ["Be","Car","Always","Door","Eat" ]
#words.sort()
words = words[::-1]
print(words)

x1 = [ (3,6),(4,7),(5,9),(8,4),(3,1)]

x2= x1.sort(key=itemgetter(1))
x1.sort()
print( x1)
print( x2)