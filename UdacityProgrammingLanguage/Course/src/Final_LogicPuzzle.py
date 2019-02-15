#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="epasseto"
__date__ ="$28/05/2012 15:03:33$"

"""
UNIT 2: Logic Puzzle
You will write code to solve the following logic puzzle:
1. The person who arrived on Wednesday bought the laptop.
2. The programmer is not Wilkes.
3. Of the programmer and the person who bought the droid,
   one is Wilkes and the other is Hamming. ###PROBLEM
4. The writer is not Minsky.
5. Neither Knuth nor the person who bought the tablet is the manager. ###PROBLEM
6. Knuth arrived the day after Simon.
7. The person who arrived on Thursday is not the designer.
8. The person who arrived on Friday didn't buy the tablet.
9. The designer didn't buy the droid.
10. Knuth arrived the day after the manager.
11. Of the person who bought the laptop and Wilkes,
    one arrived on Monday and the other is the writer. ##PROBLEM
12. Either the person who bought the iphone or the person who bought the tablet
    arrived on Tuesday. ##PROBLEM
You will write the function logic_puzzle(), which should return a list of the
names of the people in the order in which they arrive. For example, if they
happen to arrive in alphabetical order, Hamming on Monday, Knuth on Tuesday, etc.,
then you would return: ['Hamming', 'Knuth', 'Minsky', 'Simon', 'Wilkes']
(You can assume that the days mentioned are all in the same week.)
"""

import itertools

def dayafter(d1,d2): #dayafter(Knuth,Simon) == True
    return d1-d2 == 1

def logic_puzzle():
    "Return a list of the names of the people, in the order they arrive."
    days = Monday, Tuesday, Wednesday, Thursday, Friday = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(days))
    #print 'days:', days
    #print 'orderings:', orderings
    return next([Hamming, Knuth, Minsky, Simon, Wilkes]
        for (Hamming, Knuth, Minsky, Simon, Wilkes) in orderings
        if dayafter(Knuth, Simon) #6
        for (manager, writer, designer, programmer, undefined) in orderings
        if programmer is not Wilkes #2
        if designer is not Thursday#7
        if writer is not Minsky #4
        for (laptop, droid, droid, tablet, iphone) in orderings
        if laptop is Wednesday#1
        if tablet is Friday#8
        if droid is not designer #9
        )
    
print logic_puzzle()
