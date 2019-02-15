#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="epasseto"
__date__ ="$02/10/2012 08:39:14$"

#
# Given a list L of n numbers, find the mode
# (the number that appears the most times).
# Your algorithm should run in Theta(n).
# If there are ties - just pick one value to return
#
from operator import itemgetter

def mode(L):
    Item = L[0]
    Count = 1
    Prov = False
    CountProv = 0
    Index = 1
    print 'O Begin', Item, Count
    while Index < len(L):
        if L[Index] == Item: 
            Count += 1
            print Index,'Count the same, continue', Item, Count
            Index += 1
            continue
        else:
            if Prov == False:
                Prov = L[Index]
                CountProv = 1
                print Index, 'New Provisory', Prov, CountProv
            else:
                if L[Index] == Prov:
                    CountProv += 1
                    print Index, 'Count Provisory', Prov, CountProv
        if CountProv > Count:
            'Provisory now surpasses!'
            Item = Prov
            Prov = False
            Count = CountProv
            CountProv = 0
        Index += 1
    return Item

#L = [1, 5, 2, 5, 3, 5]
L = [2, 4, 7, 2, 6, 9, 2, 3, 1, 8, 4, 6, 7, 1, 5, 6, 8, 4, 6, 6, 1, 2, 2, 7, 5, 3, 4, 7, 5, 3, 4, 2, 1, 8, 3, 3, 5, 4, 3, 5, 2, 10, 6, 3, 3, 5, 5, 6, 3, 4]
print mode(L)

####
# Test
#
import time
from random import randint

def test():
    assert 5 == mode([1, 5, 2, 5, 3, 5])
    iterations = (10, 20, 30, 100, 200, 300, 1000, 5000, 10000, 20000, 30000)
    times = []
    for i in iterations:
        L = []
        for j in range(i):
            L.append(randint(1, 10))
        start = time.clock()
        for j in range(500):
            mode(L)
        end = time.clock()
        print start, end
        times.append(float(end - start))
    slopes = []
    for (x1, x2), (y1, y2) in zip(zip(iterations[:-1], iterations[1:]), zip(times[:-1], times[1:])):
        print (x1, x2), (y1, y2)
        slopes.append((y2 - y1) / (x2 - x1))
    # if mode runs in linear time,
    # these factors should be close (kind of)
    print slopes

#test()
