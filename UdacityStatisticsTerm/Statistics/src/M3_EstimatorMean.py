#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="epasseto"
__date__ ="$25/07/2012 09:05:30$"

#Complete the mean function to make it return the mean of a list of numbers

data1=[49., 66, 24, 98, 37, 64, 98, 27, 56, 93, 68, 78, 22, 25, 11]

def mean(data):
    return sum(data)/len(data)

print mean(data1)

