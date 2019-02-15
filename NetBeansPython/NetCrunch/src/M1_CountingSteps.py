#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="epasseto"
__date__ ="$15/08/2012 10:49:00$"

import math

def time(n):
    """ Return the number of steps necessary to calculate `print countdown(n)`"""
    return 3 + 2 * math.ceil(n/5.0) #rounded up
    #Return the ceiling of x as a float
    #the smallest integer value greater than or equal to x

def countdown(x):
    y = 0
    while x > 0:
        x = x - 5
        y = y + 1
    print y

print countdown(50)