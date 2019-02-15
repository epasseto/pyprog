#! /usr/bin/python

def mc_problem2(start=(3, 3, 1, 0, 0, 0), goal=None):
    #solve the missionaries and cannibals problem
    #state is 6 ints: (M1, C1, B1, M2, C2, B2) on the start(1) and other (2) sides
    #find a path that goes from the initial state to the goal state
    # (which, if not specified, is the state with no people or boats on the start side
    if goal is None:
        goal = (0, 0, 0) + start[:3]
    return shortest_path_search(start, csuccessors, all_gone)

def all_gone(state): return state[:3] == (0, 0, 0)

def shortest_path_search(start, successors, is_goal):
    """Find the shortest path from start state to a state
    such that is_goal(state) is true."""
    if is_goal(start):
        return [start]
    explored = set() #set of states we have visited
    frontier = [[start]] #ordered list of pahts we have blazed
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

def mc_problem1(start=(3, 3, 1, 0, 0, 0), goal=None):
    """Solve the missionaries and cannibals problem.
    State is 6 ints: (M1, C1, B1, M2, C2, B2) on the start (1) and other (2) sides.
    Find a path that goes from the initial state to the goal state (which, if
    not specified, is the state with no people or boats on the start side."""
    if goal is None:
        goal = (0, 0, 0) + start[:3]
    if start == goal:
        return [start]
    explored = set() # set of states we have visited
    frontier = [ [start] ] # ordered list of paths we have blazed
    while frontier:
        path = frontier.pop(0)
        s = path[-1]
        for (state, action) in csuccessors(s).items():
            if state not in explored:
                explored.add(state)
                path2 = path + [action, state]
                if state == goal:
                    return path2
                else:
                    frontier.append(path2)
    return Fail

Fail = []

def csuccessors(state):
    """Find successors (including those that result in dining) to this
    state. But a state where the cannibals can dine has no successors."""
    M1, C1, B1, M2, C2, B2 = state
    if C1 > M1 > 0 or C2 > M2 > 0:
        return {}
    items = []
    if B1 > 0:
        items += [(sub(state, delta), a + '->')
                    for delta, a in deltas.items()]
    if B2 > 0:
        items += [(add(state, delta), '<-' + a)
                    for delta, a in deltas.items()]
    return dict(items)

deltas = {(2, 0, 1,   -2,  0, -1):'MM', #differences in spaces
          (0, 2, 1,    0, -2, -1):'CC', #corresponding to these moves
          (1, 1, 1,   -1, -1, -1):'MC',
          (1, 0, 1,   -1,  0, -1):'M',
          (0, 1, 1,    0, -1, -1):'C'}

def add(X, Y):
    #add two vectors, X and Y
    return tuple(x+y for x,y in zip(X, Y))

def sub(X, Y):
    #subtract vector Y from X
    return tuple(x-y for x,y in zip(X, Y))

def test():
    assert csuccessors((2, 2, 1, 0, 0, 0)) == {(2, 1, 0, 0, 1, 1): 'C->',
                                               (1, 2, 0, 1, 0, 1): 'M->',
                                               (0, 2, 0, 2, 0, 1): 'MM->',
                                               (1, 1, 0, 1, 1, 1): 'MC->',
                                               (2, 0, 0, 0, 2, 1): 'CC->'}
    assert csuccessors((1, 1, 0, 4, 3, 1)) == {(1, 2, 1, 4, 2, 0): '<-C',
                                               (2, 1, 1, 3, 3, 0): '<-M',
                                               (3, 1, 1, 2, 3, 0): '<-MM',
                                               (1, 3, 1, 4, 1, 0): '<-CC',
                                               (2, 2, 1, 3, 2, 0): '<-MC'}
    assert csuccessors((1, 4, 1, 2, 2, 0)) == {}
    return 'tests pass'

print test()


