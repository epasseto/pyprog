#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="epasseto"
__date__ ="$02/08/2012 09:17:28$"

#In class you wrote a function mean that computed the mean of a set of numbers."""
#Consider a case where you have already computed the mean of a set of data and
#get a single additional number. Given the number of observations in the
#existing data, the old mean and the new value, complete the function to return
#the correct mean

from __future__ import division

def mean(oldmean,n,x):
    return (oldmean*n+x)/(n+1)

currentmean=10
currentcount=5
new=4

print mean(currentmean,currentcount,new) #should print 9
