#!/usr/bin/python3
attack = {'quick' : (lambda : print("Quick attack")),
	'miss' : (lambda : print("missed attack")),
	'power' : (lambda : print("power attack"))}

attack['quick']()

import random

attackKey = random.choice(list(attack.keys()))
attack[attackKey]()
