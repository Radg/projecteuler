#! /usr/bin/env python
# -*- coding: utf-8 -*-

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

found, a = False, 2

while not found:
	for b in range (a, 1000):
		c = (a ** 2 + b ** 2) ** .5
		if c * c == (a ** 2 + b ** 2) and a + b + c == 1000:
			found = True
			print a, "^2 + ", b, "^2 = ", int(c), "^2"
			print a, "*", b, "*", int(c), "=", int(a*b*c)
			break
	a += 1