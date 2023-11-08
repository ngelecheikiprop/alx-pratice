#!/usr/bin/python3
def mul_by_2(num):
	return num * 2

def do_math(func, num):
	return func(num)
print ("8 * 2 = {}".format(do_math(mul_by_2, 8)))
