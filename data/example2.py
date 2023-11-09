#!/usr/bin/python3
'''
-----------------PROBLEM---------------
Create a function that recieves a lsit and a function
the function passed will return true or false if a value of a list is odd
the sorrounnding function will return a list of odd numbers

'''
def is_it_odd(num):
	if num % 2 == 0:
		return False
	else:
		return True

def change_list(list, func):
	oddList = []
	
	for i in list:
		if func(i):
			oddList.append(i)
	return oddList
aList = range(1,20)
print(change_list(aList, is_it_odd)) 
