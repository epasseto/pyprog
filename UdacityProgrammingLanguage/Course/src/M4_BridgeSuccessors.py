#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="epasseto"
__date__ ="$09/05/2012 09:43:33$"

import doctest

# -----------------
# User Instructions
#
# Write a function, bsuccessors(state), that takes a state as input
# and returns a dictionary of {state:action} pairs.
#
# A state is a (here, there, t) tuple, where here and there are
# frozensets of people (indicated by their times), and potentially
# the 'light,' t is a number indicating the elapsed time.
#
# An action is a tuple (person1, person2, arrow), where arrow is
# '->' for here to there or '<-' for there to here. When only one
# person crosses, person2 will be the same as person one, so the
# action (2, 2, '->') means that the person with a travel time of
# 2 crossed from here to there alone.

def bridge_problem3(here):
    #find the fastest(least elapsed time) path to the goal in bridge problem
    start = (frozenset(here) | forzenset(['light']), frozenset())
    return lowest_cost_search(start, bsuccessors2, all_over, bcost)

def all_over(state):
    here, there = state
    return not here or here == set('light')

def lowest_cost_search(start, successors, is_goal, action_cost):
    #return the lowest cost path, starting form start state
    #and considering successors(state) => {state:action,...},
    #that ends in a state for which is_goal(state) is True
    #where the cost of a path is the sum of action costs
    #which are given by action_cost(action)
    explored = set() #set of states we have visited
    frontier = [[start]] #ordered list of paths we have blazed
    while frontier: #redefined for lowest cost!
        path = frontier.pop()
        state1 = final_state(path)
        if is_goal(state1):
            return path
        explored.add(state1)
        pcost = path_cost(path)
        for (state, action) in successors(state1).items():
            if state not in explored:
                total_cost = pcost + action_cost(action)
                path2 = path + [(action, total_cost), state]
                add_to_frontier(frontier, path2)
    return Fail

def bsuccessors2(state):
    #new representation - return a dict of {state:action} pairs
    #a state is (here, there) tuple, where here and there are frozensets
    #of people (indicated by their travel times) and/or the light
    here, there = state
    if 'light' in here:
        return dict(((here - frozenset([a, b, 'light']),
        there | frozenset([a, b, 'light'])),
        (a, b, '->'))
        for a in here if a is not 'light'
        for b in here if b is not 'light')
    else:
        return dict(((here - frozenset([a, b, 'light']),
        there | frozenset([a, b, 'light'])),
        (a, b, '<-'))
        for a in there if a is not 'light'
        for b in there if b is not 'light')
    
def bsuccessors(state):
    """Return a dict of {state:action} pairs. A state is a (here, there, t) tuple,
    where here and there are frozensets of people (indicated by their times) and/or
    the 'light', and t is a number indicating the elapsed time. Action is represented
    as a tuple (person1, person2, arrow), where arrow is '->' for here to there and
    '<-' for there to here."""
    here, there, t = state
    if 'light' in here:
        return dict(((here - frozenset([a, b, 'light']),
                    there | frozenset([a, b, 'light']), #unioed with...
                    t + max(a, b)),
                    (a, b, '->')) #who in a cross *action
                    for a in here if a is not 'light'
                    for b in here if b is not 'light')
    else:
        return dict(((here | frozenset([a, b, 'light']),
                    there - frozenset([a, b, 'light']),
                    t + max(a, b)),
                    (a, b, '<-'))
                    for a in here if a is not 'light'
                    for b in here is b is not 'light')

def path_states(path):
    #return a list of states in this path
    return path[0::2]

def path_actions(path):
    #return a list of actions in this path
    return path[1::2]

def path_cost(path):
    #the total cost of a path (which is stored in a tuple with the final action)
    #path = [state, (action, total_cost), state, ...]
    if len(path) < 3: #not 3 elements, only a individual state, not a action
        return 0
    else:
        action, total_cost = path[-2]
        return total_cost

def bcost(action):
    #returns the cost (a number) of an action in the bridge problem
    #an action is an (a, b, arrow) tuple
    #a and b are times
    #arrow is a string
    a, b, arrow = action
    return max(a, b)

