#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="epasseto"
__date__ ="$02/10/2012 08:34:46$"

#
# Modify long_and_simple_path
# to build and return the path
#

# Find me that path!
def long_and_simple_path(G,u,v,l):
    if not long_and_simple_decision(G,u,v,l):
        return False
    #otherwise, build and return the path
    for node1 in G:
        neighbors = G[node1].keys()
        for node2 in neighbors:
            G = break_link(G, node1, node2) #break the link
            if not long_and_simple_decision(G,u,v,l):
                #need to keep that edge! - put that edge back into the graph! a graph search
                G = make_link(G, node1, node2) #exactly the simple path!
    path = [u]
    node = u
    next = (G[node].keys())[0] #next point in chain
    while (next != v):
        path.append(next)
        nextnext0 = (G[next].keys())[0] #one of the neighbors
        nextnext1 = (G[next].keys())[1] #the other one
        if nextnext0 == node: (node,next) = (next,nextnext1)
        else: (node,next) = (next,nextnext0)
    return path + [v]


"""
    G: Graph
    u: starting node
    v: ending node
    l: minimum length of path
"""
#############

def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G

def break_link(G, node1, node2):
    if node1 not in G:
        print "error: breaking link in a non-existent node"
        return
    if node2 not in G:
        print "error: breaking link in a non-existent node"
        return
    if node2 not in G[node1]:
        print "error: breaking non-existent link"
        return
    if node1 not in G[node2]:
        print "error: breaking non-existent link"
        return
    del G[node1][node2]
    del G[node2][node1]
    return G

flights = [(1,2),(1,3),(2,3),(2,6),(2,4),(2,5),(3,6),(4,5)]
G = {}
for (x,y) in flights: make_link(G,x,y)

def all_perms(seq):
    if len(seq) == 0: return [[]]
    if len(seq) == 1: return [seq, []]
    most = all_perms(seq[1:])
    first = seq[0]
    rest = []
    for perm in most:
        for i in range(len(perm)+1):
            rest.append(perm[0:i] + [first] + perm[i:])
    return most + rest

def check_path(G,path):
    for i in range(len(path)-1):
        if path[i+1] not in G[path[i]]: return False
    return True

def long_and_simple_decision(G,u,v,l):
    if l == 0:
        return False
    n = len(G)
    perms = all_perms(G.keys())
    for perm in perms:
        # check path
        if (len(perm) >= l and check_path(G,perm) and perm[0] == u
            and perm[len(perm)-1] == v):
            return True
    return False

#is there a long and simple path with 4 or more nodes from node 1 to node 5?
print long_and_simple_decision(G,1,5,4)
print long_and_simple_path(G,1,5,4)
