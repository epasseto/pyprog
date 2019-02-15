#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="epasseto"
__date__ ="$14/05/2012 10:00:00$"

def memo(f): #multiple memoize function
    #decorator that caches the return value for each call to f(args)
    #then when called again with some args, we can just look it up
    cache = {} #this is the cache
    def _f(*args):
        print 'cache is', cache
        try:
            return cache[args] #prevents repeating calculation
        except KeyError:
            cache[args] = result = f(*args)
            return result
        except TypeError:
            #some element of args cant be a dict key
            return f(args)
    return _f
@memo #memo decorator = same as: fib = memo of fib
def fib(n):
    if n <= 1: return 1
    else: return fib(n-1) + fib(n-2)
@memo
def square(n): #namespace
    return n*n

print fib(4)
print fib(4)
print square(4)
print square(4)

