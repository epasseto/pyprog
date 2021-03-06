#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="epasseto"
__date__ ="$14/05/2012 09:25:07$"

# In this problem, you will solve the pouring problem for an arbitrary
# number of glasses. Write a function, more_pour_problem, that takes
# as input capacities, goal, and (optionally) start. This function should
# return a path of states and actions.
#
# Capacities is a tuple of numbers, where each number represents the
# volume of a glass.
#
# Goal is the desired volume and start is a tuple of the starting levels
# in each glass. Start defaults to None (all glasses empty).
#
# The returned path should look like [state, action, state, action, ... ]
# where state is a tuple of volumes and action is one of ('fill', i),
# ('empty', i), ('pour', i, j) where i and j are indices indicating the
# glass number.



def more_pour_problem(capacities, goal, start=None):
    """The first argument is a tuple of capacities (numbers) of glasses; the
    goal is a number which we must achieve in some glass.  start is a tuple
    of starting levels for each glass; if None, that means 0 for all.
    Start at start state and follow successors until we reach the goal.
    Keep track of frontier and previously explored; fail when no frontier.
    On success return a path: a [state, action, state2, ...] list, where an
    action is one of ('fill', i), ('empty', i), ('pour', i, j), where
    i and j are indices indicating the glass number."""

    def is_goal(state): return goal in state

    def more_pour_successors(state):
        #all the {state:action} pairs we reach from any pouring action
        indices = range(len(state))
        succ = {} #dictionnary of results state:action pairs
        for i in indices:
            succ[replace(state, i, capacities[i])] = ('fill', i) #tupples are immutable
            succ[replace(state, i, 0)] = ('empty', i)
            for j in indices:
                if i != j: #not pouring from itself!
                    amount = min(state[i], capacities[j] - state[j])
                    state2 = replace(state, i, state[i] - amount)
                    suu[replace(state2, j, state[j] + amount)] = ('pour', i, j)
        return succ

    if start is None: start = (0,) * len(capacities)
    return shortest_path_search(start, more_pour_successors, is_goal) #hardest of the function

def replace(sequence, i, val):
    #return copy of sequence, with sequence[i] replaced by val
    s = list(sequence)
    s[i] = val #mutate list
    return type(sequence)(s) #tell type and call that!

def shortest_path_search(start, successors, is_goal):
    """Find the shortest path from start state to a state
    such that is_goal(state) is true."""
    if is_goal(start):
        return [start]
    explored = set()
    frontier = [ [start] ]
    while frontier:
        path = frontier.pop(0)
        s = path[-1]
        for (state, action) in successors(s).items():
            if state not in explored:
                explored.add(state)
                path2 = path + [action, state]
                if is_goal(state):
                    return path2
                else:
                    frontier.append(path2)
    return Fail

Fail = []

def test_more_pour():
    assert more_pour_problem((1, 2, 4, 8), 5) == [
        (0, 0, 0, 0), ('fill', 3), (0, 0, 0, 8), ('pour', 3, 0), (1, 0, 0, 7),
        ('pour', 3, 1), (1, 2, 0, 5)]
    starbucks = (8, 12, 16, 20, 24)
    assert not any(more_pour_problem(starbucks, odd) for odd in (3, 5, 7, 9))
    assert all(more_pour_problem((1, 3, 9, 27), n) for n in range(28))
    assert more_pour_problem((1, 3, 9, 27), 28)
    return 'test_more_pour passes'

print test_more_pour()
