#!/usr/bin/env python3

def addition(s):
    y=0
    for x in s:
        y = y+x
        print(str(y))
    return y



mylist = [1,2,3,4,5]
total = addition(mylist)
print(str(total))