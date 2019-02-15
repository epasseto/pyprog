#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="epasseto"
__date__ ="$08/05/2012 08:20:53$"

import doctest 
#write notes with your class items and function items and automatically run out this tests

class Test: """
>>> successors(0, 0, 4, 9)
{(0, 9): 'fill Y', (0, 0): 'empty Y', (4, 0): 'fill X'}

>>> successors(3, 5, 4, 9)
{(4, 5): 'fill X', (4, 4): 'X<-Y', (3, 0): 'empty Y', (3, 9): 'fill Y', (0, 5): 'empty X',

>>> successors(3, 7, 4, 9)
{(4, 7): 'fill X', (4, 6): 'X<-Y', (3, 0): 'empty Y', (0, 7): 'empty X', (3, 9): 'fill Y',

>>> pour_problem(4, 9, 6)
[(0, 0), 'fill Y', (0, 9), 'X<-Y', (4, 5), 'empty X', (0, 5), 'X<-Y', (4, 1), 'empty X', (0

## What problem, with X, Y, and goal < 10, has the longest solution?
## Answer: pour_problem(7, 9, 8), with 14 steps

>>> def num_actions(triplet): X, Y, goal = triplet; return len(pour_problem(X, Y, goal)) //

>>> def harness(triplet): X, Y, goal = triplet; return num_actions((X, Y, goal)) - max(X,

>>> max([(X, Y, goal) for X in range(1, 10) for Y in range(1, 10)
...                   for goal in range(1, max(X, Y))], key=num_actions)
(7, 9, 8)
>>> max([(X, Y, goal) for X in range(1, 10) for Y in range(1, 10)
...                   for goal in range(1, max(X, Y))], key=hardness)
(7, 9, 8)
>>> pour_problem(7, 9, 8)
[(0, 0), 'fill Y', (0, 9), 'X<-Y', (7, 2), 'empty X', (0, 2), 'X<-Y', (2, 0), 'fill Y, (2
"""

def pour_problem(X, Y, goal, start=(0,0)):
#X and Y are the capacity of glasses
#(x,y) is current fill levels and represents a state
#The goal is a level that can be in either glass
#start at start state and follow successors until we reach the goal
#keep track of frontier and previously explored
#fail when no frontier
    if goal in start:
        return [start]
    explored = set() #set of states whe have visited
    frontier = [[start]] #ordered list of paths we have blazed
    while frontier:
            path = frontier.pop(0) #pull element of the begin of the frontier
            (x, y) = path[-1] #last state in the first paht of the frontier
            for (state, action) in successors(x, y, X, Y).items():
                if state not in explored:
                    explored.add(state)
                    path2 = path + [action, state]
                    if goal in state:
                        return path2
                    else:
                        frontier.append(path2)
    return Fail

Fail = []

def successors(x, y, X, Y):
#return a dict of {state:action} pairs describing
#what can be reached from the (x, y) state, and how
    assert x <= X and y <= Y #(x, y) is glass levels; X and Y are glass sizes
    return {((0, y+x) if y+x<=Y else (x-(Y-y), y+(Y-y))):'X->Y',
            ((x+y, 0) if x+y<=X else (x+(X-x), y-(X-x))):'X<-Y',
            (X, y):'fill X', (x, Y):'fill Y',
            (0,y):'empty X', (x, 0):'empty y'}

print doctest.testmod() #TestResults(failed=0, attempted=9)