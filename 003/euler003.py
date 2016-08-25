#! /usr/bin/env python
# -*- coding: utf-8 -*-

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

number = 600851475143

def primefactors(n):
	factors, d = [], 3
	while d * d <= n:
		if n % d == 0:
			factors.append(d)
			n //= d
		else:
			d += 2
	if n > 1:
		factors.append(n)
	return factors

print(primefactors(number)[-1])
