#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="epasseto"
__date__ ="$16/10/2012 14:56:12$"

#DFS depth-first search
v1 = 0
open_list = [v1]
visited = {}
visited[v1] = True
while len(open_list) > 0:
    pick = len(open_list) - 1 #DFS
    current = open_list[pick]
    del open_list[pick]
    for neighbor in G[current].keys():
        if neighbor not in visited:
            open_list.append(neighbor)
            visited[neighbor] = True

#BFS breadth-first search
v1 = 0
open_list = [v1]
visited = {}
visited[v1] = True
while len(open_list) > 0:
    pick = 0  #BFS
    current = open_list[pick]
    del open_list[pick]
    for neighbor in G[current].keys():
        if neighbor not in visited:
            open_list.append(neighbor)
            visited[neighbor] = True

