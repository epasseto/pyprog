#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="epasseto"
__date__ ="$02/08/2012 08:36:03$"

#Complete the variance function to make it return the variance of a list of numbers
data3=[13.04, 1.32, 22.65, 17.44, 29.54, 23.22, 17.65, 10.12, 26.73, 16.43]
def mean(data):
    return sum(data)/len(data)

def variance(data):
    mu = mean(data)
    ndata = []
    for i in range(len(data)):
        ndata.append((data[i]-mu)**2)
    sigma2 = mean(ndata)
    return sigma2

def variance2(data):
    mu=mean(data)
    return mean([(x-mu)**2 for x in data])

def variance3(data): #no use of mean
    xi = 0.0
    xisq = 0.0
    n = len(data)
    for i in data:
        xi+=i
        xisq+=i*i
    return (xisq/n)-((xi**2)/(n**2))

print variance(data3)
