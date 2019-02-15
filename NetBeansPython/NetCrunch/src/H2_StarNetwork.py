#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="epasseto"
__date__ ="$27/08/2012 14:45:29$"

# Write a program that returns the number of edges
# in a star network that has `n` nodes

def star_network(n):
    # return number of edges
    if n < 2:
        e = 0
    else:
        e = n-1
    return e

print star_network(3)