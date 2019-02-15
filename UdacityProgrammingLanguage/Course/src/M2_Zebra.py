#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="epasseto"
__date__ ="$23/04/2012 13:38:20$"

import itertools
#import math

houses = [1, 2, 3, 4, 5]
orderings = list(itertools.permutations(houses))

def imright(h1, h2):
    #house h1 is immediately right of h2 if h1-h2 == 1
    return h1-h2 == 1

def nextto(h1, h2):
    #two houses are next to each other if they differ by 1
    return abs(h1-h2) == 1

def slow_zebra_puzzle():
    #return a tuple (WATER, ZEBRA) indicating their house numbers
    houses = first, _, middle, _, _ = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(houses)) #1
    return next((WATER, ZEBRA)
            for (red, green, ivory, yellow, blue) in orderings
            for (Englishman, Spaniard, Ukranian, Japanese, Norwegian) in orderings
            for (dog, snails, fox, horse, ZEBRA) in orderings
            for (coffee, tea, milk, oj, WATER) in orderings
            for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in orderings
            if Englishman is red            #2 -> objects identical (x == same value)
            if Spaniard is dog              #3
            if coffee is green              #4
            if Ukranian is tea              #5
            if imright(green, ivory)        #6
            if OldGold is snails            #7
            if Kools is yellow              #8
            if milk is middle               #9
            if Norwegian is first           #10
            if nextto(Chesterfields, fox)   #11
            if nextto(Kools, horse)         #12
            if LuckyStrike is oj            #13
            if Japanese is Parliaments      #14
            if nextto(Norwegian, blue)      #15
            )

def fast_zebra_puzzle():
    #return a tuple (WATER, ZEBRA) indicating their house numbers
    houses = first, _, middle, _, _ = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(houses)) #1
    return next((WATER, ZEBRA)
            for (red, green, ivory, yellow, blue) in c(orderings)
            if imright(green, ivory)        #6
            for (Englishman, Spaniard, Ukranian, Japanese, Norwegian) in c(orderings)
            if Englishman is red            #2 -> objects identical (x == same value)
            if Norwegian is first           #10
            if nextto(Norwegian, blue)      #15
            for (dog, snails, fox, horse, ZEBRA) in c(orderings)
            if Spaniard is dog              #3
            for (coffee, tea, milk, oj, WATER) in c(orderings)
            if coffee is green              #4
            if Ukranian is tea              #5
            if milk is middle               #9
            for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in c(orderings)
            if OldGold is snails            #7
            if Kools is yellow              #8
            if nextto(Chesterfields, fox)   #11
            if nextto(Kools, horse)         #12
            if LuckyStrike is oj            #13
            if Japanese is Parliaments      #14
            )

def instrument_fn(fn, *args):
    c.starts, c.items = 0,0
    result = fn(*args)
    print '%s got %s with %5d iters over %7d items' % (fn.__name__, result, c.starts, c.items)

#print fast_zebra_puzzle() #(1, 5)
#
import time

def timedcall(fn, *args):
    #call function with args, return the time in s and result
    t0 = time.clock()
    result = fn(*args)
    t1 = time.clock()
    return t1-t0, result

def old_timedcalls(n, fn, *args):
    #call function n times with args, return min, avg and max time
    times = [timedcall(fn, *args)[0] for _ in range(n)]
    return min(times), average(times), max(times)

def timedcalls(n, fn, *args):
    #call function n times with args, return min, avg and max time
    #if n is an int or up to n seconds
    #if n is a float, return the min, avg and max time
    if isinstance(n, int):
        times = [timedcall(fn, *args)[0] for _ in range(n)]
    else:
        times = []
        while sum(times) < n:
            times  = [timedcall(fn, *args)[0] for _ in range(n)]
    return min(times), average(times), max(times)


def average(numbers):
    #return the average (artithmetic mean) of a sequence of numbers
    return sum(numbers) / float(len(numbers))


instrument_fn(fast_zebra_puzzle)
