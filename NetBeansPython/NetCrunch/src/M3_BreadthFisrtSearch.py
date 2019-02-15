#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="epasseto"
__date__ ="$06/09/2012 09:27:02$"

import csv
import time

def make_link(G, node1, node2):
        if node1 not in G:
            G[node1] = {}
        (G[node1])[node2] = 1
        if node2 not in G:
            G[node2] = {}
        (G[node2])[node1] = 1
        return G

def read_graph(filename):
    # reads an undirected graph in CSV format - each line is an edge!
    tsv = csv.reader(open(filename), delimiter='\t')
    G = {}
    for (node1, node2) in tsv: make_link(G, node1, node2)
    return G

#read the marvel comics graph
marvelG = read_graph("uniq_edges.tsv")

def path(G, v1, v2): #beadth first search - tells only the link of shortest path!
    distance_from_start = {} #better - produce the path itself
    open_list = [v1]
    #distance_from_start[v1] = 0
    distance_from_start[v1] = [v1] #to return the path, not the distance!
    path_from_start[v1] = [v1]
    while len(open_list) > 0:
        current = open_list[0]
        del open_list[0] #delete the first element of the open list
        for neighbor in G[current].keys():
            if neighbor not in distance_from_start: #not visited!
                #distance_from_start[neighbor] = distance_from_start[current] + 1 #expand search distance
                distance_from_start[neighbor] = distance_from_start[current] + [neighbor]
                if neighbor == 2: return distance_from_start[v2] #node found!
                open_list.append(neighbor)
    return False

from_node = "A"
to_node = "ZZZAX"

