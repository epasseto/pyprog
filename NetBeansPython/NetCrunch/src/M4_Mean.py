#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="epasseto"
__date__ ="$12/09/2012 11:17:56$"

#list of node centrality values
L = [2, 3, 2, 3, 2, 4]

def mean(L):
    total = 0
    for i in range(len(L)):
        total += L[i]
    return (0.0+total)/len(L)

print mean(L)

#in one command!
#print (0.0+sum(L))/len(L)