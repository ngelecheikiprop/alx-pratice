#!/usr/bin/python3

oneto10 = range (1,11)

def dbl_num(num):
	return num * 2

print (list(map(dbl_num, oneto10)))
print(list(map((lambda x:x ** 3), oneto10)))

aList  = list(map((lambda x,y:x + y),[1,2,3],[1,2,3]))
