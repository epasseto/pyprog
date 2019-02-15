#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="epasseto"
__date__ ="$16/10/2012 15:12:08$"

# Finding a Favor v2
#
# Each edge (u,v) in a social network has a weight p(u,v) that
# represents the probability that u would do a favor for v if asked.
# Note that p(v,u) != p(u,v), in general.
#
# Write a function that finds the right sequence of friends to maximize
# the probability that v1 will do a favor for v2.
#

#
# Provided are two standard versions of dijkstra's algorithm that were
# discussed in class. One uses a list and another uses a heap.
#
# You should manipulate the input graph, G, so that it works using
# the given implementations.  Based on G, you should decide which
# version (heap or list) you should use.
#

# code for heap can be found in the instructors comments below
from heap import *
from operator import itemgetter

def maximize_probability_of_favor(G, v1, v2):
    # your code here
    # call either the heap or list version of dijkstra
    # and return the path from `v1` to `v2`
    # along with the probability that v1 will do a favor
    # for v2
    pass

#
# version of dijkstra implemented using a heap
#
# returns a dictionary mapping a node to the distance
# to that node and the parent
#
# Do not modify this code
#
def dijkstra_heap(G, a):
    # Distance to the input node is zero, and it has
    # no parent
    first_entry = (0, a, None)
    heap = [first_entry]
    # location keeps track of items in the heap
    # so that we can update their value later
    location = {first_entry:0}
    dist_so_far = {a:first_entry}
    final_dist = {}
    while len(dist_so_far) > 0:
        dist, node, parent = heappopmin(heap, location)
        # lock it down!
        final_dist[node] = (dist, parent)
        del dist_so_far[node]
        for x in G[node]:
            if x in final_dist:
                continue
            new_dist = G[node][x] + final_dist[node][0]
            new_entry = (new_dist, x, node)
            if x not in dist_so_far:
                # add to the heap
                insert_heap(heap, new_entry, location)
                dist_so_far[x] = new_entry
            elif new_entry < dist_so_far[x]:
                # update heap
                decrease_val(heap, location, dist_so_far[x], new_entry)
                dist_so_far[x] = new_entry
    return final_dist

#
# version of dijkstra implemented using a list
#
# returns a dictionary mapping a node to the distance
# to that node and the parent
#
# Do not modify this code
#
def dijkstra_list(G, a):
    dist_so_far = {a:(0, None)} #keep track of the parent node
    final_dist = {}
    while len(final_dist) < len(G):
        node, entry = min(dist_so_far.items(), key=itemgetter(1))
        # lock it down!
        final_dist[node] = entry
        del dist_so_far[node]
        for x in G[node]:
            if x in final_dist:
                continue
            new_dist = G[node][x] + final_dist[node][0]
            new_entry = (new_dist, node)
            if x not in dist_so_far:
                dist_so_far[x] = new_entry
            elif new_entry < dist_so_far[x]:
                dist_so_far[x] = new_entry
    return final_dist

##########
#
# Test

def test():
    G = {'a':{'b':.9, 'e':.5},
         'b':{'c':.9},
         'c':{'d':.01},
         'd':{},
         'e':{'f':.5},
         'f':{'d':.5}}
    path, prob = maximize_probability_of_favor(G, 'a', 'd')
    assert path == ['a', 'e', 'f', 'd']
    assert abs(prob - .5 * .5 * .5) < 0.001

'''
Be careful of underflow errors - which can happen when multiplying lots of small numbers (like probabilities) together: http://en.wikipedia.org/wiki/Arithmetic_underflow.

The heap module can be found on the wiki: http://www.udacity.com/wiki/CS215Final or copied from:

# modified to be able to store ids and values in heap.

# Heap shortcuts
def left(i): return i*2+1
def right(i): return i*2+2
def parent(i): return (i-1)/2
def root(i): return i==0
def leaf(L, i): return right(i) >= len(L) and left(i) >= len(L)
def one_child(L, i): return right(i) == len(L)
def val_(pair): return pair[0]

def swap(heap, old, new, location):
    location[heap[old]] = new
    location[heap[new]] = old
    (heap[old], heap[new]) = (heap[new], heap[old])

# Call this routine if the heap rooted at i satisfies the heap property
# *except* perhaps i to its children immediate children
#
#
# location is a dictionary mapping an object to its location
# in the heap
def down_heapify(heap, i, location):
    # If i is a leaf, heap property holds
    while True:
        l = left(i)
        r = right(i)

        # see if we don't have any children
        if l >= len(heap):
            break

        v = heap[i][0]
        lv = heap[l][0]

        # If i has one child...
        if r == len(heap):
            # check heap property
            if v > lv:
                # If it fails, swap, fixing i and its child (a leaf)
                swap(heap, i, l, location)
            break

        rv = heap[r][0]
        # If i has two children...
        # check heap property
        if min(lv, rv) >= v:
            break
        # If it fails, see which child is the smaller
        # and swap i's value into that child
        # Afterwards, recurse into that child, which might violate
        if lv < rv:
            # Swap into left child
            swap(heap, i, l, location)
            i = l
        else:
            # swap into right child
            swap(heap, i, r, location)
            i = r

# Call this routine if whole heap satisfies the heap property
# *except* perhaps i to its parent
def up_heapify(heap, i, location):
    # If i is root, all is well
    while i > 0:
        # check heap property
        p = (i - 1) / 2
        if heap[i][0] < heap[p][0]:
            swap(heap, i, p, location)
            i = p
        else:
            break

# put a pair in the heap
def insert_heap(heap, v, location):
    heap.append(v)
    location[v] = len(heap) - 1
    up_heapify(heap, len(heap) - 1, location)

# build_heap
def build_heap(heap):
    location = dict([(n, i) for i, n in enumerate(heap)])
    for i in range(len(heap)-1, -1, -1):
        down_heapify(heap, i, location)
    return location

# remove min
def heappopmin(heap, location):
    # small = heap[0]
    val = heap[0]
    new_top = heap.pop()
    del location[val]
    if len(heap) == 0:
        return val
    location[new_top] = 0
    heap[0] = new_top
    down_heapify(heap, 0, location)
    return val

def decrease_val(heap, location, old_val, new_val):
    i = location[old_val]
    heap[i] = new_val
    # is this the best way?
    del location[old_val]
    location[new_val] = i
    up_heapify(heap, i, location)


def _test_location(heap, location):
    for n, i in location.items():
        assert heap[i] == n

def _test_heap():
    h = [(1, 'a'), (4, 'b'), (6, 'c'), (8, 'd'),
         (9, 'e'), (1, 'f'), (4, 'g'), (5, 'h'),
         (7, 'i'), (8, 'j')]
    location = build_heap(h)
    _test_location(h, location)
    old_min = (-float('inf'), None)
    while len(h) > 0:
        new_min = remove_min_heap(h, location)
        _test_location(h, location)
        assert val_(old_min) <= val_(new_min)
        old_min = new_min

def _test_add_and_modify():
    h = [(1, 'a'), (4, 'b'), (6, 'c'), (8, 'd'),
         (9, 'e'), (1, 'f'), (4, 'g'), (5, 'h'),
         (7, 'i'), (8, 'j')]
    location = build_heap(h)
    insert_heap(h, (-1, 'k'), location)
    assert (-1, 'k') == remove_min_heap(h, location)
    decrease_val(h, location, (6, 'c'), (-1, 'c'))
    assert (-1, 'c') == remove_min_heap(h, location)
    _test_location(h, location)

'''