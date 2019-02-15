#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="epasseto"
__date__ ="$25/04/2012 08:32:35$"

#def ints(start,end=None):
#    i = start
#    while i <= end or end is None:
#        yield i
#        i = i + 1

#l = ints(0,10)
#for i in l:
#    next(l)
#    print l

#def node._get_child_candidates(self, distance, min_dist, max_dist):
#    if self._leftchild and distance - max_dist < self._median:
#        yield self._leftchild
#    if self._rightchild and distance + max_dist >= self._median:
#        yield self._rightchild

#result, candidates = list(), [self]
#while candidates:
#    node = candidates.pop()
#    distance = node._get_dist(obj)
#    if distance <= max_dist and distance >= min_dist:
#        result.extend(node._values)
#        candidates.extend(node._get_child_candidates(distance, min_dist, max_dist))
#        return result

#first step: iterables can reach as much as you wish
#but you store all the values in memory and its not always what you want when
#you have a lot of values!
#mylist = [1, 2, 3]
#for i in mylist:
#    print(i)

#mylist = [x*x for x in range(3)]
#print mylist
#for i in mylist:
#    print(i)

#second step: generators are iterables, but you can only read them once
#Its because they do not store all values on the fly!

#mygenerator = (x*x for x in range(3))
#print mygenerator
#for i in mygenerator:
#    print(i)

#third step: yield is like return; except: function will return a generator

#def creategenerator():
#    mylist = range(3)
#    for i in mylist:
#        yield i*i

#mygenerator = creategenerator() #create the generator
#print(mygenerator) #is an object!

#for i in mygenerator:
#    print(i)


# all ints generator
#def all_ints(start, end = None):
#    "Generate integers in the order 0, +1, -1, +2, -2, +3, -3, ..."
#    i = start
#    if i == 0:
#        yield i
#        i = i + 1
#    while i <= end or end is None:
#        yield i
#        yield -i
#        i = i + 1

#for i in all_ints(0,3):
#    print(i),

def c(sequence):
    #generate items in sequence; keeping counts as we go
    #c.starts is the number of sequences started
    #c.items is number of items generated
    c.starts += 1
    for item in sequence:
        c.items += 1
        yield item