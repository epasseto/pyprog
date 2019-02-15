#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="epasseto"
__date__ ="$26/04/2012 09:39:09$"

#f = lambda Y, M, E, U, O:(1*U+10*O+100*Y) == (1*E+10*M)**2
#print f
#print f(1, 2, 3, 4, 5)
#print f(2, 1, 7, 9, 8)
#print 289 == 17**2

import itertools

def old_compile_word(word):
    """Compile a word of uppercase letters as numeric digits.
    E.g., compile_word('YOU') => '(1*U+10*O+100*Y)'
    Non-uppercase words unchanged: compile_word('+') => '+'"""
    a = 0
    m = 0
    result = ()
    string = ''
    while a < len(word):
        m = (10**a)
        adds = str(m) + '*' + word[-a-1] + '+'
        string = string + adds
        a = a + 1
    result = '(' + string[:-1] + ')'
    return result

def faster_solve(formula):
    #given a formula like 'ODD + ODD == EVEN', fill in digits to solve it
    #input formula is a string, output is a digit-filled-in string or None
    #this version precompiles the formula, only one eval per formula
    f, letters = compile_formula(formula) #gives me back the function that represents it
    for digits in itertools.permutations(1,2,3,4,5,6,7,8,9,0), len(letters)): #do all the permutations, letters at the time
        try:
            if f(*digits) is True:
                table = string.maketrans(letters, ''.join(map(str, digits))) #mapping up a translation table
                return formula.translate(table)
        except ArithmeticError:
            pass

def compile_formula(formula, verbose=False):
    #compile formula into a function
    #also return letters found, as a str, in same order as parms of function
    #for example, 'YOU == ME**2' returns
    #(lambda Y, M, E, U, O: (U+10*)+100*Y) == (E+10*M)**2), 'YMEUO'
    letters = ''.join(set(re.findall('[A-Z]', formula)))
    parms = ', '.join(letters)
    tokens = map(compile_word, re.split('([A-Z]+)', formula)) #token is a individual term like 'YOU'
    body = ''.join(tokens) #concatenating all the tokens
    f = 'lambda %s: %s' % (parms, body)
    if verbose: print f
    return eval(f) ,letters #compiles one the function

def compile_word(word):
    if word.isupper():
        terms = [('%s*%s' % (10**i, d)) for (i, d) in enumerate(word[::-1])]
        return '(' + '+'.join(terms) + ')'
    else:
        return word

print compile_word('YOU')