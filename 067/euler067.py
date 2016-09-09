#! /usr/bin/env python
# -*- coding: utf-8 -*-

# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

# 3
# 7 4
# 2 4 6
# 8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

# NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 299 altogether! If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)

filename = 'p067_triangle.txt'

grid = [list(map(int, line.rstrip('\n').split())) for line in open(filename)]

def maxtot(g):
	for i in xrange(len(g)-2, -1, -1):
		for j in xrange(i, -1, -1):
			g[i][j] += max(g[i + 1][j], g[i + 1][j + 1])
	return g[0][0]

print maxtot(grid)
