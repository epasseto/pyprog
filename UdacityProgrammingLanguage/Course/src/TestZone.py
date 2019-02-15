#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="epasseto"
__date__ ="$04/07/2013 15:14:44$"

import random

#a = set(['JS', 'JD', '2S', '2C', '7H', '7H'])
#print a

hand1 = ['JS', 'JD', '2S', '2C', '7H', '7A']
#print hand1
hand2 = ['J', 'JD', '2S', '2C', '7H', '8H']
hand3 = ['B', 'JD', '2S', '2C', '7H', '7B']
hand4 = ['K', 'JD', '2S', '2C', '7H', '7H']
hand5 = ['L', 'JD', '2S', '2C', '7H', '7H']

group = [hand1, hand2, hand3, hand4, hand5]
#print poker

'''def poker(hands):
    return max(hands, key=hand_rank)
def hand_rank(hands):
    return random.random()
print poker(group)

def last(s): return s[-1]
print sorted (group, key = last)
a = ':'.join(hand1)
b = a.split(':') #sort by tuples!
print a
print b'''

#print [hand1] + 99*[hand2]
a = ['SF'] + 99*['SH']
print a, len(a)
a.pop(0)
print a, len(a)