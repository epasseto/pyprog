#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="epasseto"
__date__ ="$21/05/2012 13:30:50$"

import this

WORDS = set(file(words4k.txt).read().upper().split())

mnx, moab = anchor('MNX'), anchor('MOAB')
a_row = row = ['|', 'A', mnx, moab, '.', '.', ANY, 'B', 'E', ANY, 'C', ANY, '.', ANY, 'D', ANY, '|']
a_hand = 'ABCEHKN'

def a_board():
    return map(list, ['|||||||||||||||||',
                      '|J............I.|'
                      '|A.....BE.C...D.|',
                      '|GUY....F.H...L.|',
                      '|||||||||||||||||'])

def old_show(board):
    #print the board
    for row in board:
        for sq in row:
            print sq,
        print

def show(board):
    #print the board and the BONUS[j][i] entries where appropriate
    for j,row in enumerate(board):
        for i,sq in enumerate(row):
            print (sq if (is_letter(sq) or sq == '|') else BONUS[j][i]),
        print


# >>> a_board()
# [['|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|'],
#  ['|', 'J', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'I', '.', '|'],
#  ['|', 'A', '.', '.', '.', '.', '.', 'B', 'E', '.', 'C', '.', '.', '.', 'D', '.', '|'],
#  ['|', 'G', 'U', 'Y', '.', '.', '.', '.', 'F', '.', 'H', '.', '.', '.', 'L', '.', '|'],
#  ['|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|']]

# >>> show(a_board())
# | | | | | | | | | | | | | | | | |
# | J . . . . . . . . . . . . I . |
# | A . . . . . B E . C . . . D . |
# | G U Y . . . . F . H . . . L . |
# | | | | | | | | | | | | | | | | |

#>>> find_cross_word(a_board(), 2, 2)
#(2, '.U')
#>>> find_cross_word(a_board(), 1, 2)
#(1, 'JAG')
#>>> w = '.U'
#>>> anchor(L for L in LETTERS inf w.replace('.', L) in WORDS)
#anchor(['X', 'M', 'N']) #restricted or unrestricted letter

def text_row():
    assert legal_prefix(2, a_row) == ( 'A', 1)
    assert legal_prefix(2, a_row) == (  '', 0)
    assert legal_prefix(2, a_row) == (  '', 2)
    assert legal_prefix(2, a_row) == ('BE', 2)
    assert legal_prefix(2, a_row) == ( 'C', 1)
    assert legal_prefix(2, a_row) == (  '', 1)
    return 'test_row passes'

def old2_find_words(hand):
    'find all words that can be made from the letters in hand'
    results = set()
    for a in hand:
        if a in WORDS: results.add(a)
        for b in removed(hand, a):
            w = a+b
            if w in WORDS: results.add(w)
            for c in removed(hand, w):
                w = a+b+c
                if w in WORDS: results.add(w)
                for d in removed(hand, w):
                    w = a+b+c+d
                    if w in WORDS: results.add(w)
                    for e in removed(hand, w):
                        w = a+b+c+d+e
                        if w in WORDS: results.add(w)
                        for f in removed(hand, w):
                            w = a+b+c+d+e+f
                            if w in WORDS: results.add(w)
                            for g in removed(hand, w):
                                w = a+b+c+e+f+g
                                if w in WORDS: results.add(w)
    return results

def old_find_words(letters):
    'find all words that can be made from letters'
    results = set()
    for a in letters:
        if a in WORDS: results.add(a)
        if a not in PREFIXES: continue
        for b in removed(letters, a):
            w = a+b
            if w in WORDS: results.add(w)
            if w not in PREFIXES: continue
            for c in removed(letters, w):
                w = a+b+c
                if w in WORDS: results.add(w)
                if w not in PREFIXES: continue
                for d in removed(letters, w):
                    w = a+b+c+d
                    if w in WORDS: results.add(w)
                    if w not in PREFIXES: continue
                    for e in removed(letters, w):
                        w = a+b+c+d+e
                        if w in WORDS: results.add(w)
                        if w not in PREFIXES: continue
                        for f in removed(letters, w):
                            w = a+b+c+d+e+f
                            if w in WORDS: results.add(w)
                            if w not in PREFIXES: continue
                            for g in removed(letters, w):
                                w = a+b+c+e+f+g
                                if w in WORDS: results.add(w)
                                if w not in PREFIXES: continue
    return results

