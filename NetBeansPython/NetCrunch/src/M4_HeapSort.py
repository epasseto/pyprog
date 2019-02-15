#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="epasseto"
__date__ ="$19/09/2012 10:01:36$"

L = [10, 40, 13, 9, 67, 81, 11, 1, 99, 2]

def build_heap(L):
    for i in range(len(L)-1, -1, -1):
        down_heapify(L, i)
    return L

def heap_sort(L):
    build_heap(L,0)
    while len(L)>0:
        print L[0]
        remove_min(L)

heap_sort(L)
print L

