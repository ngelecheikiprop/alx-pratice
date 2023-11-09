#!/usr/bin/python3
'''
---------problem-------
make a random list of heads and tails 
count the heads and count the tails 
heads: 46
Tails: 54

'''
import random
flipList = []
for i in range(1, 101):
	flipList += random.choice(['H', 'T'])

#output the results
print("heads : {}".format(flipList.count('H')))
print("heads : {}".format(flipList.count('T')))
