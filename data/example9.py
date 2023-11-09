#!/usr/bin/python3
'''
------problem--------
find the multiple pf 9 from a random 100 value list
with values between 1 to 1000
'''
import random

aList = range(1,101)

print(list(filter((lambda x:x % 9 == 0), aList)))
