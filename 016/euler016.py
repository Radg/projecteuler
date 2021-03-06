#! /usr/bin/env python
# -*- coding: utf-8 -*-

# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 2^1000?

res = sum(int(n) for n in bytes(1<<1000))
print res

res = sum(int(n) for n in str(2**1000))	
print res

res = sum(map(int, str(2 ** 1000)))
print res
