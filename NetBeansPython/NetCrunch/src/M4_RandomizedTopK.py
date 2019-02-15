#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="epasseto"
__date__ ="$14/09/2012 16:17:30$"

# Write partition to return a new array with
# all values less then `v` to the left
# and all values greater then `v` to the right
#

import random


L = [31, 45, 91, 51, 66, 82, 28, 33, 11, 89, 84, 27, 36]

def partition(L, v):
    smaller = []
    bigger = []
    for val in L:
        if val < v: smaller += [val]
        if val > v: bigger  += [val]
    #return smaller+ [v]+ bigger #glue all together
    return (smaller, [v], bigger) 

#print partition(L, 84)

def top_k(L, k):
    v = L[random.randrange(len(L))]
    (left, middle, right) = partition(L,v)
    if len(left)   == k: return left #done!
    if len(left)+1 == k: return left+[v] #still know the answer!
    if len(left)   >  k: return top_k(left,k) #recursive call1 (make some progess)
    return left+[v]+top_k(right, k-len(left)-1) #recursive call2

print top_k(L, 5)

def rank(L, v):
    pos = 0
    for val in L:
        if val < v:
            pos += 1
    return pos


