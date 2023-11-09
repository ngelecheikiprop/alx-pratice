#!/usr/bin/python3

#---------sum  lambda function--------
sum  = lambda x, y : x + y
print ("2 + 2  = {}".format(sum(2,2)))

#---can vote lambada function-----
can_vote = lambda age: True if age >= 18 else False
print("can vote :{}".format(can_vote(10)))

#-----list of functions-------------
powerList = [lambda x: x**2,
		lambda x: x**3,
		lambda x: x**4,
		lambda x: x**5]

for func in powerList:
	print(func(4))

