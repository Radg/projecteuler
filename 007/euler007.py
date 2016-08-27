#! /usr/bin/env python
# -*- coding: utf-8 -*-

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10001st prime number?

primeCounter, i = 1, 3

while primeCounter < 10001:
    for j in range(3, int(i ** .5) + 1, 2):
        if i % j == 0:
        	break
    else:
    	primeCounter += 1
    i += 2

print i-2