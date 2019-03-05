#! /usr/bin/env python
# -*- coding: utf-8 -*-

# n! means n × (n − 1) × ... × 3 × 2 × 1
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# Find the sum of the digits in the number 100!

def factorial(number):
	if number == 1:
		return 1
	else:
		return number * factorial(number - 1)

fact100 = factorial(100)
sum = 0

while fact100 > 1:
	sum += fact100 % 10
	fact100 = fact100 / 10

print(sum)