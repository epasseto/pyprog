#! /usr/bin/python

# You may assume the following behavior of each function:
# straight(ranks): returns True if the hand is a straight.
# flush(hand):     returns True if the hand is a flush.
# kind(n, ranks):  returns the first rank that the hand has
#                  exactly n of. For A hand with 4 sevens
#                  this function would return 7.
# two_pair(ranks): if there is a two pair, this function
#                  returns their corresponding ranks as a
#                  tuple. For example, a hand with 2 twos
#                  and 2 fours would cause this function
#                  to return (4, 2).
# card_ranks(hand) returns an ORDERED tuple of the ranks
#                  in a hand (where the order goes from
#                  highest to lowest rank).
__author__="epasseto"
__date__ ="$17/04/2012 08:52:57$"

import random

mydeck = [r+s for r in '23456789TJQKA' for s in 'SHDC']

def deal(numhands, n=5, deck=mydeck):
    random.shuffle(deck)
    return [deck[n*i:n*(i+1)] for i in range(numhands)]

def poker(hands):
    #return a list of winning hands: poker([hand,...]) -> [hand,...]
    return allmax(hands, key=hand_rank)

def allmax(iterable, key=None):
    #return a list of all items equal to the max of the iterable
    result, maxval =[], None #keep track of the max value, initially None
    key = key or (lambda x: x) #maps an argument to itself
    for x in iterable:
        xval = key(x)
        if not result or xval > maxval: #not a result at all or xval is >
            result, maxval = [x], xval #create this list with single X +max=xval
        elif xval == maxval: #if is a tie, append x to a list of results
            result.append(x)
    return result

def hand_rankc(hand):
    #return a value indicating the ranking of a hand
    #counts is the count of each rank; ranks lists corresponding ranks
    #e.g. '7 T 7 9 7' -> counts = (3, 1, 1); ranks = (7, 10, 9)
    #slightly different values
    groups = group(['--23456789TJQKA'.index(r) for r, s in hand])
    counts, ranks = unzip(groups)
    if ranks == (14, 5, 4, 3, 2):
        ranks = (5, 4, 3, 2, 1)
    straight = len(ranks) == 5 and max(ranks)-min(ranks) == 4
    flush = len(set([s for r,s in hand])) == 1
    return (9 if 5,) == counts else
            8 if straight and flush else        # straight flush
            7 if (4, 1) == counts else          # 4 of a kind
            6 if (3, 2) == counts else          # full house
            5 if flush else                     # flush
            4 if straight else                  # straight
            3 if (3, 1, 1) == counts else       # 3 of a kind
            2 if (2, 2, 1) == counts else       # 2 pair
            1 if (2, 1, 1, 1) == counts else    # kind
            0), ranks                           # high card
            #partitions of number 5

def hand_rank(hand):
    #return a value indicating how high the hand ranks
    #counts is the count of each rank; ranks lists corresponding ranks
    #e.g. '7 T 7 9 7' -> counts = (3, 1, 1); ranks = (7, 9, 10)
    groups = group(['--23456789TJQKA'.index(r) for r, s in hand])
    counts, ranks = unzip(groups)
    if ranks == (14, 5, 4, 3, 2):
        ranks = (5, 4, 3, 2, 1)
    straight = len(ranks) == 5 and max(ranks)-min(ranks) == 4
    flush = len(set([s for r,s in hand])) == 1
    return max(count_rankings[counts], 4*straight + 5*flush), ranks
                                       #conversion of boolean to integer
count_rankings = {(5,):10, (4, 1):7 (3, 2):6, (3, 1, 1):3, (2, 2, 1):2,
                 (2, 1, 1, 1):1, (1, 1, 1, 1, 1):0}
    

def hand_rankb(hand):
    #return a value indicating the ranking of a hand
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):            # straight flush
        return (8, max(ranks)) #2 3 4 5 6 (8,6)
    elif kind(4, ranks):                           # 4 of a kind
        return (7, kind(4, ranks), kind(1, ranks)) # 9 9 9 9 3 (7, 9, 3)
    elif kind(3, ranks) and kind(2, ranks):        # full house
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):                              # flush
        return (5,ranks)
    elif straight(ranks):                          # straight
        return (4, max(ranks))
    elif kind(3, ranks):                           # 3 of a kind
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):                          # 2 pair
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):                           # kind
        return (1, kind(2, ranks), ranks)
    else:                                          # high card
        return (0, ranks)                          # allways sorted!

def group(items):
    #return a list of [(count, x)...], highest count first, then highest first
    groups = [(items.count(x), x) for x in set (items)]
    return sorted(groups, reverse=True)

def unzip(pairs): return zip(*pairs)
    #turn it in a pair of lists list of pairs in a pair of lists!

def card_ranks(hand):
    #returna a list of the ranks, sorted with higher first
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand] #iterating over
                           #the cards: rank,suit, only collect up the rank
                           #modified set: '-A23456789TJQKA'
    ranks.sort(reverse=True)
    return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks
                           #a 'ad-hoc' fix return

