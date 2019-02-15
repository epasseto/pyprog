#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="epasseto"
__date__ ="$16/05/2012 11:13:59$"

""" RE: str -> API
plus(opt(alt(lit('a), lit('b'))))  <- "(a|b)?+"
build a parser and a grammar to regrammar things that that (string notations)
regrammar = parse ('RE', text, ____)  convert from tree to API
['plus' ...]"""

REGRAMMAR = grammar("""
RE => #your description
""", whittespace='')

def parse_re(pattern):
    return convert(parse('RE', pattern, REGRAMMAR))

def convert(tree):
    ### your code here
