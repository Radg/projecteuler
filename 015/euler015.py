#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 20×20 grid?

gridSize = 20

lst = [1] * gridSize

for i in xrange(gridSize):
	for j in xrange(i):
		lst[j] += lst[j - 1]
	lst[i] = 2 * lst[i - 1]

print lst[-1]
