#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="epasseto"
__date__ ="$14/05/2012 14:08:05$"

# States are represented as a tuple of (p, me, you, pending) where
# p:       an int, 0 or 1, indicating which player's turn it is.
# me:      an int, the player-to-move's current score
# you:     an int, the other player's current score.
# pending: an int, the number of points accumulated on current turn, not yet scored

from collections import namedtuppe
import random

possible_moves = ['roll', 'hold']

def clueless(state):
    #a strategy that ignores the state and chooses at random from possible moves
    return random.choice(possible_moves)

def old_hold(state):
    """Apply the hold action to a state to yield a new state:
    Reap the 'pending' points and it becomes the other player's turn."""
    (p, me, you, pending) = state
    return (other[p], you, me+pending, 0)

def hold(state):
    """Apply the hold action to a state to yield a new state:
    Reap the 'pending' points and it becomes the other player's turn."""
    return State(other[state.p], state.you, state.me+state.pending, 0) #explicitly creating a new state

def roll(state, d):
    """Apply the roll action to a state (and a die roll d) to yield a new state:
    If d is 1, get 1 point (losing any accumulated 'pending' points),
    and it is the other player's turn. If d > 1, add d to 'pending' points."""
    if d == 1:
        return State(other[state.p], state.you, state.me+1, 0) #pig out, one player´s turn
    else:
        return State(state.p, state.me, state.you, state.pending+d) #accumulate die roll in pending

def old_roll(state, d):
    """Apply the roll action to a state (and a die roll d) to yield a new state:
    If d is 1, get 1 point (losing any accumulated 'pending' points),
    and it is the other player's turn. If d > 1, add d to 'pending' points."""
    (p, me, you, pending) = state #tupple with 4 components
    if d == 1:
        return (other[p], you, me+1, 0) #pig out, one player´s turn
    else:
        return (p, me, you, pending+d) #accumulate die roll in pending

other = {1:0, 0:1} #mapping from player to other player

def hold_at(x):
    #return a strategy that holds if and only if pending => x
    #or player reaches goal
    def strategy(state):
        (p, me, you, pending) = state
        return 'hold' if (pending >=x or me + pending >= goal) else 'roll'
    strategy.__name__ = 'hold_at(%d' % x
    return strategy
## state = (p, me, you, pending)

def dierolls():
    #generate die rolls
    while True:
        yield random.randint(1, 6)

def play_pig(A, B):
    #play a game of pig between two players, represented by their strategies
    #each time through the main loop we ask the current player for one decision,
    #which must be 'hold' or 'roll', and we update the state accordingly
    #for 'roll', this means that play_pig will have to roll the die
    #when one player´s score exceeds the goal, return that player
    strategies = [A, B]
    state = (0, 0, 0, 0) #strategies in a list - indexing it!
    while True:
        (p, me, you, pending) = state
        if me >= goal:
            return strategies[p] #player wins
        elif you >= goal:
            return strategies[other[p]] #player wins
        elif strategies[p](state) == 'hold':
            state = hold(state) #make hold
        else:
            state = roll(state, next(dierolls)) #an iterator
            #state = roll(state, random.randint(1,6)) #old perform roll

goal = 50

def test():
    A, B = hold_at(50), clueless
    rolls = iter([6, 6, 6, 6, 6, 6, 2]) #shortest list that allows A to win
    assert play_pig(A, B, rolls) == A #rolls as a iterator

"""def test():
    assert hold_at(30)((1, 29, 15, 20)) == 'roll'
    assert hold_at(30)((1, 29, 15, 21)) == 'hold'
    assert hold_at(30)((0, 2, 30, 10))  == 'roll'
    assert hold_at(30)((0, 2, 30, 15))  == 'hold'
    return 'tests pass'

def test_actions():
    s = (0, 10, 20, 30)
    assert hold(s) == (1, 20, 40, 0)
    assert roll(s, 6) == (0, 10, 20, 36)
    assert roll(s, 1) == (1, 20, 11, 0)
    return 'test_actions pass'

def old_test():
    assert hold((1, 10, 20, 7))    == (0, 20, 17, 0)
    assert hold((0, 5, 15, 10))    == (1, 15, 15, 0)
    assert roll((1, 10, 20, 7), 1) == (0, 20, 11, 0)
    assert roll((0, 5, 15, 10), 5) == (0, 5, 15, 15)
    return 'tests pass'"""

print test()
