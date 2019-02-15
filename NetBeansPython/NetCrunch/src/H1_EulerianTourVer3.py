#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="epasseto"
__date__ ="$22/10/2012 10:48:06$"

#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="epasseto"
__date__ ="$17/10/2012 09:42:41$"

import itertools
# Find Eulerian Tour
#
# Write a function that takes in a graph
# represented as a list of tuples
# and return a list of nodes that
# you would follow on an Eulerian Tour
#
# For example, if the input graph was
#graph = [(1, 2), (2, 3), (3, 1)]
# A possible Eulerian tour would be [1, 2, 3, 1]
#graph = [(0, 1), (1, 5), (1, 7), (4, 5), (4, 8), (1, 6), (3, 7), (5, 9), (2, 4), (0, 4), (2, 5), (3, 6), (8, 9)] #failure!
#graph = [(1, 13), (1, 6), (6, 11), (3, 13), (8, 13), (0, 6), (8, 9),(5, 9), (2, 6), (6, 10), (7, 9), (1, 12), (4, 12), (5, 14), (0, 1), (2, 3), (4, 11), (6, 9), (7, 14), (10, 13)]
graph = [(8, 16), (8, 18), (16, 17), (18, 19), (3, 17), (13, 17), (5, 13),(3, 4), (0, 18), (3, 14), (11, 14), (1, 8), (1, 9), (4, 12), (2, 19),(1, 10), (7, 9), (13, 15), (6, 12), (0, 1), (2, 11), (3, 18), (5, 6), (7, 15), (8, 13), (10, 17)]
#control = [1,1,1]
#ex = itertools.compress(graph, control)
#for i in ex:
#    print i

def dictiograph(graph): # create a dictionnaire for the graph
    dictiog = {}
    while len(graph)>0:
        link = graph.pop()
        a = link[0]
        b = link[1]
        if a in dictiog:
            c = dictiog[a]
            c.append([b,0]) #0 is for an unvisited path
            dictiog[a] = c
        else:
            dictiog[a] = [[b,0]]
        if b in dictiog:
            c = dictiog[b]
            c.append([a,0])
            dictiog[b] = c
        else:
            dictiog[b] = [[a,0]]
    return dictiog

def testkill(neighbors, start): #must evolute this one!
    print "neighbors:", neighbors, "start:", start
    a = 0
    for i in range (0, len(neighbors)):
        candidate = neighbors[i]
        if candidate[0] != start:
            if candidate[1] == 0: a=a+1
    if a == 0: return True #enter in kill process
    else: return a

def tweak_entry(dic, neighbors, node, start):
    for i in range(0, len(neighbors)): #hash in this node
        candidate = neighbors[i]
        if candidate[1] == 0: #a viable path was found
                if candidate[0] != start: #start clause here!
                    next = candidate[0]
                    candidate[1] = 1 #break visited link
                    neighbors[i] = candidate
                    dic[node] = neighbors #marked path in dic
                    newneighbors = dic[next] #mark next also in dic
                    for j in range(0, len(newneighbors)):
                        entry = newneighbors[j]
                        if entry[0] == node:
                            entry[1] = 1 #mark retronode
                            newneighbors[j] = entry
                    print 'new:', next, newneighbors
                    dic[next] = newneighbors
                    return [next, newneighbors]
                else:
                    if testkill(neighbors, start) == True: return True #termination signal
    return None

#must find the node to start (odd, or if all even, the larger even)
def find_eulerian_tour(graph, node=0):
    tour = []
    if len(graph) == 0: return tour #no-nodes case
    dic = dictiograph(graph)
    set = dic.keys()
    while node < len(set):
        if node in dic:
            start = node #mark the start node
            tour.append(node) #get this node
            neighbors = dic[node]
            while True:
                print node, dic
                if len(neighbors) > 0:
                    answer = tweak_entry(dic, neighbors, node, start)
                    if answer == None:
                        return tour #an dead-end was found
                    elif answer == True:
                        tour.append(start)
                        return tour
                    else:
                        tour.append(answer[0])
                        node = answer[0] #go to next node
                        neighbors = answer[1]
            return tour
        else:
            node = node + 1 #look for starting node
    return tour

print find_eulerian_tour(graph)