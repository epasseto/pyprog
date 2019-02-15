#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="epasseto"
__date__ ="$27/04/2012 09:26:41$"

#------------------
# User Instructions
#
# Hopper, Kay, Liskov, Perlis, and Ritchie live on
# different floors of a five-floor apartment building.
#
# 1.Hopper does not live on the top floor.
# 2.Kay does not live on the bottom floor.
# 3.Liskov does not live on either the top or the bottom floor.
# 4.Perlis lives on a higher floor than does Kay.
# 5.Ritchie does not live on a floor adjacent to Liskov's.
# 6.Liskov does not live on a floor adjacent to Kay's.
#
# Where does everyone live?
#
# Write a function floor_puzzle() that returns a list of
# five floor numbers denoting the floor of Hopper, Kay,
# Liskov, Perlis, and Ritchie.

import itertools

def adjacent(f1, f2):
    return abs(f1-f2) == 1

def higher(f1,f2):
    return f1-f2 >= 1

def other_floor_puzzle():
    floors = bottom, _, _, _, top = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(floors))
    return next((Hopper, Kay, Liskov, Perlis, Ritchie)
        for (Hopper, Kay, Liskov, Perlis, Ritchie) in orderings
        if Hopper is not top                #1
        if Kay is not bottom                #2
        if Liskov is not top or bottom      #3
        if higher(Perlis, Kay)              #4
        if not adjacent(Ritchie, Liskov)    #5
        if not adjacent(Liskov, Kay)        #6
        )

print other_floor_puzzle()

def floor_puzzle():
    floors = bottom, _, _, _, top = [1, 2, 3, 4, 5]
    #print "floors:", floors
    orderings = list(itertools.permutations(floors))
    print "orderings:", orderings
    for (Hopper, Kay, Liskov, Perlis, Ritchie) in orderings:
        if Hopper is not top:                #1
            if Kay is not bottom:                #2
                if Liskov is not top and Liskov is not bottom:      #3
                    if higher(Perlis, Kay):              #4
                        if not adjacent(Ritchie, Liskov):    #5
                            if not adjacent(Liskov, Kay):        #6
                                return [Hopper, Kay, Liskov, Perlis, Ritchie]

def fake_floor_puzzle():
    floors = bottom, _, _, _, top = [1, 2, 3, 4, 5]
    #print "floors:", floors
    orderings = list(itertools.permutations(floors))
    #print "orderings:", orderings
    for (Hopper, Kay, Liskov, Perlis, Ritchie) in orderings:
        if Liskov is not top and Liskov is not bottom:      #3
            print [Liskov],
            
def professor_floor_puzzle():
    floors = bottom, _, _, _, top = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(floors))
    for (Hopper, Kay, Liskov, Perlis, Ritchie) in orderings:
        if (Hopper is not top       #1
        and Kay is not bottom       #2
        and Liskov is not top       #ea
        and Liskov is not bottom    #3b
        and Perlis > Kay            #4
        and abs(Richtie - Liskov)>1 #5
        and abs(Liskov - kay)1:     #6
        return [Hopper, Kay, Liskov, Perlis, Richtie]