test_words()

def word_plays(hand, board_letters):
    'find all word plays from hand that can be made to abut with a letter on board'
    #find prefix + L + suffix; L from board_letters, rest from hand
    results = set()
    for pre in find_prefixes(hand, '', set()):
        for L in board_letters:
            add_suffixes(removed(hand, pre), pre+L, results)
    return results

assert (word_plays('ADEQUAT', set('IRE')) ==
        set(['DIE', 'ATE', 'READ', 'AIT', 'DE', 'IDEA', 'RET', 'QUID', 'DATE', 'RATE',
             'ETA', 'QUIET', 'ERA', 'TIE', 'DEAR', 'AID', 'TRADE', 'TRUE', 'DEE',
             'RED', 'RAD', 'TAR', 'TAE', 'TEAR', 'TEA', 'TED', 'TEE', 'QUITE', 'RE',
             'RAT', 'QUADRATE', 'EAR', 'EAU', 'EAT', 'QAID', 'URD', 'DUI', 'DIT', 'AE',
             'AI', 'ED', 'TI', 'IT', 'DUE', 'AQUAE', 'AR', 'ET', 'ID', 'ER', 'QUIT',
             'ART', 'AREA', 'EQUID', 'RUE', 'TUI', 'ARE', 'QI', 'ADEQUATE', 'RUT']))

def longest_words(hand, board_letters):
    "Return all word plays, longest first."
    words = word_plays(hand, board_letters)
    return sorted(words, reverse=True, key=len)

POINTS = dict(A=1, B=3, C=3, D=2, E=1, F=4, G=2, H=4, I=1, J=8, K=5, L=1, M=3, N=1, O=1, P=3, Q=10, R=1, S=1, T=1, U=1, V=4, W=4, X=8, Y=4, Z=10, _=0)

def word_score(word):
    "The sum of the individual letter point scores for this word."
    return sum(POINTS[L] for L in word)

def topn(hand, board_letters, n=10): #James Parker - w/ great power cames great responsability
    "Return a list of the top n words that hand can play, sorted by word score."
    words = word_plays(hand, board_letters)
    return sorted(words, reverse=True, key=word_score)[:n]

def removed(letters, remove):
    'return a str of letters, but with each letter in remove removed once'
    for L in remove:
        letters = letters.replace(L, '', 1) #replace with empty string
    return letters

def prefixes(word):
    'a list of the initial sequences of a word, not including the complete word'
    return [word[:i] for i in range (len(word))]

def old_readwordlist(filename):
    'return a pair of sets: all the words in a file, and all the prefixes. (Uppercased.)'
    wordset = set(file(filename).read().upper().split())
    prefixset = set(p for word in wordset for p in prefixes(word))
    return wordset, prefixset

WORDS, PREFIXES = readwordlist('words4k.txt')

def readwordlist(filename):
    'return a pair of sets: all the words in a file, and all the prefixes. (Uppercased.)'
    file = open(filename)
    text = file.read().upper()
    wordset = set(word for word in text.splitlines())
    prefixset = set(p for word in wordset for p in prefixes(word))
    return wordset, prefixset

WORDS, PREFIXES = readwordlist('words4k.txt')

'''def find_words(letters):
    return extend_prefix('', letters, set())
        
def extend_prefix(pre, letters, results):
    if pre in WORDS: result.add(pre)
    if pre in PREFIXES:
        for L in letters: #nested loop
            extend_prefix(pre+L, letters.replace(L, '', 1), results)
    return results'''

class anchor(set):
    'an anchor is where a new word can be placed - a set of allowable letters'

LETTERS = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
ANY = anchor(LETTERS) #anchor can be any letter

def is_letter(sq):
    return isinstance(sq, str) and sq in LETTERS

def is_empty(sq):
    #is this an empty square (no letters, but a valid position on board)
    return sq == '.' or sq == '*' or isinstance(sq, anchor) #* is middle of board

