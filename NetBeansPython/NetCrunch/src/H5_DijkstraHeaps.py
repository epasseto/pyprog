#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="epasseto"
__date__ ="$02/10/2012 08:35:52$"

#
# The code below uses a linear
# scan to find the unfinished node
# with the smallest distance from
# the source.
#
# Modify it to use a heap instead
#

# write up_heapify, an algorithm that checks if
# node i and its parent satisfy the heap
# property, swapping and recursing if they don't
#
# L should be a heap when up_heapify is done
#

def up_heapify(L, i):
    while True:
        p = parent(i)
        if p == -1: return L #i was in the parent node
        valueChild  = L[i]
        valueParent = L[p]
        if valueParent > valueChild:
            L[p] = valueChild
            L[i] = valueParent
        i = p
    return None

def parent(i):
    return (i-1)/2
def left_child(i):
    return 2*i+1
def right_child(i):
    return 2*i+2
def is_leaf(L,i):
    return (left_child(i) >= len(L)) and (right_child(i) >= len(L))
def one_child(L,i):
    return (left_child(i) < len(L)) and (right_child(i) >= len(L))

#L = [2, 4, 3, 5, 9, 7, 7, 1]
#print parent (0)
#print left_child(3)
#print right_child(0)
#print is_leaf(L,7)
#print one_child (L,3)
#print up_heapify(L,7)

def test():
    L = [2, 4, 3, 5, 9, 7, 7]
    L.append(1)
    up_heapify(L, 7)
    assert 1 == L[0]
    assert 2 == L[1]


def shortest_dist_node(dist):
    best_node = 'undefined'
    best_value = 1000000
    for v in dist:
        if dist[v] < best_value:
            (best_node, best_value) = (v, dist[v])
    return best_node


def dijkstra(G,v): #v is the start point!
    return none

def old_dijkstra(G,v):
    dist_so_far = {}
    dist_so_far[v] = 0
    final_dist = {}
    while len(final_dist) < len(G):
        w = shortest_dist_node(dist_so_far)
        # lock it down!
        final_dist[w] = dist_so_far[w]
        del dist_so_far[w]
        for x in G[w]:
            if x not in final_dist:
                if x not in dist_so_far:
                    dist_so_far[x] = final_dist[w] + G[w][x]
                elif final_dist[w] + G[w][x] < dist_so_far[x]:
                    dist_so_far[x] = final_dist[w] + G[w][x]
    return final_dist

############
#
# Test

def make_link(G, node1, node2, w):
    if node1 not in G:
        G[node1] = {}
    if node2 not in G[node1]:
        (G[node1])[node2] = 0
    (G[node1])[node2] += w
    if node2 not in G:
        G[node2] = {}
    if node1 not in G[node2]:
        (G[node2])[node1] = 0
    (G[node2])[node1] += w
    return G

def test():
    # shortcuts
    (a,b,c,d,e,f,g) = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
    triples = ((a,c,3),(c,b,10),(a,b,15),(d,b,9),(a,d,4),(d,f,7),(d,e,3),
               (e,g,1),(e,f,5),(f,g,2),(b,f,1))
    G = {}
    for (i,j,k) in triples:
        make_link(G, i, j, k)
    return G

print test()
#print len(G)
G = {'A': {'C': 3, 'B': 15, 'D': 4}, 'C': {'A': 3, 'B': 10}, 'B': {'A': 15, 'C': 10, 'D': 9, 'F': 1}, 'E': {'D': 3, 'G': 1, 'F': 5}, 'D': {'A': 4, 'B': 9, 'E': 3, 'F': 7}, 'G': {'E': 1, 'F': 2}, 'F': {'B': 1, 'E': 5, 'D': 7, 'G': 2}}
    #dist = dijkstra(G, a)
    #assert dist[g] == 8 #(a -> d -> e -> g)
    #assert dist[b] == 11 #(a -> d -> e -> g -> f -> b)
