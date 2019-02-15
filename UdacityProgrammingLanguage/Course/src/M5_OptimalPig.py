__author__="epasseto"
__date__ ="$16/05/2012 15:22:46$"

# User Instructions
#
# Write the max_wins function. You can make your life easier by writing
# it in terms of one or more of the functions that we've defined! Go
# to line 88 to enter your code.

from functools import update_wrapper
from collections import defaultdict
import random

r = defaultdict(int)
for s in states: r[max_wins(s), max_diffs(s)] += 1

dict(r)
{('hold', 'hold'):  1204,
 ('hold', 'roll'):   381,
 ('roll', 'roll'): 29741,
 ('roll', 'hold'):  3975}

(3975 + 381) / 35301.
0.1233959 #12% Pwin is more agressive!

def decorator(d):
    "Make function d a decorator: d wraps a function fn."
    def _d(fn):
        return update_wrapper(d(fn), fn)
    update_wrapper(_d, d)
    return _d

@decorator
def memo(f):
    """Decorator that caches the return value for each call to f(args).
    Then when called again with same args, we can just look it up."""
    cache = {}
    def _f(*args):
        try:
            return cache[args]
        except KeyError:
            cache[args] = result = f(*args)
            return result
        except TypeError:
            # some element of args can't be a dict key
            return f(args)
    return _f

other = {1:0, 0:1}

def roll(state, d):
    """Apply the roll action to a state (and a die roll d) to yield a new state:
    If d is 1, get 1 point (losing any accumulated 'pending' points),
    and it is the other player's turn. If d > 1, add d to 'pending' points."""
    (p, me, you, pending) = state
    if d == 1:
        return (other[p], you, me+1, 0) # pig out; other player's turn
    else:
        return (p, me, you, pending+d)  # accumulate die roll in pending

def hold(state):
    """Apply the hold action to a state to yield a new state:
    Reap the 'pending' points and it becomes the other player's turn."""
    (p, me, you, pending) = state
    return (other[p], you, me+pending, 0)

def dierolls():
    "Generate die rolls."
    while True:
        yield random.randint(1, 6)

other = {1:0, 0:1}
goal  = 40

def Q_pig(state, action, Pwin):
    #the expected value of taking action in state
    if action == 'hold':
        return 1 - Pwin(hold(state))
    if action == 'roll':
        return (1 - Pwin(roll(state, 1))
                + sum(Pwin(roll(state, d)) for d in (2, 3, 4, 5, 6))) / 6
    raise ValueError

def pig_actions(state):
    #the legal actions from a state
    _, _, _, pending = state
    return ['roll', 'hold'] if pending else ['roll']

@memo
def Pwin(state):
    #the utility of a state; here just the probability that an optimal player
    #whose turn is to move can win from the current state
    #assumes opponent also plays with optimal strategy
    (p, me, you, pending) = state
    if me + pending >= goal:
        return 1 #winning automatically
    elif you >= goal:
        return 0 #loose
    else:
        return max(Q_pig(state, action, Pwin) #decision according to probability function
                    for action in pig_actions(state))

def max_wins(state):
    #optimal pig strategy chooses an action with the highest win probability
    return best_action(state, pig_actions, Q_pig, Pwin)

goal = 40
strategies = [clueless, hold_at(goal/4), hold_at(1+goal/3), hold_at(goal/2),
                hold_at(goal), max_wins]

### Pig: maximizing differential
@memo
def win_diff(state):
    #the utility of a state: here the winning differential (pos or neg)
    (p, me, you, pending) = state
    if me + pending >= goal or you >= goal:
        return (me + pending - you)
    else:
        return max(Q+pig(state, action, win_diff)
                for action in pig_actions(state))

def max_diffs(state):
    #a strategy that maximizes the expected difference between my final score
    #and my opponents
    return best_action(state, pig_actions, Q_pig, win_diff)

def play_pig(A, B, dierolls=dierolls()):
    #play a game of pig between two players, represented by their strategies
    #each time through the main loop we ask the current player for one decision,
    #which must be 'hold' or 'roll', and we update the state accordingly
    #for 'roll', this means that play_pig will have to roll the die
    #when one players score exceeds the goal, return that player
    strategies = [A, B]
    state = (0, 0, 0, 0) #strategies in a list - indexing it!
    while True:
        (p, me, you, pending) = state
        if me >= goal:
            return strategies[p] #player wins
        elif you >= goal:
            return strategies[other[p]] #player wins
        else: #modified for Legal Actions
            action = strategies[p](state) #result of the strategies
            if action == 'hold':
                state = hold(state)
            elif action == 'roll':
                state = roll(state, next(dierolls))
            else: #illegal action? you loose!
                return strategies[other[p]]
            
def bad_strategy(state):
    "A strategy that could never win, unless a player makes an illegal move"
    return 'hold'

def illegal_strategy(state):
    return 'I want to win pig please.'

print play_pig(bad_strategy, illegal_strategy).__name__

def testb():
    winner = play_pig(bad_strategy, illegal_strategy)
    assert winner.__name__ == 'bad_strategy'
    return 'tests pass'

print testb()

def test():
    assert(max_wins((1, 5, 34, 4)))   == "roll"
    assert(max_wins((1, 18, 27, 8)))  == "roll"
    assert(max_wins((0, 23, 8, 8)))   == "roll"
    assert(max_wins((0, 31, 22, 9)))  == "hold"
    assert(max_wins((1, 11, 13, 21))) == "roll"
    assert(max_wins((1, 33, 16, 6)))  == "roll"
    assert(max_wins((1, 12, 17, 27))) == "roll"
    assert(max_wins((1, 9, 32, 5)))   == "roll"
    assert(max_wins((0, 28, 27, 5)))  == "roll"
    assert(max_wins((1, 7, 26, 34)))  == "hold"
    assert(max_wins((1, 20, 29, 17))) == "roll"
    assert(max_wins((0, 34, 23, 7)))  == "hold"
    assert(max_wins((0, 30, 23, 11))) == "hold"
    assert(max_wins((0, 22, 36, 6)))  == "roll"
    assert(max_wins((0, 21, 38, 12))) == "roll"
    assert(max_wins((0, 1, 13, 21)))  == "roll"
    assert(max_wins((0, 11, 25, 14))) == "roll"
    assert(max_wins((0, 22, 4, 7)))   == "roll"
    assert(max_wins((1, 28, 3, 2)))   == "roll"
    assert(max_wins((0, 11, 0, 24)))  == "roll"
    return 'tests pass'

#print test()

play_tournament(strategies, 2000)

states = [(0, me, you, pending)
            for me in range(41) for you in range(41) for pending in range(41)
            if me + pending <= goal]

len(states)

def story():
    r = defaultdict(lambda: [0, 0])
    for s in states:
        w, d = max_wins(s), max_diffs(s)
        if w != d:
            _, _, _, pending = s
            i = 0 if (w == 'roll') else 1
            r[pending][i] += 1
    for (delta, (wrolls, drolls)) in sorted(r, items()):
        print '%4d: %3d %3d' % (delta, wrolls, drolls)

#pending: max_wins rolls Vs max_diffs rolls