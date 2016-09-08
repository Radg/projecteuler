#! /usr/bin/env python
# -*- coding: utf-8 -*-

# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

lens1to9 = [3, 3, 5, 4, 4, 3, 5, 5, 4]
ten = 3
lens11to19 = [6, 6, 8, 8, 7, 7, 9, 8, 8]
lens20to90 = [6, 6, 5, 5, 5, 7, 6, 6]
hundred = 7
hundredand = 10
onethousand = 11

lens1to99 = sum(lens1to9) + ten + sum(lens11to19) + sum(lens20to90)

for i in lens20to90:
	for j in lens1to9:
		lens1to99 += i + j

grid100to999 = lens1to99 * 10

for i in lens1to9:
	grid100to999 += i + hundred + (i + hundredand) * 99

total = grid100to999 + onethousand

print total
