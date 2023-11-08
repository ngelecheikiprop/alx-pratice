#!/usr/bin/python3
def get_func_mul_by_num(num):
	def mult_by(value):
		return num * value
	return mult_by

generated_func = get_func_mul_by_num(5)
print("5 * 10  = {}".format(generated_func(10)))

