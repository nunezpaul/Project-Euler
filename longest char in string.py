#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 00:25:29 2017

@author: p
"""

string = "aabsdnfkjenfwnjwknfbcddbbbea"

def maxSingleChar(string):
    unique = set(string)
    
    maxcharlen = 0
    iterations = 0
    for i in unique:
        
        i_count = string.count(i)
        for j in range(1,i_count+1):
            test = string.count(i*j)
            iterations+=1
            if test is not 0 and j > maxcharlen:
                maxcharlen = j
                maxchar = i
            elif test is 0:
                break
            
    return {maxchar:maxcharlen}, iterations

#will result in less iterations than a single for loop through the chars of the string
result = maxSingleChar(string)
