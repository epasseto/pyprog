#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="epasseto"
__date__ ="$15/08/2012 11:04:21$"

# counting steps in naive as a function of a

def naive(a, b):
    x = a
    y = b
    z = 0
    while x > 0:
        z = z + y
        x = x - 1
    return z

def time(a):
    # The number of steps it takes to execute naive(a, b)
    # as a function of a
    steps = 0
    return 3 + a*2
