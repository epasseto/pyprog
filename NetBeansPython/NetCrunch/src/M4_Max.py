#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="epasseto"
__date__ ="$12/09/2012 14:49:20$"

#
# Write `max`
#

def max(L):
    if len(L) > 0:
        maximum = L[0]
        for i in range (1, len(L)):
            if L[i] > maximum:
                maximum = L[i]
        return maximum
    else: return 0

def max_new(L):
    maximum = L[0]
    for i in range (1, len(L)):
        if L[i] > maximum: maximum = L[i]
    return maximum

def test():
    L = [1, 2, 3, 4]
    assert 4 == max(L)
    L = [3, 6, 10, 9, 3]
    assert 10 == max(L)

test()
