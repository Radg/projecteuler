#! /usr/bin/env python
# -*- coding: utf-8 -*-

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

i = j = product = 0

def isPalindrome(n):
	string = str(n)
	if string == string[::-1]:
		return True
	else:
		return False

for i in xrange(100, 999):
	for j in xrange(100, 999):
		if isPalindrome(i * j) and (i * j) > product:
			product = i * j

print product
