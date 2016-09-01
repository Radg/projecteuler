#! /usr/bin/env python
# -*- coding: utf-8 -*-

# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.

lensDict = {} # Dictionary to store sequences lengths for number, key is a number, value is a sequence length

for i in xrange(1, 1000001):
	n, length = i, 1
	while n > 1:
		if n in lensDict:
			length += lensDict[n] - 1
			break
		else:
			if n & 1:
				n = (3 * n + 1) >> 1
				length += 2
			else:
				n >>= 1
				length += 1
	lensDict[i] = length

maxlength = max(lensDict.values())
print ("Number %d has maximum sequence length equal to %d" % (lensDict.keys()[lensDict.values().index(maxlength)], maxlength))

