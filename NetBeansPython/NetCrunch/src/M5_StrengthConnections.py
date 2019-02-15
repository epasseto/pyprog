#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="epasseto"
__date__ ="$19/09/2012 14:42:01$"

import csv

def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G

def read_graph(filename):
    # Read an undirected graph in CSV format. Each line is an edge
    tsv = csv.reader(open(filename), delimiter='\t')
    G = {}
    for (node1, node2) in tsv: make_link(G, node1, node2)
    return G

# Read the marvel comics graph
# Read the marvel comics graph
marvelG = read_graph('c://Marveltest.tsv')
print marvelG

# distance from start (original)
def distance(G, v1, v2):
    distance_from_start = {}
    open_list = [v1]
    distance_from_start[v1] = 0
    while len(open_list) > 0:
        current = open_list[0]
        del open_list[0]
        for neighbor in G[current].keys():
            if neighbor not in distance_from_start:
                distance_from_start[neighbor] = distance_from_start[current] + 1
                if neighbor == v2: return distance_from_start[v2]
                open_list.append(neighbor)
    return False

'''
# path from start (after modification on distance())
def path(G, v1, v2):
    #distance_from_start = {}
    path_from_start = {} # modification
    open_list = [v1]
    #distance_from_start[v1] = 0
    path_from_start[v1] = [v1] # modification
    while len(open_list) > 0:
        current = open_list[0]
        del open_list[0]
        for neighbor in G[current].keys():
            #if neighbor not in distance_from_start:
            if neighbor not in path_from_start: # modification
                #distance_from_start[neighbor] = distance_from_start[current] + 1
                path_from_start[neighbor] = path_from_start[current + [neighbor] # modification
                #if neighbor == v2: return distance_from_start[v2]
                if neighbor == v2: return path_from_start[v2] # modification
                open_list.append(neighbor)
    return False

from_node = "A"
to_node = "ZZZAX"

print distance(marvelG, from_node, to_node)
print path(marvelG, from_node, to_node)

#let´s make a character-to-character graph
#note that if an edge is added multiple times, the strength increases
time1 = time.time()
charG = {} #heap code from the last unit
for char1 in characters:
    for book in marvelG[ghar1]:
        for char2 in marvelG[book]: #loop all different characters
            make_link(charG, char1, char2) #no make link a twice!
time2 = time.time()
print "time to compute strengths: ", time2-time1

Be aware that this code double counts the values. Students suggested the following fix:
for char1 in characters:
    for book in marvelG[char1]:
        for char2 in marvelG[book]:
            if char1 > char 2:
                 make_link(charG, char1, char2)

#get highest k strengths
time1 = time.time()
k = 10
heap = []
for char1 in characters:
    for char2 in charG[char1]:
        #avoid duplicates by only including pairs where the character number of the first is less than that of the second
        if characters[char1] < characters[char2]:
            if len(heap) < k:
                insert_heap(heap, (charG[char1][char2],(char1,char2)))
            elif charG[char1][char2] > val(cheap[0]):
'''
