#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="epasseto"
__date__ ="$25/07/2012 09:14:45$"

#Complete the median function to make it return the median of a list of numbers
data1=[1,2,5,10,-20]
def median(data):
    sdata = sorted(data)
    length = len(sdata)
    if length%2 == 1:
        return sdata[length/2]
    else:
        return (sdata[(length/2)-1]+sdata[length/2])/2

print median(data1)
