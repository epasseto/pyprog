#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="epasseto"
__date__ ="$18/09/2012 10:48:15$"

#import random
#L = [random, randrange(90)+10 for i in range(20)
L = [50, 88, 27, 58, 30, 21, 58, 13, 84, 24, 29, 43, 61, 44, 65, 74, 76, 30, 82, 42]

#heap shortcuts
def left(i):        return i*2+1
def right(i):       return i*2+2
def parent(i):      return (i-1)/2
def root(i):        return i==0
def leaf(L, i):     return right(i)>=len(L) and left(i)>=len(l) #no child
def one_child(L,i): return right(i) == len(L) #olher extreme of the list

#call this routine if the heap rooted at i satisfies the heap property
#except: pehaps i to its children immediate children
def down_heapify(L, i): #if i is a leaf, heap property holds
    if leaf(L, i): return #done (heap property restored)
    if one_child(L, i): #if i has one child...
        if L[i]>L[left(i)]: #check heap property
            (L[i], L[left(i)]) = (L[left(i)], L[i]) #if fails, swap fixing i and its child (a leaf)
        return
    if min(L[left(i)], L[right(i)])>=L[i]: return #if it has two children check heap property - intermediary node
    if L[left(i)]<L[right(i)]:
        (L[i], L[left(i)]) = (L[left(i)], L[i]) #swap into left child
    down_heapify(L, left(i)) #heapify on left child - continue the process - bubbling down the tree
    return
    (L[i], L[right(i)]) = (L[right(i)], L[i])
    down_heapify(L, right(i)) #same thing on right
    return
