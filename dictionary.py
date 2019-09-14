#!/usr/bin/python
words ={}
words["SGD"]="Singapore Dollar"
words["INR"]="INDIAN RUPEES"
words["USD"]="US Dollar"

print(words)



for key, value in words.items():
    print(key + " = " +value)

