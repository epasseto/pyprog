#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="epasseto"
__date__ ="$16/05/2012 14:38:22$"


import math
million = 1000000

def Q(state, action, U):
    #the expected value of taking action in state, acoording to utility U
    if action == 'hold':
        return U(state + 1*million)
    if action == 'gamble':
        return U(state + 3*million) * .5 + U(state) * .5

def actions(state): return ['hold', 'gamble']

def identity(x): return x #refering itself

#U = identity

U = math.log10

def best_action(state, actions, Q, U):
    #return the optimal action for a state, given U
    def EU(action): return Q(state, action, U)
    return max(actions(state), key=EU) #average utility given the probabilities

#print best_action(100, actions, Q, identity)

#print best_action(100, actions, Q, math.log)

print best_action(1.0*million, actions, Q, math.log)
