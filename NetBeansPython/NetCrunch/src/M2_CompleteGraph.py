#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="epasseto"
__date__ ="$22/08/2012 12:37:19$"
#how many edges in a complete graph of n nodes?

def make_link(G, node1, node2):
        if node1 not in G:
            G[node1] = {}
        (G[node1])[node2] = 1
        if node2 not in G:
            G[node2] = {}
        (G[node2])[node1] = 1
        return G

#make an empty graph
G = {}

def clique(n):
    G = {}
    #add in the edges
    for i in range(n):
        for j in range(n):
            if i<j: make_link(G, i, j)
    #print G
    return sum([len(G[node]) for node in G.keys()])/2 #keys as it is a dictionnary!

for n in range(1,10):
    print n, clique(n), n*(n-1)/2

def oldclique(n):
    #return the number of edges
    #try to use a mathematical formula
    return (n**2-n)/2
