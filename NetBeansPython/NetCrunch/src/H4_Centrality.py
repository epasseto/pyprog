#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="epasseto"
__date__ ="$03/12/2012 16:44:10$"

import scipy
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
    for (node1, node2, node3) in tsv:
        make_link(G, node1, node2)
    print "done creating graph"
    return G

def dictio_actor(A, node1):
    if node1 in A: pass
    else: A[node1] = True
    return A

def read_actor(filename):
    # Read an undirected graph in CSV format. Each line is an edge
    tsv = csv.reader(open(filename), delimiter='\t')
    A = {}
    for (node1, node2, node3) in tsv:
        dictio_actor(A, node1)
    print "done creating autors"
    return A

#Importance: 01
#1-gets a guy; 2-open his nodes; 3-if pair not registered, add it; register all distances and return them
#INPUT : G-complete graph, A-actors dic, dictioCentral-all centralities from a node, dictioMinDist-minimal centrality of a pair of nodes
#OUTPUT: G-complete graph(no changes), dictioCentral(better), dictioMinDist(better)
def get_guy(G, guy):
    distance = 1
    open_list = [guy]
    visited = {}
    nextStep = []
    visited[guy] = True
    centraList = []
    alfa = []
    while True:
        while len(open_list) > 0:
            current = open_list.pop() #modified BFS
            alfa = alfa + G[current].keys()
            for neighbor in alfa:
                #print current, neighbor, visited, open_list
                if neighbor not in visited:
                    nextStep.append(neighbor)
                    visited[neighbor] = True
                    centraList.append(distance)
                    #print 'added', neighbor, open_list, nextStep, centraList
        distance += 1
        #print 'newdistance', distance, nextStep
        while len(nextStep) > 0: #transfers new step
            #print 'transfering', nextStep, open_list
            a = nextStep.pop()
            open_list.append(a)
        if len(open_list) == 0: return centraList #operation was completed!

#Importance: xx
#1-looks for all guys and return their centralities
#INPUT : dictioCentral
#A = {'a': True, 'c': True, 'b': True, 'e': True, 'd': True}
#G = {'a': {'1': 1, '3': 1, '2': 1, '5': 1, '4': 1}, 'c': {'3': 1, '2': 1, '6': 1}, 'b': {'1': 1, '2': 1, '5': 1}, 'e': {'6': 1}, 'd': {'2': 1, '5': 1, '6': 1}, '1': {'a': 1, 'b': 1}, '3': {'a': 1, 'c': 1}, '2': {'a': 1, 'c': 1, 'b': 1, 'd': 1}, '5': {'a': 1, 'b': 1, 'd': 1}, '4': {'a': 1}, '6': {'c': 1, 'e': 1, 'd': 1}}
#print get_guy(G, 'a')
file = 'c:/udacity/Actors1.tsv'
G = read_graph(file)
alfa = get_guy(G, 'Hoffman, Dustin')
centrality = scipy.mean(alfa)
print centrality

def find_centrality():
    Alfa = 'c:/udacity/Actors1.tsv' # Read the graph
    Actor = read_actor(Alfa)
    #print Actor
    Graph = read_graph(Alfa)
    #print Graph
    dictioCentral = {}
    for guy in Actor:
        centraList = get_guy(Graph, guy)
        dictioCentral[guy] = scipy.mean(centraList)
    return dictioCentral

#print find_centrality()
#import scipy;
#a=[1,2,4,3,2,1];
#a = [8969, 10783, 6779, 641, 242, 8300, 10004, 12049, 5174, 10455, 8831, 1069, 2922, 2973, 3233, 6440, 3809, 821, 226, 9829, 1031, 8421, 1953, 940, 9741, 5194, 2677, 8316, 4178, 179, 252, 293, 1160, 10890, 6777, 11550, 5803, 1799, 5036, 3251, 5742, 2799, 7501, 7302, 475, 2186, 8949, 6660, 3637, 7033, 4661, 7902, 4774, 602, 1889, 9466, 11970, 10695, 7428, 5320, 887, 10666, 5848, 1212, 2268, 3169, 835, 4000, 11394, 324, 6198, 4659, 4942, 4966, 2741, 10901, 5056, 2048, 6615, 7209, 541, 1461, 11856, 11512, 11762, 6271, 3643, 1875, 1998, 1953, 1984, 10114, 3217, 1214, 1262, 7726, 104, 11975, 974, 7483, 8073, 648, 7954, 3323, 1782, 290, 4587, 480, 3554, 3738, 810, 1834, 1270, 7160, 3999, 166, 533, 12053, 9326, 11758, 2437, 461, 7581, 8945, 1974, 1323, 11086, 215, 9519, 3784, 10869, 7177, 1932, 1258, 745, 1340, 3906, 7638, 9528, 260, 1296, 2553, 728, 7728, 2260, 1238, 3974, 5042, 2791, 8101, 357, 423, 3532, 6018, 339, 10280, 8776, 6627, 10733, 5482, 2238, 11702, 649, 10638, 635, 1664, 10631, 136, 2740]
#a = [1, 1, 1, 1, 1, 2, 2, 2, 3, 4]
#print(scipy.mean(a));

def get_first(G, guy):
    centraList = []
    gentlemen = G[guy].keys()
    for neighbor in gentlemen:
        centraList.append(1)
    return centraList #operation was completed!

#G = {'a': {'1': 1, '3': 1, '2': 1, '5': 1, '4': 1}, 'c': {'3': 1, '2': 1, '6': 1}, 'b': {'1': 1, '2': 1, '5': 1}, 'e': {'6': 1}, 'd': {'2': 1, '5': 1, '6': 1}, '1': {'a': 1, 'b': 1}, '3': {'a': 1, 'c': 1}, '2': {'a': 1, 'c': 1, 'b': 1, 'd': 1}, '5': {'a': 1, 'b': 1, 'd': 1}, '4': {'a': 1}, '6': {'c': 1, 'e': 1, 'd': 1}}
#print get_first(G, 'a')

def find_first_degree():
    file = 'c:/udacity/Actors1.tsv' # Read the graph
    Actor = read_actor(file)
    #print Actor
    Graph = read_graph(file)
    #print Graph
    dictioCentral = {}
    for guy in Actor:
        centraList = get_first(Graph, guy)
        dictioCentral[guy] = len(centraList)
    return dictioCentral

#beta = find_first_degree()
#print beta

def find_order():
    Beta = find_first_degree()
    print Beta
    ordered = {}
    list = []
    actor = 'Null'
    while len(list) < 20:
        relevance = 0
        for guy in Beta:
            if Beta[guy] > relevance and guy not in ordered:
                actor = guy
                relevance = Beta[guy]
        ordered[actor] = True
        list.append(actor)
        #print actor, ordered
    guy = list[19]
    return guy

#answer = find_order()
#print answer