def old_add_suffixes(hand, pre, results):
    """Return the set of words that can be formed by extending pre with letters in hand."""
    if pre in WORDS: results.add(pre)
    if pre in PREFIXES:
        for L in hand:
            add_suffixes(hand.replace(L, '', 1), pre+L, results)
    return results

def add_suffixes(hand, pre, start, row, results, anchored=True):
    "Add all possible suffixes, and accumulate (start, word) pairs in results."
    i = start + len(pre)
    if pre in WORDS and anchored and not is_letter(row[i]):
        results.add((start, pre))
    if pre in PREFIXES:
        sq = row[i]
        if is_letter(sq):
            add_suffixes(hand, pre+sq, start, row, results)
        elif is_empty(sq):
            possibilities = sq if isinstance(sq, set) else ANY
            for L in hand:
                if L in possibilities:
                    add_suffixes(hand.replace(L, '', 1), pre+L, start, row, results)
    return results

def legal_prefix(i, row):
    #a legal prefix of an acnhor at row[i] is either a string of letters
    #already on the board, or new letters that fit into an empty space
    #return the tuple (prefix_on_board, maxsize) to indicate this
    #e.g. legal_prefix(a_row, 9) == ('BE', 2) and for 6, ('', 2)
    s = i
    while is_letter(row[s-1]): s -=1
    if s < i: #there is a prefix
        return ''.join(row[s:i]), i-s
    while is_empty(row[s-1]) and not isinstance(row[s-1], anchor): s -= 1
    return ('', i-s)

prev_hand, prev_results = '', set() # cache for find_prefixes

def find_prefixes(hand, pre='', results=None):
    'find all prefixes (of words) that can be made from letters in hand'
    if results is None: results = set()
    if pre in PREFIXES:
        results.add(pre)
        for L in hand:
            find_prefixes(hand.replace(L, '', 1), pre+L, results)
    return results

def row_plays(hand, row):
    #return a set of legal plays in row. a row play is an (start, 'WORD') pair
    results = set()
    # to each allowable prefix, add all suffices, keeping words
    for (i, sq) in enumerate(row[1:-1], 1): #not borders!
        if isinstance(sq, anchor):
            pre, maxsize = legal_prefix(i, row)
            if pre: #add to the letters already on the board
                start = i - len(pre)
                add_suffixes(hand, pre, start, row, results, anchored=False)
            else: #empty to left: go through the set of all possible prefixes
                for pre in find_prefixes(hand):
                    if len(pre) <= maxsize:
                        start = i - len(pre)
                        add_suffixes(removed(hand, pre), pre, start, row, results,
                                    anchored=False)
    return results

def find_cross_word(board, i, j):
    """Find the vertical word that crosses board[j][i]. Return (j2, w),
    where j2 is the starting row, and w is the word"""
    sq = board[j][i]
    w = sq if is_letter(sq) else '.'
    for j2 in range(j, 0, -1):
        sq2 = board[j2-1][i]
        if is_letter(sq2): w = sq2 + w
        else: break
    for j3 in range(j+1, len(board)):
        sq3 = board[j3][i]
        if is_letter(sq3): w = w + sq3
        else: break
    return (j2, w)

def neighbors(board, i, j):
    """Return a list of the contents of the four neighboring squares,
    in the order N,S,E,W."""
    return [board[j-1][i], board[j+1][i],
            board[j][i+1], board[j][i-1]]

def transpose(matrix):
    #transpose e.g. [[1,2,3], [4,5,6]] to [1,4], [2,5], [3,6]]
    #or [[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]
    return map(list, zip(*matrix))

def set_anchors(row, j, board):
    """Anchors are empty squares with a neighboring letter. Some are resticted
    by cross-words to be only a subset of letters."""
    for (i, sq) in enumerate(row[1:-1], 1):
        neighborlist = (N,S,E,W) = neighbors(board, i, j)
        # Anchors are squares adjacent to a letter.  Plus the '*' square.
        if sq == '*' or (is_empty(sq) and any(map(is_letter, neighborlist))):
            if is_letter(N) or is_letter(S):
                # Find letters that fit with the cross (vertical) word
                (j2, w) = find_cross_word(board, i, j)
                row[i] = anchor(L for L in LETTERS if w.replace('.', L) in WORDS)
            else: # Unrestricted empty square -- any letter will fit.
                row[i] = ANY

