#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="epasseto"
__date__ ="$03/09/2012 08:46:05$"

#the edge maker
def make_link(G, node1, node2):
        if node1 not in G:
            G[node1] = {}
        (G[node1])[node2] = 1
        if node2 not in G:
            G[node2] = {}
        (G[node2])[node1] = 1
        return G

connections = [('a', 'g'), ('a', 'd'), ('d', 'g'), ('g', 'c'), ('b', 'f'), ('f', 'e'), ('e', 'h')]

G = {}
for (x,y) in connections: make_link(G,x,y)

#transversal
#chall this routine on nodes being visited for the first time
def mark_component(G, node, marked):
    marked[node] = True #executed only 1 time
    total_marked = 1
    for neighbor in G[node]:
#       print "=>", neighbor, "(",node,")"
        if neighbor not in marked:
            total_marked += mark_component(G, neighbor, marked) #recursively
    return total_marked

def list_component_sizes(G):
    marked = {}
    for node in G.keys():
        if node not in marked: #identified components
            print "Component containing", node, ": ", mark_component(G, node, marked)

list_component_sizes(G)