def my_straight(ranks):
    "Return True if the ordered ranks form a 5-card straight."
    a = ranks[0]
    count = 1
    while count < len(ranks):
        b = ranks[count]
        if b < a:
            a = b
        else:
            return False
        count = count + 1
    return True

def straight(ranks):
    return (max(ranks)-min(ranks) == 4) and len(set(ranks)) == 5
    # distance of max and min is 4          all cards are different

def my_flush(hand):
    "Return True if all the cards have the same suit."
    a = hand[0]
    count = 1
    while count < len(hand):
        b = hand[count]
        if b[1] != a[1]:
            return False
        count = count + 1
    return True

def flush(hand):
    suits = [s for r,s in hand] #extract for rank and suit, save suit
    return len(set(suits)) == 1 #lenght of set must be 1

def kind(n, ranks):
    #return the first rank that this hand has exactly n of
    #return None if there is no n-of-a-kind in the hand
    for rank in ranks:
        if ranks.count(rank) == n: return rank
    return None

def two_pair(ranks):
    #if there are two pair, return the two ranks as a tuple: (highest, lowest)
    #otherwise, return None
    pair = kind(2, ranks) #get the first pair, if has one
    lowpair = kind(2, list(reversed(ranks))) #get the second pair in reversed
    if pair and lowpair != pair: #if there are really two pairs
        return (pair, lowpair)
    else:
        return None

def hand_percentages(n=700*1000):
    #sample n random hands and print a table of percentages for each type hand
    counts = [0]*9 #make a vector counts that starts with 9
    for i in range(n/10): #10 hands
        for hand in deal(10): #10 times
            ranking = hand_rank(hand)[0]
            counts[ranking] += 1
        for i in reversed(range(9)):
            print '%14s: %6.3f %%' % (hand_names[i], 100.*counts[i]/n)

def test():
    #test cases for functions in poker program
    sf = '6C 7C 8C 9C TC'.split()  # Straight Flush give a list of these cards
    fk = '9D 9H 9S 9C 7D'.split()  # Four of a Kind
    fh = 'TD TC TH 7C 7D'.split()  # Full House
    #fl = 'TD 8D 7D 5D 3D'.split() # Flush
    s1 = 'AS 2S 3S 4S 5C'.split()  # Straight A-5 <-is a particular hand, A=1
    #1 modify function Straight 2 modify function Handrank 3 modify Cardranks
    s2 = '2C 3C 4C 5S 6S'.split()  # Straight 2-6
    #tk = 'JD JC JH 3D 2H'.split() # 3 of a Kind
    tp = '5S 5D 9H 9C 6S'.split()  # 2 pair <-needs ordering!
    #ki = 'JD JC 9C 5D 3H'.split() # Kind
    ah = 'AS 2S 3S 4S 6C'.split()  # High Card A
    sh = '2s 3s 4s 6c 7D'.split()  # High Card 7
    fkranks = card_ranks(fk)
    tpranks = card_ranks(tp)
    assert kind(4, fkranks) == 9 #4 of 9s in set!
    assert kind(3, fkranks) == None
    assert kind(2, fkranks) == None
    assert kind(1, fkranks) == 7 #1 of 7 in set!
    assert two_pair(fkranks) == None
    assert two_pair(tpranks) == (9, 5) #has 2 pairs, a 9 and a 5-pair!
    #assert poker([sf, fk, fh]) == sf #poker played, winning hand is sf
    #assert poker([fk, fh]) == fk
    #assert poker([fh, fh]) == fh
    #assert poker([fh]) == fh #1hand
    #assert poker([sf] + 99*[fk]) == sf #100hands
    assert hand_rank(sf) == (8, 10)    #straight flush
    assert hand_rank(fk) == (7, 9, 7)  #four of a kind
    assert hand_rank(fh) == (6, 10, 7) #full house
    #assert hand_rank(fl) == (5, [10, 8, 7, 5, 3]) #flush
    #assert hand_rank(st) == (4, 11) #straight
    #assert hand_rank(tk) == (3, 11, [11, 11, 11, 3, 2]) #3 of a kind
    #assert hand_rank(tp) == (2, 9, 5, [9, 9, 6, 5, 5]) #2 pair
    #assert hand_rank(ki) == (1, 11, [11, 11, 9, 5, 3]) #kind
    #assert hand_rank(hc) == (0, 12, 11, 9, 5, 3) #high card
    assert card_ranks(sf) == [10, 9, 8, 7, 6]
    assert card_ranks(fk) == [9, 9, 9, 9, 7]
    assert card_ranks(fh) == [10, 10, 10, 7, 7]
    assert straight([9, 8, 7, 6, 5]) == True
    assert straight([9, 8, 8, 6, 5]) == False
    assert flush(sf) == True
    assert flush(fk) == False
    return 'tests pass'
print test()