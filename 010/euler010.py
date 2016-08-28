#! /usr/bin/env python
# -*- coding: utf-8 -*-

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

sum, n = 2, 2000000

for i in range(3, n+1, 2):
    for j in range(3, int(i ** .5) + 1):
        if i % j == 0:
             break
    else:
        sum += i

print sum