def old_horizontal_plays(hand, board):
    #find all horizontal plays -- ((i, j), word) pairs -- across all rows
    results = set()
    for (j, row) in enumerate(board[1:-1], 1): #only the good ones
        set_anchor(row, j, board)
        for (i, word) in row_plays(hand, row):
            results.add(((i, j), word))
    return results

def horizontal_plays(hand, board):
    #find all horizontal plays -- (score, pos, word) pairs -- across all rows
    results = set()
    for (j, row) in enumerate(board[1:-1], 1): #only the good ones
        set_anchor(row, j, board)
        for (i, word) in row_plays(hand, row):
            results.add((score, (i, j), word))
    return results

def old_all_plays(hand, board):
    #all plays in both directions. A plai is a (pos, dir, word) tuple,
    #where pos is an (i, j) pair, and dir is ACROSS or DOWN
    hplays = horizontal_plays(hand, board) #set of ((i, j), word)
    vplays = horizontal_plays(hand, transpose(board)) #set of ((j, i), word)
    return (set(((i, j), ACROSS, w) for ((i, j), w) in hplays) | #union them
            set(((i, j), DOWN, w) for ((j, i), w) in vplays))

def all_plays(hand, board):
    #all plays in both directions. A plai is a (score, pos, dir, word) tuple,
    #where pos is an (i, j) pair, and dir is ACROSS or DOWN
    hplays = horizontal_plays(hand, board) #set of ((i, j), word)
    vplays = horizontal_plays(hand, transpose(board)) #set of ((j, i), word)
    return (set((score, (i, j), ACROSS, w) for (score, (i, j), w) in hplays) | #union them
            set((score, (i, j), DOWN, w) for (score, (j, i), w) in vplays))

def bonus_template(quadrant):
    #make a board from the upper-left quadrant
    reuturn mirror(map(mirror, quadrant.split()))

def mirror(sequence): return sequence + sequence[-2::-1]

SCRABBLE = bonus_template("""
|||||||||
|3..:...3
|.2...;..
|..2....:
|...2....
|.;...;..
|..:...:.
|3..:...*
""")

WWF = bonus_template("""
|||||||||
|...3..;.
|..:..2..
|.:..:...
|3..;...2
|..:...:.
|;...:...
|...:...*
""")

BONUS = WWF

DW, TW, DL, TL = '23:;' #doubleword, tripleword, doubleletter, tripleletter

def calculate_score(board, pos, direction, hand, word):
    #return the total score for this play
    total, crosstotal, word_mult = 0, 0, 1 #recursive score
    starti, startj = pos
    di, dj = direction
    other_direction = DOWN if direction == ACROSS else ACROSS
    for (n, L) in enumerate(word):
        i, j = starti + n*di, startj + n*dj
        sq = board[j][i]
        b = BONUS[j][i]
        word_mult *= (1 if is_letter(sq) else
                      3 if b == TW else 2 if b in (DW,'*') else 1)
        letter_mult = (1 if is_letter(sq) else #more abstract
                       3 if b == TL else 2 if b == DL else 1)
        total += POINTS[L] * letter_mult
        if isinstance(sq, anchor) and sq is not ANY and direction is not DOWN:
            crosstotal += cross_word_score(board, L, (i, j), other_direction)
    return crosstotal + word_mult * total

def cross_word_score(board, L, pos, direction):
    #return the score of a word made in the other direction from the main word
    i, j = pos
    (j2, word) = find_cross_word(board, i, j)
    return calculate_score(board, (i, j2), DOWN, L, word.replace('.', L))

ACROSS, DOWN = (1, 0), (0, 1) #directions that words can go

###
# IA......BE.C...D.I <-this board

## Alternative version
def old_find_words(letters, pre='', results=None):
    if results is None: results = set()
    if pre in WORDS: results.add(pre)
    if pre in PREFIXES:
        for L in letters:
            find_words(letters.replace(L, '', 1), pre+L, results)
    return results

