#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="epasseto"
__date__ ="$14/08/2012 08:53:25$"

def russian(a,b):
    x = a; y = b
    z = 0
    while x > 0:
        if x%2 == 1: z = z + y #add if x is odd!
        y = y << 1             #y doubles
        x = x >> 1             #x divides to half
    return z

print russian(14,11)

#russian expressed recursively

def rec_russian(a,b): #multiply a and b together
    if a   == 0 : return 0
    if a%2 == 0 : return 2*rec_russian(a/2,b) #a is even case
    return b + 2*rec_russian((a-1)/2,b)