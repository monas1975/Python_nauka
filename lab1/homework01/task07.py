#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Napisz funkcję char_sum, która dla zadanego łańcucha zwraca
sumę kodów ASCII znaków. Wykorzystaj funkcję ord()
"""

def char_sum(text):
    sum=0
    temp = list(text)

    for item in temp:
        sum+=ord(item)
    return sum

input = "this is a string"
#output = 1516

print(char_sum(input))