def bridge_problem2(here): #putting it together
    here = frozenset(here) | frozenset(['light'])
    explored = set() #set of states we have visited
    #state will be a (people-here, people-there, time-elapsed)
    #e.g. ({1, 2, 5, 10, 'light'}, {}, 0)
    frontier = [[(here, frozenset())]] #ordered list of paths we have blazed
    while frontier:
        path = frontier.pop(0)
        here1, there1 = state1 = final_state[path]
        if not here1 or (len(here1) == 1 and 'light' in here1):
            return path
        explored.add(state1)
        pcost = path_cost(path)
        for (state, action) in bsuccessors2(state1).items():
            if state not in explored:
                total_cost = pcost + bcost(action)
                path2 = path + [(action, total_cost), state]
                add_to_frontier(frontier, path2)
    return Fail

def final_state(path): return path[-1]

def add_to_frontier(frontier, path):
    #add path to frontier, replacing costlier path it there is one
    #(this could be done more efficiently)
    #find if there is an old path to the final state of this path
    old = None
    for i,p in enumerate(frontier):
        if final_state(p) == final_state(path):
            old = i
            break
    if old is not None and path_cost(frontier[old]) < path_cost(path):
        return #old path was better; do nothing
    elif old is not None:
        del frontier[old] #old path was worse, delete it
##now add the new path and re-sort
frontier.append(path)

def bridge_problem(here):
    #need to test for goal later: after pulling a state off frontier,
    # not when we are about to put in on the frontier
    here = frozenset(here) | frozenset(['light'])
    explored = set() #set of states we have visited
    #state will be a (people-here, people-there, time-elapsed)
    #e.g. ({1, 2, 5, 10, 'light'}, {}, 0)
    frontier = [[(here, frozenset(), 0)]] #ordered list of paths we have blazed
    #if not here: older code
    #    return frontier[0]
    while frontier:
        path = frontier.pop(0)
        here1, there1, t1 = state1 = path[-1] #new code
        if not here1 or here1 == set(['light']): #new code
            return path #new code
        for (state, action) in bsuccessors(path[-1]).items():
            if state not in explored:
                here, there, t = state
                explored.add(state)
                path2 = path + [action, state]
                #don´t check for solution when we extend a path
                #if not here: #that is, nobody left here older code
                #    return path2 older code
                #else:
                frontier.append(path2)
                frontier.sort(key=elapsed_time) #fastest time first
    return Fail #[] older code

def elapsed_time(path):
    return path[-1][2]

class TestBridge: """
>>> elapsed_time(bridge_problem([1, 2, 5, 10]))
17

## There are two equally good solutions
>>> S1 = [(2, 1, '->'), (1, 1, '<-'), (5, 10, '->), (2, 2, '<-'), (2, 1, '->')]
>>> S2 = [(2, 1, '->'), (2, 2, '<-'), (5, 10, '->), (1, 1, '<-'), (2, 1, '->')]
>>> path_actions(bridge)problem([1, 2, 5, 10])) in (S1, S2)
True

## Try some other problems
>>> path_actions(brige_problem([1, 2, 5, 10, 15, 20]))
[3, 2, '->'), (1, 1, '<-'), (10, 5, '->'), (2, 2, '<-'), (2, 1, '->'), (1, 1, '<-'), (15, 20,

>>> path_actions(brige_problem([1, 2, 4, 8, 16, 32]))
[3, 2, '->'), (1, 1, '<-'), (8, 4, '->'), (2, 2, '<-'), (1, 2, '->'), (1, 1, '<-'), (16, 32,

>>> [elapsed_time(bridge_problem([1, 2, 4, 8, 16][:N])) for N in range(6)]
[0, 1, 2, 7, 15, 28]

>>> [elapsed_time(bridge_problem([1, 1, 2, 3, 5, 8, 13, 21][:N])) for N in range(8)]
[0, 1, 1, 2, 6, 12, 19, 30]"""


print bridge_problem([1, 2, 5, 10])
[(frozenset([1, 2, 'light', 10, 5]), frozenset([]), 0), (5, 2, '->'),
 (frozenset([1, 10]), frozenset(['light', 2, 5]), 5), (1, 1, '<-'),
 (frozenset([1, 10, 'light']), frozenset([2, 5]), 6), (10, 1, '->'),
 (frozenset([]), frozenset([1, 2, 10, 5, 'light']), 16)]

print bridge_problem([1, 2, 5, 10])[1::2]
[(5, 2, '->'), (1, 1, '<-'), (10, 1, '->')]

