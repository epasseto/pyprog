#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="epasseto"
__date__ ="$16/05/2012 17:05:46$"

import itertools
from fractions import Fraction #produces an exact fraction

sex = 'BG' #random variable

def product(*variables):
    #the cartesian product (as a str) of the possibilities for each variable
    return map(''.join, itertools.product(*variables))

two_kids = product(sex, sex)

print two_kids

one_boy = [s for s in two_kids if 'B' in s]

print one_boy

def two_boys(s): return s.count('B') == 2

def condP(predicate, event):
    #Conditional probability: P(predicate(s) | s in event)
    #the proportion of states in event for which predicate is True
    pred = [s for s in event if predicate(s)]
    return Fraction(len(pred), len(event))

print condP(two_boys, one_boy)

###out of all families with two kids whith at least one boy born on Tuesday,
###what is the probability of two boys?

day = 'SMTWtFs'

two_kids_bday = product(sex, day, sex, day)

print two_kids_bday

boy_tuesday = [s for s in two_kids_bday if 'BT' in s]

print boy_tuesday

print condP(two_boys, boy_tuesday)

def report(verbose=False, predicate=two_boys, predname='2 boys',
            cases = [('2 kids', two_kids), ('2 kids born any day', two_kids_bday),
            ('at least 1 boy', one_boy),
            ('at least 1 boy born any day', boy_anyday),
            ('at least 1 boy born on Tuesday', boy_tuesday),
            ('at least 1 boy born in December', boy_december)]):
    import textwrap
    for (name, event) in cases:
        print 'P(%s | %s) = %s' % (predname, name, condP(predicate, event))
        if verbose:
            print 'Reason:\n"%s" has %d elements:\n%s' %(
                name, len(event), textwrap.fill(' '.join(event), 85))
            good = [s for s in event if predicate(s)]
            print 'of those, %d are "%s":\n%s\n\n' % (
                len(good), predname, textwrap, textwrap.fill(' '.join(good), 85))

report()

mont = 'JFMAmjLaSOND'

two_kids_bmonth = product(sex, month, sex, month)

boy_december = [s for s in two_kids_bmonth if 'BD' in s]

"""
P(2 boys | at least 1 boy born on Tuesday) = 13/27
Reason:
"at least 1 boy born on Tuesday" has 27 elements:
...
of those, 13 are "2 boys":
...
"""