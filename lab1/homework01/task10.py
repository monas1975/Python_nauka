#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Napisz funkcję common_chars(string1, string2), która zwraca alfabetycznie
uporządkowaną listę wspólnych liter z lańcuchów string1 i string2.
Oba napisy będą składać się wyłacznie z małych liter.
"""


def common_chars(string1, string2):
    result=[]
    string1 = string1.replace(' ', '')  #usuwam spacje
    l1 = list(string1)                  #zamieniam string na liste
    l1=list(dict.fromkeys(l1)) #usuwam duplikaty z listy
    string2 = string2.replace(' ', '')
    l2 = list(string2)
    l2 = list(dict.fromkeys(l2))

    for item in l1:
        print(item)
        if item in l2:
            result.append(item)
    result.sort()
    return result


input1 = "this is a string"
input2 = "ala ma kota"
output = ['a', 't']


print(common_chars(input1,input2))