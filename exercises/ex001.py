#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 13:30:38 2020

Exercise: lists and dictionaries
◻ Given the list: l = [12, 3, -4, 6, -5, 9]
◻ Given the dictionary:
◻ d = {’apple’:3, ’orange’:4, ’tomato’:-5, ’meat’:6,
’potato’:15, ’strawberry’:9}
◻ If a value in the dictionary is found in the list, add the
corresponding key to a string named ’to-buy’ and
print it at the end.
◻ If a value in the dictionary is not found in the list,
chose another value in the list, that is not present in
the dictionary, and assign it to the corresponding
key. Print the updated dictionary at the end.

@author: piyush2017
"""

to_buy = " "

l = [12, 3, -4, 6, -5, 9]
 
d = {'apple':3, 'orange':4, 'tomato':-5, 'meat':6,'potato':15, 'strawberry':9}
 
for l_element in l:
    for key in d:
        if l_element == d[key]:
            to_buy += key
   
print(to_buy)