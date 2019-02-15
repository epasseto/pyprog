#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="epasseto"
__date__ ="$31/07/2012 10:32:47$"

#Confidence Interval
from math import sqrt

def mean(l):
    return float(sum(l))/len(l)

def var(l):
    m = mean(l)
    return sum([(x-m)**2 for x in l])/len(l)

def factor(l):
    return 1.96

def conf(l):
    return factor(l)*sqrt(var(l)/len(l))

def test(l,h):
    m = mean(l)
    c = conf(l)
    print "confidence", c, "h-m", abs(h-m)
    return abs(h-m) <= c

l=[199,200,201,202,203,204]
h=200

print test(l,h)
