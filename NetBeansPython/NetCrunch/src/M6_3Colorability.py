#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="epasseto"
__date__ ="$09/10/2012 08:40:21$"

############
#
# Verify a coloring of a graph
#
############

# if cert a k-coloring of G?
#   colors in {0, ..., k-1}

def new_verify(G, cert, k):
    if len(cert) != len(G): return False #1-if num of coloring nodes in map equals num of coloring in graph
    for node in cert.keys():
        if cert[node] not in range(k): return False #2-color is not a value color
        for neighbor in G[node]:
            if cert[neighbor] == cert[node]: return False #3-check adjacent colors
    return True
#more to check - if nodes used in the certificate are the same used in the graph

def old_verify(G, cert, k):
    country = ""
    fronteer = {}
    #print "G:", G, "Cert:", cert, "K:", k
    for key in G: #first part - crack borders
        #print "key:", keys
        country = key
        colorcountry = cert[country]
        fronteer = G[country]
        #print country, ":", colorcountry, "fronteer:", fronteer
        for key in fronteer:
            border = key
            colorborder = cert[border]
            #print "border:", border, ":", colorborder
            if colorcountry == colorborder: return False #not valid!
    return True

#######
#
# Testing

def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G


(a,b,c,d,e,f,g,h) = ('a','b','c','d','e','f','g','h')
cxns = [(a,c),(a,b),(c,d),(b,d),(d,e),(d,f),(e,g),(f,g),(f,h),(g,h)]

G = {}
for (x,y) in cxns: make_link(G,x,y)


cert = {}
for (node, color) in [(a,0),(b,1),(c,2),(d,0),(e,1),(f,2),(g,0),(h,1)]:
    cert[node] = color
print verify(G,cert,3)

cert = {}
for (node, color) in [(a,0),(b,1),(c,2),(d,0),(e,0),(f,1),(g,2),(h,0)]:
    cert[node] = color
print verify(G,cert,4)
