#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 20×20 grid?

gridSize = 21

grid = [[0]*gridSize for i in range(gridSize)]

for i in xrange(gridSize - 1):
	grid[i][gridSize-1] = grid[gridSize-1][i] = 1

# print grid

# grid = [[0] * (gridSize - 1) + [1]] * (gridSize - 1) + [[1] * gridSize]

def routesNum(n, m):
	if n == 1 or m == 1: 
		grid[n-1][m-1] = 1
		return 1
	if grid[n-1][m-1]:
		return grid[n-1][m-1]
	else:
		grid[n-1][m-1] = routesNum(n - 1, m) + routesNum(n, m - 1)
		return grid[n-1][m-1]


for i in xrange(gridSize - 2, -1, -1):
	for j in xrange(i, -1, -1):
		grid[i][j] = grid [j][i] = grid[i+1][j] + grid[i][j+1]
	print gridSize-i, ": ", grid[i][i]

print grid[0][0]


# for i in xrange(0, gridSize):

# for i in xrange(0, 5):
# 	grid[i][gridSize - 2] = 1
# 	print grid

# print routesNum(gridSize, gridSize)
# print grid

# for i in xrange(1, 6):
# 	print ("Routes for %d x %d grid is: %d " % (i, i, routesNum(i, i)))

# print grid
