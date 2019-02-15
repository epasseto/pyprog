#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="epasseto"
__date__ ="$28/01/2013 14:33:44$"

'''function tree_search(problem): #false code - a family of functions!
    forntier = {[Initial]}
    loop:
        if frontier is empty: return FAIL
        path = remove_choice(frontier) #this is de difference for each one
        s = path.end
        if s is a goal: return path
        for a in actions:
            add [path+a -> result(s,a)] to frontier

breadth-first search = shortest search first
?? = choice search first
BFS + termination clause (specific BFS)
depth-first search = longest path first - DFS have no completness (no garantee)
best estimate into the frontier (STOP)
'''

'''function graph_search(problem): #false code
    forntier = {[Initial]}
    explored = {} #new line
    loop:
        if frontier is empty: return FAIL
        path = remove_choice(frontier)
        s = path.end
        add s to explored #new line
        if s is a goal: return path
        for a in actions:
            add [path+a -> result(s,a)] to frontier unless result(s,a) in frontier + explored

uniform-cost search = cheapest-first (drop-off worse paths) (like topologicals)
Greedy best-first search = UCS+a estimate of distance/route to goal!
A* = total cost combined GBFS + UCS (better) -> path cost + estimated distance to goal (with a good heuristic function h-optimistic for tree-search)'''


