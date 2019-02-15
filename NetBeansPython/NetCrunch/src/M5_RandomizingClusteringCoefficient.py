#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="epasseto"
__date__ ="$27/09/2012 13:14:01$"

#
# Modify `expected_c`
# to return the expected value of C[w,x],
# where C[w,x] is the clustering coefficient
# given w and x - two randomly choosen neighbors of v
#
#Clustering coefficient
import random
import time
seed = time.time()
print seed
random.seed(seed)

def expected_C(G,v):
    # G[v].keys() is the set of neighbors of v
    neighbors = G[v].keys()
    degree = len(neighbors)
    # x in G[w][x] if x and w are connected in the graph (C[w,x])
    return # YOUR ANSWER HERE: expected value of C[w,x]

def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G

flights = [(1,2),(1,3),(2,3),(2,6),(2,4),(2,5),(3,6),(4,5)]
G = {}
for (x,y) in flights: make_link(G,x,y)

def clustering_coefficient(G,v):
    neighbors = G[v].keys()
    if len(neighbors) == 1: return 0.0
    links = 0.0
    for w in neighbors:
        for u in neighbors:
            if u in G[w]: links += 0.5
    return 2.0*links/(len(neighbors)*(len(neighbors)-1))

v = 2
print "CC:", clustering_coefficient(G,v)

vindex = {}
d = 0
for w in G[v].keys():
    vindex[d] = w
    d += 1

total = 0
for i in range(1,1000):
    if d > 1:
        pick = random.randint(0,d-1)
        v1 = vindex[pick]
        v2 = vindex[(pick+random.randint(1,d-1))%d]
        if v2 in G[v]: total += 1
    print i, (total+0.0)/i


for v in [1,2,3,4,5,6]:
    print v
    print expected_C(G,v)
    print clustering_coefficient(G,v) #converges to clustering coefficient
