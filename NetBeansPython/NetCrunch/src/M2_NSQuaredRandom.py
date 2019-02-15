#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="epasseto"
__date__ ="$24/08/2012 17:10:48$"

def make_link(G, node1, node2):
        if node1 not in G:
            G[node1] = {}
        (G[node1])[node2] = 1
        if node2 not in G:
            G[node2] = {}
        (G[node2])[node1] = 1
        return G

def makeG(n): #random fake algorythm
        if n == 1: return
        G1 = makeG(n/2)
        G2 = makeG(n/2)
        S1 = random n/4 nodes from G1
        S2 = random n/4 nodes from G2
        for all i1 in S1 and i2 in S2: make_link(G, i1, i2)
        return G

def makeG(n): #random fake algorythm (tangled hypercube)
        if n == 1: return
        G1 = makeG(n/2)
        G2 = makeG(n/2)
        i1 = list of nodes of G1 in random order
        i2 = list of nodes of G2 in random order
        for i in range(n/2): make_link(G, i1, i2)
        return G