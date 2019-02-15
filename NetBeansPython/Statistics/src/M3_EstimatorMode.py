#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="epasseto"
__date__ ="$02/08/2012 08:36:25$"

#Complete the mode function to make it return the mode of a list of numbers
data1=[1,2,5,10,-20,5,5]
def mode(data):
    modecnt=0
    for i in range(len(data)):
        icount=data.count(data[i])
        if icount>modecnt:
            mode=data[i]
            modecnt=icount
    return mode

print mode(data1)