def old2_find_words(letters):
    return extend_prefix('', letters, set()) #more concise, general

    def extend_prefix(pre, letters, results):
    if pre in WORDS: results.add(pre)
    if pre in PREFIXES:
        for L in letters:
            extend_prefix(pre+L, letters.replace(L, '', 1), results)
    return results

def find_words(letters, pre='', results=None):
    if results is None: results = set()
    if pre in WORDS: results.add(pre)
    if pre in PREFIXES:
        for L in letters:
            find_words(letters.replace(L, '', 1), pre+L, results)
    return results

test_words()

'''OLD    def extend_prefix(w, letters):
        if w in WORDS:
        if w not in PREFIXES: return
        for L in letters: #nested loop
            extend_prefix(w+L, removed(letters, L))

    extend_prefix('', letters)
    return results'''

def make_play(play, board):
    #put the word down on the board
    (score, (i, j), (di, dj), word) = play
    for (n, L) in enumerate(word):
        board[j+ n*dj][i + n*di] = L
    return board

def best_play(hand, board):
    #return the highest-scoring play | None
    plays = all_plays(hand, board)
    return sorted(plays)[-1] if plays else NOPLAY

NOPLAY = None

def show_best(hand, board):
    print 'Current board:'
    show(board)
    play = best_play(hand, board)
    if play:
        print '\nNew word: %r scores %d' % (play[-1], play[0])
        show(make_play(play, board))
    else:
        print 'Sorry, no legal plays'

def test():
    assert len(WORDS)    == 3892
    assert len(PREFIXES) == 6475
    assert 'UMIAQS' in WORDS
    assert 'MOVING' in WORDS
    assert 'UNDERSTANDIN' in PREFIXES
    assert 'ZOMB' in PREFIXES
    return 'tests pass'

assert prefixes('WORD') == ['', 'W', 'WO', 'WOR']

print text()

"""find_words('LETTERS')

hands = { ## Regresson test

'ABECDR': : set (['TO', stone...

])}"""
def timedcall(fn, *args):
    "Call function with args; return the time in seconds and result."
    t0 = time.clock()
    result = fn(*args)
    t1 = time.clock()
    return t1-t0, result

timedcall (map, find_words, hands)

