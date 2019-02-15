#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="epasseto"
__date__ ="$18/12/2012 10:31:54$"

import csv

def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G

def make_hero(H, node1):
    if node1 not in H:
        H[node1] = {}
    H[node1] = True
    return H

# Read the marvel comics graph
def read_graph(filename):
    # Read an undirected graph in CSV format. Each line is an edge
    tsv = csv.reader(open(filename), delimiter='\t')
    G = {}
    H = {}
    for (node1, node2) in tsv:
        make_link(G, node1, node2)
        make_hero(H, node1)
    print 'done making Graph and Heroes'
    return G, H

# Create weighted graph
def old_weighted_graph():
    alfa = read_graph('c:/udacity/Marvel.tsv')
    marvelG = alfa[0]
    marvelH = alfa[1]
    print 'G',marvelG
    print 'H',marvelH
    W = {}
    mostPair = 'None'
    mostNumber = 0
    for hero1 in marvelH: #feeds hero1 list
        hqNovels = []
        novels = marvelG[hero1]
        #print 'hero1', hero1, novels
        for novel in novels:
            hqNovels.append(novel)
        if len(hqNovels) > 0:
            heroesfor2 = []
            while len(hqNovels) > 0:
                hqNovel = hqNovels.pop()
                heroes2 = marvelG[hqNovel]
                for man in heroes2:
                    heroesfor2.append(man)
            #print 'pairs', hero1, heroesfor2
            if len(heroesfor2) > 0:
                hero2=heroesfor2.pop()
                if hero1 != hero2:
                    pair1 = hero1 + ' - ' + hero2
                    pair2 = hero2 + ' - ' + hero1
                    if pair1 not in W:
                        W[pair1] = 1
                    else:
                        value = W[pair1]
                        value += 1
                        W[pair1] = value
                        if value > mostNumber:
                            mostNumber = value
                            mostPair = pair1
                            print 'new pair:', mostPair, mostNumber
                    if pair2 not in W:
                        W[pair2] = 1
                    else:
                        value = W[pair2]
                        value += 1
                        W[pair2] = value
                        if value > mostNumber:
                            mostNumber = value
                            mostPair = pair1
                            print 'new pair2:', mostPair, mostNumber
    return mostNumber, mostPair, W

# Create weighted graph
def weighted_graph():
    alfa = read_graph('c:/udacity/Marvel.tsv')
    marvelG = alfa[0]
    marvelH = alfa[1]
    print 'G',marvelG
    print 'H',marvelH
    W = {}
    mostPair = 'None'
    mostNumber = 0
    for hero1 in marvelH: #feeds hero1 list
        hqNovels = []
        novels = marvelG[hero1]
        #print 'hero1', hero1, novels
        for novel in novels:
            hqNovels.append(novel)
        heroesfor2 = []
        while len(hqNovels) > 0:
            hqNovel = hqNovels.pop()
            heroes2 = marvelG[hqNovel]
            for man in heroes2:
                heroesfor2.append(man)
        #print 'pairs', hero1, heroesfor2
        while len(heroesfor2) > 0:
            hero2=heroesfor2.pop()
            if hero1 != hero2:
                winners = sorted([hero1,hero2])
                pair = winners[0] + ' - ' + winners[1] #not duplicate pairs in dictionary
                if pair not in W:
                    W[pair] = 1
                    print 'created:', pair
                else:
                    value = W[pair]
                    value += 1
                    W[pair] = value
                    print 'added:', pair
                    if value > mostNumber:
                        mostNumber = value
                        mostPair = pair
                        print 'new pair:', mostPair, mostNumber
    return mostNumber, mostPair, W

print weighted_graph()