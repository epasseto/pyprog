#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="epasseto"
__date__ ="$15/08/2012 17:01:55$"


def clique(n):
    print 'in a clique...'
    for j in range(n):
        for i in range(j):
            print i, 'is friends with', j

clique(4)