hands = {  ## Regression test
    'ABECEDR': set(['BE', 'CARE', 'BAR', 'BA', 'ACE', 'READ', 'CAR', 'DE', 'BED', 'BEE',
         'ERE', 'BAD', 'ERA', 'REC', 'DEAR', 'CAB', 'DEB', 'DEE', 'RED', 'CAD',
         'CEE', 'DAB', 'REE', 'RE', 'RACE', 'EAR', 'AB', 'AE', 'AD', 'ED', 'RAD',
         'BEAR', 'AR', 'REB', 'ER', 'ARB', 'ARC', 'ARE', 'BRA']),
    'AEINRST': set(['SIR', 'NAE', 'TIS', 'TIN', 'ANTSIER', 'TIE', 'SIN', 'TAR', 'TAS',
         'RAN', 'SIT', 'SAE', 'RIN', 'TAE', 'RAT', 'RAS', 'TAN', 'RIA', 'RISE',
         'ANESTRI', 'RATINES', 'NEAR', 'REI', 'NIT', 'NASTIER', 'SEAT', 'RATE',
         'RETAINS', 'STAINER', 'TRAIN', 'STIR', 'EN', 'STAIR', 'ENS', 'RAIN', 'ET',
         'STAIN', 'ES', 'ER', 'ANE', 'ANI', 'INS', 'ANT', 'SENT', 'TEA', 'ATE',
         'RAISE', 'RES', 'RET', 'ETA', 'NET', 'ARTS', 'SET', 'SER', 'TEN', 'RE',
         'NA', 'NE', 'SEA', 'SEN', 'EAST', 'SEI', 'SRI', 'RETSINA', 'EARN', 'SI',
         'SAT', 'ITS', 'ERS', 'AIT', 'AIS', 'AIR', 'AIN', 'ERA', 'ERN', 'STEARIN',
         'TEAR', 'RETINAS', 'TI', 'EAR', 'EAT', 'TA', 'AE', 'AI', 'IS', 'IT',
         'REST', 'AN', 'AS', 'AR', 'AT', 'IN', 'IRE', 'ARS', 'ART', 'ARE']),
    'DRAMITC': set(['DIM', 'AIT', 'MID', 'AIR', 'AIM', 'CAM', 'ACT', 'DIT', 'AID', 'MIR',
         'TIC', 'AMI', 'RAD', 'TAR', 'DAM', 'RAM', 'TAD', 'RAT', 'RIM', 'TI',
         'TAM', 'RID', 'CAD', 'RIA', 'AD', 'AI', 'AM', 'IT', 'AR', 'AT', 'ART',
         'CAT', 'ID', 'MAR', 'MA', 'MAT', 'MI', 'CAR', 'MAC', 'ARC', 'MAD', 'TA',
         'ARM']),
    'ADEINRST': set(['SIR', 'NAE', 'TIS', 'TIN', 'ANTSIER', 'DEAR', 'TIE', 'SIN', 'RAD',
         'TAR', 'TAS', 'RAN', 'SIT', 'SAE', 'SAD', 'TAD', 'RE', 'RAT', 'RAS', 'RID',
         'RIA', 'ENDS', 'RISE', 'IDEA', 'ANESTRI', 'IRE', 'RATINES', 'SEND',
         'NEAR', 'REI', 'DETRAIN', 'DINE', 'ASIDE', 'SEAT', 'RATE', 'STAND',
         'DEN', 'TRIED', 'RETAINS', 'RIDE', 'STAINER', 'TRAIN', 'STIR', 'EN',
         'END', 'STAIR', 'ED', 'ENS', 'RAIN', 'ET', 'STAIN', 'ES', 'ER', 'AND',
         'ANE', 'SAID', 'ANI', 'INS', 'ANT', 'IDEAS', 'NIT', 'TEA', 'ATE', 'RAISE',
         'READ', 'RES', 'IDS', 'RET', 'ETA', 'INSTEAD', 'NET', 'RED', 'RIN',
         'ARTS', 'SET', 'SER', 'TEN', 'TAE', 'NA', 'TED', 'NE', 'TRADE', 'SEA',
         'AIT', 'SEN', 'EAST', 'SEI', 'RAISED', 'SENT', 'ADS', 'SRI', 'NASTIER',
         'RETSINA', 'TAN', 'EARN', 'SI', 'SAT', 'ITS', 'DIN', 'ERS', 'DIE', 'DE',
         'AIS', 'AIR', 'DATE', 'AIN', 'ERA', 'SIDE', 'DIT', 'AID', 'ERN',
         'STEARIN', 'DIS', 'TEAR', 'RETINAS', 'TI', 'EAR', 'EAT', 'TA', 'AE',
         'AD', 'AI', 'IS', 'IT', 'REST', 'AN', 'AS', 'AR', 'AT', 'IN', 'ID', 'ARS',
         'ART', 'ANTIRED', 'ARE', 'TRAINED', 'RANDIEST', 'STRAINED', 'DETRAINS']),
    'ETAOIN': set(['ATE', 'NAE', 'AIT', 'EON', 'TIN', 'OAT', 'TON', 'TIE', 'NET', 'TOE',
         'ANT', 'TEN', 'TAE', 'TEA', 'AIN', 'NE', 'ONE', 'TO', 'TI', 'TAN',
         'TAO', 'EAT', 'TA', 'EN', 'AE', 'ANE', 'AI', 'INTO', 'IT', 'AN', 'AT',
         'IN', 'ET', 'ON', 'OE', 'NO', 'ANI', 'NOTE', 'ETA', 'ION', 'NA', 'NOT',
         'NIT']),
    'SHRDLU': set(['URD', 'SH', 'UH', 'US']),
    'SHROUDT': set(['DO', 'SHORT', 'TOR', 'HO', 'DOR', 'DOS', 'SOUTH', 'HOURS', 'SOD',
         'HOUR', 'SORT', 'ODS', 'ROD', 'OUD', 'HUT', 'TO', 'SOU', 'SOT', 'OUR',
         'ROT', 'OHS', 'URD', 'HOD', 'SHOT', 'DUO', 'THUS', 'THO', 'UTS', 'HOT',
         'TOD', 'DUST', 'DOT', 'OH', 'UT', 'ORT', 'OD', 'ORS', 'US', 'OR',
         'SHOUT', 'SH', 'SO', 'UH', 'RHO', 'OUT', 'OS', 'UDO', 'RUT']),
    'TOXENSI': set(['TO', 'STONE', 'ONES', 'SIT', 'SIX', 'EON', 'TIS', 'TIN', 'XI', 'TON',
         'ONE', 'TIE', 'NET', 'NEXT', 'SIN', 'TOE', 'SOX', 'SET', 'TEN', 'NO',
         'NE', 'SEX', 'ION', 'NOSE', 'TI', 'ONS', 'OSE', 'INTO', 'SEI', 'SOT',
         'EN', 'NIT', 'NIX', 'IS', 'IT', 'ENS', 'EX', 'IN', 'ET', 'ES', 'ON',
         'OES', 'OS', 'OE', 'INS', 'NOTE', 'EXIST', 'SI', 'XIS', 'SO', 'SON',
         'OX', 'NOT', 'SEN', 'ITS', 'SENT', 'NOS'])}


