#! /usr/bin/env python
# -*- coding: utf-8 -*-

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

i, sp = 1, 20
found = False

while not found:
	for i in range(11, 20):
		if (sp % i) != 0:
			sp += 20
			break
	else:
		found = True

print sp
