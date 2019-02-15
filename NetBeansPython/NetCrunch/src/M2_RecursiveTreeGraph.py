#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.
#makes a messy recursive tree graph
__author__="epasseto"
__date__ ="$24/08/2012 08:33:14$"

def makeG(n):
        if n == 1:
            G1 = makeG(n/2)
            G2 = makeG(n/2)
            i1 = random node from G1
            i2 = random node from G2
            Make_link (G, i1, i2)

def make_link(G, node1, node2):
        if node1 not in G:
            G[node1] = {}
        (G[node1])[node2] = 1
        if node2 not in G:
            G[node2] = {}
        (G[node2])[node1] = 1
        return G