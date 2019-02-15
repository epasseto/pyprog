#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="epasseto"
__date__ ="$11/09/2012 11:06:19$"

# Non-recursive Depth First Search
# Implement mark_component using the open list as discussed in lecture.
# mark_component should not use recursion.

G={1: {2: 1}, 2: {1: 1, 3: 1}, 3: {2: 1}, 4: {5: 1}, 5: {4: 1, 6: 1}, 6: {5: 1}}
marked={}

def mark_component(G, node, marked): #recursive solution
    #marked[node] = True
    total_marked = 0
    openlist = []
    openlist.append(node)
    while len(openlist) > 0:
        print "openlist:", openlist
        tomark = openlist.pop()
        if tomark not in marked:
            marked[tomark] = True
            total_marked += 1
            tovisit = G[tomark]
            print tomark, tovisit, "G:", G
            for entries in tovisit:
                openlist.append(entries)
    print marked
    return total_marked

print mark_component(G, 1, marked)

def old_mark_component(G, node, marked): #recursive solution
    marked[node] = True
    total_marked = 1
    print "node:",node,"G:",G[node]
    for neighbor in G[node]:
        if neighbor not in marked:
            total_marked += old_mark_component(G, neighbor, marked)
    print marked
    return total_marked

#print old_mark_component(G, 1, marked)

#########
# Code for testing
#
def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G

def test():
    test_edges = [(1, 2), (2, 3), (4, 5), (5, 6)]
    G = {}
    for n1, n2 in test_edges:
        make_link(G, n1, n2)
    print G
    marked = {}
    assert mark_component(G, 1, marked) == 3
    assert 1 in marked
    assert 2 in marked
    assert 3 in marked
    assert 4 not in marked
    assert 5 not in marked
    assert 6 not in marked

#print test()

print mark_component(G, 1, marked)