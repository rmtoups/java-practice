#!/usr/bin/env python

pieces = {1: ['a','b','c','d','e','f','g','h'], 2: ['b','e','h'], 3: ['a','b','c','d']. 4: ['i','j','k','l'], 5: ['g','h','m','n']}
weights = []

for p1 in pieces.keys():
	for p2 in pieces.keys():
		if p1 != p2:

