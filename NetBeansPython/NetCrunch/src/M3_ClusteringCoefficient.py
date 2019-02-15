#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="epasseto"
__date__ ="$03/09/2012 08:20:20$"


#
# Modify `expected_c`
# to return the expected value of C[w,x],
# where C[w,x] is the clustering coefficient
# given w and x - two randomly choosen neighbors of v
#

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

flights = [ ("ORD", "SEA"), ("ORD", "LAX"), ("ORD", "DFW"), ("ORD", "PIT"),
            ("SEA", "LAX"), ("LAX", "DFW"), ("DFW", "ATL"), ("ATL", "PIT"),
            ("ATL", "RDU"), ("RDU", "PHL"), ("PHL", "PIT"), ("PHL", "PVD")]

G={} #create graph
for (x,y) in flights: make_link(G,x,y)

def clustering_coefficient(G,v):
    neighbors = G[v].keys()
    if len(neighbors) == 1: return 0.0 #hard to compute, then return 0
    links = 0
    for w in neighbors:
        for u in neighbors: #neighbors again!
            if u in G[w]: links += 0.5 #gives the half (need revision of algorithm)
        print neighbors, links
        return 2.0*links/(len(neighbors)*(len(neighbors)-1))

print clustering_coefficient(G, "ORD")

total = 0
for v in G.keys():
    total += clustering_coefficient(G,v) #compute total coefficient
#       print V, clustering_coeffcient(G,V)

print total/len(G)

'''flights = [(1,2),(1,3),(2,3),(2,6),(2,4),(2,5),(3,6),(4,5)]
G = {}
for (x,y) in flights: make_link(G,x,y)

for v in [1,2,3,4,5,6]:
    print v
    print expected_C(G,v)
    print clustering_coefficient(G,v)'''
