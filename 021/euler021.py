#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
# Evaluate the sum of all the amicable numbers under 10000.

def getFactors(n):
	factors, d = [], 1
	while d <= n // 2:
		if n % d == 0:
			factors.append(d)
		d += 1
	return factors

amicableNums = []

for i in range(4, 9999):
	s = sum(getFactors(i))
	if s != i and i == sum(getFactors(s)) and i not in amicableNums:
		amicableNums.append(i)
		amicableNums.append(s)

print(sum(amicableNums))