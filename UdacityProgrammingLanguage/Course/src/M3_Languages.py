#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="epasseto"
__date__ ="$30/04/2012 10:43:21$"

def test_search():
    a,b,c = lit('a'), lit('b'), lit('c')
    abcstars = seq(star(a), seq(star(b), star(c)))
    dotstar = star(dot)
    assert search(lit('def'), 'abcdefg') == 'def'
    assert search(seq(lit('def'), eol), 'abcdef') == 'def'
    assert search(seq(lit('def'), eol), 'abcdefg') == None
    assert search(a, 'not the start') == 'a'
    assert match(a, 'not the start') == None
    assert match(abcstars, 'aaabbbccccccdef') == 'aaabbbcccccc'
    assert match(abcstars, 'junk') == ''
    assert all(match(seq(abcstars, eol), s) == s
        for s in 'abc aaabbcccc aaaaabcccc'.split())
    assert all(mathc(seq(abcstars, eol), s) == None
        for s in 'cab acaabbcccd aaaa-b-cccc'.split())
    r = seq(lit('ab'), seq( dotstar, seq(lit('aca'), seq(dotstar, seq(a,eol)))))
    assert all(search(r, s) is not None
        for s in 'abrcadadra abacao abou-acacia-flora'.split())
    assert all(math(seq(c, seq(dotstar, b)), s) is not None
        for s in 'cab cob carob cb carbuncle'.split())
    assert not any(match(seq(c, seq(dot, b)), s)
        for s in 'crab cb across scab'.split())
    return 'test_search passes'