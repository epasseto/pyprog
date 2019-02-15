#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="epasseto"
__date__ ="$20/08/2012 11:17:34$"

#graphs as dictionnaries of dictionnaries
#I probably should have written a_ring = make_link(a_ring, i (i+1)%n)
#since make_link returns the graph. I think it works either way, though. -MLL
def make_link(G, node1, node2):
        if node1 not in G:
            G[node1] = {}
        (G[node1])[node2] = 1
        if node2 not in G:
            G[node2] = {}
        (G[node2])[node1] = 1
        return G

#make an empty graph (dictionnary)
a_ring = {}

n = 5

#add in the edges
for i in range(n):
    make_link(a_ring, i, (i+1)%n) #loop for i to i-1

#for many nodes?
print len(a_ring)

#how many edges?
print sum([len(a_ring[node]) for node in a_ring.keys()])/2
#         number of degrees of each node
print a_ring

#{0: {1: 1, 4: 1}, 1: {0: 1, 2: 1}, 2: {1: 1, 3: 1},
#3: {2: 1, 4: 1}, 4: {0: 1, 3: 1}}
#name of the node: {connected to: 1, connected to: 1} <-directly
