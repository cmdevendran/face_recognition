#!/usr/bin/env python3

city = ['Tokyo','New York','Toronto','Hong Kong']
print('Cities loop:')
for x in city:
    print('City: ' + x)

print('\n')  # newline

num = [1,2,3,4,5,6,7,8,9]
print('x^2 loop:')
for x in num:
    y = x * x
    print(str(x) + '*' + str(x) + '=' + str(y))


max = 0
x1=0

# While loop example
while max<=7:
    x1=x1+max
    print("Loop number "+str(max)+" total "+ str(x1))
    max=max+1
    

