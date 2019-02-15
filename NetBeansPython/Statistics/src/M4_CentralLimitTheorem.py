#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="epasseto"
__date__ ="$02/08/2012 08:37:13$"

#Write a function flip that simulates flipping n fair coins.
#It should return a list representing the result of each flip as a 1 or 0
#To generate randomness, you can use the function random.random() to get
#a number between 0 or 1. Checking if it's less than 0.5 can help your
#transform it to be 0 or 1
#Write a function sample that simulates N sets of coin flips and
#returns a list of the proportion of heads in each set of N flips
#It may help to use the flip and mean functions that you wrote before

import random
from math import sqrt
from plotting import *

def mean(data):
    return float(sum(data))/len(data)

def variance(data):
    mu=mean(data)
    return sum([(x-mu)**2 for x in data])/len(data)

def stddev(data):
    return sqrt(variance(data))

def flipold(N):
    list = []
    i = 0
    while i < N:
        res = random.random()>0.5
        if res == False:
            list.append(0)
        else:
            list.append(1)
        i +=1
    print 'list', list
    return list

def flip(N):
    return [random.random()>0.5 for x in range(N)] #this is a list!

def sample(N):
    #Insert your code here
    return [mean(flip(N)) for x in range(N)] #this is a list!

N=1000
outcomes=sample(N)
histplot(outcomes, nbins=30)