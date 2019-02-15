#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="epasseto"
__date__ ="$02/10/2012 08:38:41$"
# Given a list of numbers, L, find a number, x, that
# minimizes the sum of the square of the difference
# between each element in L and x: SUM_{i=0}^{n-1} (L[i] - x)^2
#
# Your code should run in Theta(n) time
#

def minimize_square(L):
    x=0.0
    Count=0
    if len(L) == 0: return x
    while len(L) > 0:
        NewNumber = L.pop()
        Alfa = Count/(Count+1.0)
        Beta = 1.0/(Count+1)
        x = abs(Alfa*x) + abs(Beta*NewNumber)
        x = x * x
        Count += 1
        print NewNumber, x, Count, Alfa, Beta
    return x
