#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="epasseto"
__date__ ="$02/08/2012 08:34:31$"

#Return the probability of A condioned on B given that
#P(A)=p0, P(B|A)=p1, and P(Not B|Not A)=p2

def f1(p0,p1,p2): #Positive case (Test: Positive, P(have))
  JointCPos = (p0*p1)
  JointNPos = (1-p0)*(1-p2)
  Normalizer = JointCPos + JointNPos
  return JointCPos/Normalizer

print f1(0.1,0.9,0.8)

def f2(p0,p1,p2): #Negative case (Test: Negative, P(have))
  JointCNeg = p0*(1-p1)
  JointNNeg = (1-p0)*p2
  Normalizer = JointCNeg + JointNNeg
  return JointCNeg/Normalizer

print f2(0.1,0.9,0.8)