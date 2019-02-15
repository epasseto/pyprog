#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="epasseto"
__date__ ="$26/09/2012 09:51:49$"

def dijkstra(G,v): #single node, single source from network
    dist_so_far = {} #maping from nodes - non-locked circles
    dist_so_far[v] = 0
    final_dist = {} #locked circles - deleted from dist so far
    while len(final_dist) < len(G): #risky! - if graph disconnected, crashes!
        w = shortest_dist_node(dist_so_far)
        print "lock", w, dist_so_far([w]) #lock it down!
        final_dist[w] = dist_so_far[w]
        del dist_so_far[w]
        for x in G[w]: #find what dist so far is
            if x not in final_dist:
                if x not in dist_so_far: #look for neighbors
                    dist_so_far[x] = final_dist[w] + G[w][x] #if dont have one, give this one!
                elif final_dist[w] + G[w][x] < dist_so_far[x]: #if have, check it first - this is called relaxation!
                    dist_so_far[x] = final_dist[w] + G[w][x]
    return final_dist

print dijkstra(G,a)
# print G
