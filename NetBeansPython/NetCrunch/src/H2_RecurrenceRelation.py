#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="epasseto"
__date__ ="$27/08/2012 15:04:55$"

def makeG(n): #fake code
    if n == 1:
        return <a single node>
    g1 = makeG(n/2)
    g2 = makeG(n/2)
    for i in range(log(n)):
        i1 = <random node from g1 without replacement>
        i2 = <random node from g2 without replacement>
        make_ling(G, i1, i2)
    return G