def test_words():
    assert removed('LETTERS', 'L') == 'ETTERS'
    assert removed('LETTERS', 'T') == 'LETERS'
    assert removed('LETTERS', 'SET') == 'LTER'
    assert removed('LETTERS', 'SETTER') == 'L'
    t, results = timedcall(map, find_words, hands)
    for ((hand, expected), got) in zip(hands.items(), results):
        assert got == expected, 'Fr %r: got %s, expected %s (diff %s)' % (
            hand, got, expected, ^ got)
    return t

print test_words()

def test_board():
    assert find_cross_word(a_board(), 2, 2) == (2, '.U')
    assert find_cross_word(a_board(), 3, 2) == (2, '.Y')
    assert find_cross_word(a_board(), 5, 2) == (2, '.')
    assert find_cross_word(a_board(), 8, 2) == (2, 'EF')
    assert find_cross_word(a_board(), 8, 1) == (1, '.EF')
    assert find_cross_word(a_board(), 7, 3) == (2, 'B.')
    assert neighbors(a_board(), 2, 2) == ['.', 'U', '.', 'A']
    assert transpose([[1,2,3], [4,5,6]]) == [[1, 4], [2, 5], [3, 6]]
    assert transpose(transpose(a_board())) == a_board()
    b = a_board()
    set_anchors(b[2], 2, b)
    assert b[2] == a_row
    assert sorted(horizontal_plays(a_hand, a_board())) == [
        ((1, 1), 'JAB'), ((1, 1), 'JACK'), ((1, 2), 'AN'),
        ((1, 1), 'ANA'), ((3, 2), 'AB'), ((3, 2), 'ACE'),
        ((3, 2), 'AE'), ((3, 2), 'AH'), ((3, 2), 'AN'),
        ((3, 2), 'ANE'), ((3, 2), 'BA'), ((3, 2), 'BACKBENCH'),
        ((3, 2), 'BAH'), ((3, 2), 'BAN'), ((3, 2), 'BE'),
        ((3, 2), 'BEN'), ((5, 1), 'KEA'), ((6, 1), 'BA'),
        ((6, 1), 'HA'), ((6, 1), 'KA'), ((6, 1), 'NA'),
        ((6, 3), 'KAF'), ((6, 3), 'KEF'), ((7, 2), 'BENCH'),
        ((7, 3), 'EF'), ((8, 1), 'KA'), ((8, 3), 'FEH'),
        ((10, 2), 'CAB'), ((10, 2), 'CAN'), ((10, 3), 'HA')] #many others
#   assert sorted(horizontal_plays(a_hand, a_board())) == [
    return 'test passed'

def test_score():
    assert mirror('|.....*') == '|.....*.....|'
    assert mirror('^._') == '^._.^'
    assert bonus_template("""
    ||||
    |3.3
    |.:.
    |3.*
    """) == [
    '|||||||',
    '|3.3.3|',
    '|.:.:.|',
    '|3.3.3|',
    '|||||||']
    assert sorted(all_plays(a_hand, a_board()), reverse=True)
    return 'test_score passes'

print test_score