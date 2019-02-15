#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="epasseto"
__date__ ="$13/08/2012 13:35:57$"

def naive(a, b):
    x = a
    y = b
    z = 0
    while x > 0:
        z = z + y
        x = x - 1
    return z

def rec_naive(a, b):
    if a == 0:
        return 0
    return b + rec_naive(a-1, b)
