#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="epasseto"
__date__ ="$11/09/2012 11:00:13$"

# Eulerian Tour Revisited
#
# Write a function, `create_tour` that takes as input a list of nodes
# and outputs a list of tuples representing edges between nodes that have an Eulerian tour.
#
# Now
# Improve ET finding routine
# if you add the line:
#   use_harder_tests = True
# to your code, the grader will use more complicated graphs

#import itertools
# Find Eulerian Tour
# Write a function that takes in a graph
# represented as a list of tuples
# and return a list of nodes that
# you would follow on an Eulerian Tour
# For example, if the input graph was
#graph = [(1, 2), (2, 3), (3, 1)]
# A possible Eulerian tour would be [1, 2, 3, 1]
#graph = [(0, 1), (1, 5), (1, 7), (4, 5), (4, 8), (1, 6), (3, 7), (5, 9), (2, 4), (0, 4), (2, 5), (3, 6), (8, 9)] #failure!
#graph = [(1, 13), (1, 6), (6, 11), (3, 13), (8, 13), (0, 6), (8, 9),(5, 9), (2, 6), (6, 10), (7, 9), (1, 12), (4, 12), (5, 14), (0, 1), (2, 3), (4, 11), (6, 9), (7, 14), (10, 13)]
#graph = [(8, 16), (8, 18), (16, 17), (18, 19), (3, 17), (13, 17), (5, 13),(3, 4), (0, 18), (3, 14), (11, 14), (1, 8), (1, 9), (4, 12), (2, 19),(1, 10), (7, 9), (13, 15), (6, 12), (0, 1), (2, 11), (3, 18), (5, 6), (7, 15), (8, 13), (10, 17)]
#harder tests
#graph = [(0, 1), (1, 2), (2, 0), (2, 3), (3, 4), (4, 2), (4, 5), (5, 6), (6, 4), (6, 7), (7, 8), (8, 6), (8, 9), (9, 10), (10, 8), (10, 11), (11, 12), (12, 10), (12, 13), (13, 14), (14, 12), (14, 15), (15, 16), (16, 14), (16, 17), (17, 18), (18, 16), (18, 19), (19, 20), (20, 18), (20, 21), (21, 22), (22, 20), (22, 23), (23, 24), (24, 22), (24, 25), (25, 26), (26, 24), (26, 27), (27, 28), (28, 26), (28, 29), (29, 30), (30, 28), (30, 31), (31, 32), (32, 30), (32, 33), (33, 34), (34, 32), (34, 35), (35, 36), (36, 34), (36, 37), (37, 38), (38, 36), (38, 39), (39, 40), (40, 38), (40, 41), (41, 42), (42, 40), (42, 43), (43, 44), (44, 42), (44, 45), (45, 46), (46, 44), (46, 47), (47, 48), (48, 46), (48, 49), (49, 50), (50, 48), (50, 51), (51, 52), (52, 50), (52, 53), (53, 54), (54, 52), (54, 55), (55, 56), (56, 54), (56, 57), (57, 58), (58, 56), (58, 59), (59, 60), (60, 58), (60, 61), (61, 62), (62, 60), (62, 63), (63, 64), (64, 62), (64, 65), (65, 66), (66, 64), (66, 67), (67, 68), (68, 66), (68, 69), (69, 70), (70, 68), (70, 71), (71, 72), (72, 70), (72, 73), (73, 74), (74, 72), (74, 75), (75, 76), (76, 74), (76, 77), (77, 78), (78, 76), (78, 79), (79, 80), (80, 78), (80, 81), (81, 82), (82, 80), (82, 83), (83, 84), (84, 82), (84, 85), (85, 86), (86, 84), (86, 87), (87, 88), (88, 86), (88, 89), (89, 90), (90, 88), (90, 91), (91, 92), (92, 90), (92, 93), (93, 94), (94, 92), (94, 95), (95, 96), (96, 94), (96, 97), (97, 98), (98, 96), (98, 99), (99, 100), (100, 98)]
graph = [(0, 1), (1, 2), (2, 0), (2, 3), (3, 4), (4, 2), (4, 5), (5, 6), (6, 4), (6, 7), (7, 8), (8, 6), (8, 9), (9, 10), (10, 8), (10, 11), (11, 12), (12, 10), (12, 13), (13, 14), (14, 15), (15, 16), (16, 14), (16, 17), (17, 18), (18, 16), (18, 19), (19, 20), (20, 18), (20, 21), (21, 22), (22, 20), (22, 23), (23, 24), (24, 22), (24, 25), (25, 26), (26, 24), (26, 27), (27, 28), (28, 26), (28, 29), (29, 30), (30, 28), (30, 31), (31, 32), (32, 30), (32, 33), (33, 34), (34, 32), (34, 35), (35, 36), (36, 34), (36, 37), (37, 38), (38, 36), (38, 39), (39, 40), (40, 38), (40, 41), (41, 42), (42, 40), (42, 43), (43, 44), (44, 42), (44, 45), (45, 46), (46, 44), (46, 47), (47, 48), (48, 46), (48, 49), (49, 50), (50, 48), (50, 51), (51, 52), (52, 50), (52, 53), (53, 54), (54, 52), (54, 55), (55, 56), (56, 54), (56, 57), (57, 58), (58, 56), (58, 59), (59, 60), (60, 58), (60, 61), (61, 62), (62, 60), (62, 63), (63, 64), (64, 62), (64, 65), (65, 66), (66, 64), (66, 67), (67, 68), (68, 66), (68, 69), (69, 70), (70, 68), (70, 71), (71, 72), (72, 70), (72, 73), (73, 74), (74, 72), (74, 75), (75, 76), (76, 74), (76, 77), (77, 78), (78, 76), (78, 79), (79, 80), (80, 78), (80, 81), (81, 82), (82, 80), (82, 83), (83, 84), (84, 82), (84, 85), (85, 86), (86, 84), (86, 87), (87, 88), (88, 86), (88, 89), (89, 90), (90, 88), (90, 91), (91, 92), (92, 90), (92, 93), (93, 94), (94, 92), (94, 95), (95, 96), (96, 94), (96, 97), (97, 98), (98, 96), (98, 99), (99, 100), (100, 98)]
#graph = [(0, 1), (1, 2), (2, 0), (0, 3), (3, 4), (4, 0), (0, 5), (5, 6), (6, 0), (0, 7), (7, 8), (8, 0), (0, 9), (9, 10), (10, 0), (0, 11), (11, 12), (12, 0), (0, 13), (13, 14), (14, 0)]
#control = [1,1,1]
marked={}
#ex = itertools.compress(graph, control)
#for i in ex:
#    print i
#G = {0: [[2, 0], [1, 0]], 1: [[2, 0], [0, 0]], 2: [[4, 0], [3, 0], [0, 0], [1, 0]], 3: [[4, 0], [2, 0]], 4: [[6, 0], [5, 0], [2, 0], [3, 0]], 5: [[6, 0], [4, 0]], 6: [[8, 0], [7, 0], [4, 0], [5, 0]], 7: [[8, 0], [6, 0]], 8: [[10, 0], [9, 0], [6, 0], [7, 0]], 9: [[10, 0], [8, 0]], 10: [[12, 0], [11, 0], [8, 0], [9, 0]], 11: [[12, 0], [10, 0]], 12: [[13, 0], [10, 0], [11, 0]], 13: [[14, 0], [12, 0]], 14: [[16, 0], [15, 0], [13, 0]], 15: [[16, 0], [14, 0]], 16: [[18, 0], [17, 0], [14, 0], [15, 0]], 17: [[18, 0], [16, 0]], 18: [[20, 0], [19, 0], [16, 0], [17, 0]], 19: [[20, 0], [18, 0]], 20: [[22, 0], [21, 0], [18, 0], [19, 0]], 21: [[22, 0], [20, 0]], 22: [[24, 0], [23, 0], [20, 0], [21, 0]], 23: [[24, 0], [22, 0]], 24: [[26, 0], [25, 0], [22, 0], [23, 0]], 25: [[26, 0], [24, 0]], 26: [[28, 0], [27, 0], [24, 0], [25, 0]], 27: [[28, 0], [26, 0]], 28: [[30, 0], [29, 0], [26, 0], [27, 0]], 29: [[30, 0], [28, 0]], 30: [[32, 0], [31, 0], [28, 0], [29, 0]], 31: [[32, 0], [30, 0]], 32: [[34, 0], [33, 0], [30, 0], [31, 0]], 33: [[34, 0], [32, 0]], 34: [[36, 0], [35, 0], [32, 0], [33, 0]], 35: [[36, 0], [34, 0]], 36: [[38, 0], [37, 0], [34, 0], [35, 0]], 37: [[38, 0], [36, 0]], 38: [[40, 0], [39, 0], [36, 0], [37, 0]], 39: [[40, 0], [38, 0]], 40: [[42, 0], [41, 0], [38, 0], [39, 0]], 41: [[42, 0], [40, 0]], 42: [[44, 0], [43, 0], [40, 0], [41, 0]], 43: [[44, 0], [42, 0]], 44: [[46, 0], [45, 0], [42, 0], [43, 0]], 45: [[46, 0], [44, 0]], 46: [[48, 0], [47, 0], [44, 0], [45, 0]], 47: [[48, 0], [46, 0]], 48: [[50, 0], [49, 0], [46, 0], [47, 0]], 49: [[50, 0], [48, 0]], 50: [[52, 0], [51, 0], [48, 0], [49, 0]], 51: [[52, 0], [50, 0]], 52: [[54, 0], [53, 0], [50, 0], [51, 0]], 53: [[54, 0], [52, 0]], 54: [[56, 0], [55, 0], [52, 0], [53, 0]], 55: [[56, 0], [54, 0]], 56: [[58, 0], [57, 0], [54, 0], [55, 0]], 57: [[58, 0], [56, 0]], 58: [[60, 0], [59, 0], [56, 0], [57, 0]], 59: [[60, 0], [58, 0]], 60: [[62, 0], [61, 0], [58, 0], [59, 0]], 61: [[62, 0], [60, 0]], 62: [[64, 0], [63, 0], [60, 0], [61, 0]], 63: [[64, 0], [62, 0]], 64: [[66, 0], [65, 0], [62, 0], [63, 0]], 65: [[66, 0], [64, 0]], 66: [[68, 0], [67, 0], [64, 0], [65, 0]], 67: [[68, 0], [66, 0]], 68: [[70, 0], [69, 0], [66, 0], [67, 0]], 69: [[70, 0], [68, 0]], 70: [[72, 0], [71, 0], [68, 0], [69, 0]], 71: [[72, 0], [70, 0]], 72: [[74, 0], [73, 0], [70, 0], [71, 0]], 73: [[74, 0], [72, 0]], 74: [[76, 0], [75, 0], [72, 0], [73, 0]], 75: [[76, 0], [74, 0]], 76: [[78, 0], [77, 0], [74, 0], [75, 0]], 77: [[78, 0], [76, 0]], 78: [[80, 0], [79, 0], [76, 0], [77, 0]], 79: [[80, 0], [78, 0]], 80: [[82, 0], [81, 0], [78, 0], [79, 0]], 81: [[82, 0], [80, 0]], 82: [[84, 0], [83, 0], [80, 0], [81, 0]], 83: [[84, 0], [82, 0]], 84: [[86, 0], [85, 0], [82, 0], [83, 0]], 85: [[86, 0], [84, 0]], 86: [[88, 0], [87, 0], [84, 0], [85, 0]], 87: [[88, 0], [86, 0]], 88: [[90, 0], [89, 0], [86, 0], [87, 0]], 89: [[90, 0], [88, 0]], 90: [[92, 0], [91, 0], [88, 0], [89, 0]], 91: [[92, 0], [90, 0]], 92: [[94, 0], [93, 0], [90, 0], [91, 0]], 93: [[94, 0], [92, 0]], 94: [[96, 0], [95, 0], [92, 0], [93, 0]], 95: [[96, 0], [94, 0]], 96: [[98, 0], [97, 0], [94, 0], [95, 0]], 97: [[98, 0], [96, 0]], 98: [[100, 0], [99, 0], [96, 0], [97, 0]], 99: [[100, 0], [98, 0]], 100: [[98, 0], [99, 0]]}
#G={1: {2: 1}, 2: {1: 1, 3: 1}, 3: {2: 1}, 4: {5: 1}, 5: {4: 1, 6: 1}, 6: {5: 1}}

def dictiograph(graph): # create a dictionnaire for the graph - new data format
    dictiog = {}
    grnode = {}
    while len(graph)>0:
        link = graph.pop()
        a = link[0]
        b = link[1]
        if a in dictiog:
            grnode = dictiog[a]
            grnode[b] = 1
            #print "I", link, "a:", a, grnode
            dictiog[a] = grnode
            #print dictiog
        else:
            grnode = {}
            grnode[b] = 1
            #print "II", link, "a:", a, grnode
            dictiog[a] = grnode
            #print dictiog
        if b in dictiog:
            grnode = dictiog[b]
            grnode[a] = 1
            #print "III", link, "b:", b, grnode
            dictiog[b] = grnode
            #print dictiog
        else:
            grnode = {}
            grnode[a] = 1
            #print "IV", link, "b:", b, grnode
            dictiog[b] = grnode
            #print dictiog
    return dictiog

#graph = [(0,1),(1,2),(2,0)]
#print dictiograph(graph)

def mark_component(G, node, marked): #recursive solution
    #marked[node] = True
    total_marked = 0
    openlist = []
    openlist.append(node)
    while len(openlist) > 0:
        #print "openlist:", openlist
        tomark = openlist.pop()
        if tomark not in marked:
            marked[tomark] = True
            total_marked += 1
            tovisit = G[tomark]
            #print tomark, tovisit, "G:", G
            for entries in tovisit:
                openlist.append(entries)
    print marked
    return total_marked

#marked = {}
#print mark_component(G, 0, marked)

def count_nodes(G):
    print G
    a = 0
    for entry in G.keys():
        a += 1
    return a

def test_continuity(G):
    a = dictiograph(G) #dictionarize the graph!
    print "a:", a
    b = count_nodes(a)
    for entry in a.keys():
        marked = {}
        print entry
        c = mark_component(a, entry, marked)
        #print c
        #c = 101
        if c < b:
            return False #test fails!
        else:
            return True #needs only to loop first element!

#graph = [(0,1),(1,2),(2,3),(3,4)]
#graph = [(0,1),(1,2),(3,4)]
#print graph
#print test_continuity(graph)
#print count_nodes(dictiograph(graph))
#c = mark_component(graph, 0, marked)
#print c

def count_edge_degree(G):
    a = dictiograph(G)
    dictiocount = {}
    total_edges = 0
    for edges in a.keys():
        total_edges += 1
        b = a[edges]
        counter = 0
        for nodes in b:
            counter += 1
        dictiocount[edges] = counter
    return total_edges, dictiocount

graph = [(0,1),(1,2),(2,3),(3,4)]
#print count_edge_degree(graph)

def test_degree(G):
    a = count_edge_degree(G)
    b = a[1] #get the counted graph
    for edges in b.keys():
        c = b[edges]
        print c
        if c%2 == 1: return False
    return True

graph = [(0,1),(1,2),(2,3),(3,4),(4,0)]
print test_degree(graph)

def testkill(neighbors, start): #must evolute this one!
    print "neighbors:", neighbors, "start:", start
    a = 0
    for i in range (0, len(neighbors)):
        candidate = neighbors[i]
        if candidate[0] != start:
            if candidate[1] == 0: a=a+1
    if a == 0: return True #enter in kill process
    else: return a

def tweak_entry(dic, neighbors, node, start):
    for i in range(0, len(neighbors)): #hash in this node
        candidate = neighbors[i]
        if candidate[1] == 0: #a viable path was found
                if candidate[0] != start: #start clause here!
                    next = candidate[0]
                    candidate[1] = 1 #break visited link
                    neighbors[i] = candidate
                    dic[node] = neighbors #marked path in dic
                    newneighbors = dic[next] #mark next also in dic
                    for j in range(0, len(newneighbors)):
                        entry = newneighbors[j]
                        if entry[0] == node:
                            entry[1] = 1 #mark retronode
                            newneighbors[j] = entry
                    print 'new:', next, newneighbors
                    dic[next] = newneighbors
                    return [next, newneighbors]
                else:
                    if testkill(neighbors, start) == True: return True #termination signal
    return None

#must find the node to start (odd, or if all even, the larger even)
def find_eulerian_tour(graph, node=0):
    if test_continuity(graph) == FALSE: return None
    if test_degree(G) == FALSE: return None
    tour = []
    if len(graph) == 0: return tour #no-nodes case
    dic = dictiograph(graph)
    set = dic.keys()
    while node < len(set):
        if node in dic:
            start = node #mark the start node
            tour.append(node) #get this node
            neighbors = dic[node]
            while True:
                print node, dic
                if len(neighbors) > 0:
                    answer = tweak_entry(dic, neighbors, node, start)
                    if answer == None:
                        return tour #an dead-end was found
                    elif answer == True:
                        tour.append(start)
                        return tour
                    else:
                        tour.append(answer[0])
                        node = answer[0] #go to next node
                        neighbors = answer[1]
            return tour
        else:
            node = node + 1 #look for starting node
    return tour

#print find_eulerian_tour(graph)

def create_tour(nodes):
    #use_harder_tests = True
    graph = []
    tuple = (0,0)
    i = 0
    j = 0
    while i < len(nodes):
        j = 0
        while j < len(nodes):
            a = nodes[i]
            b = nodes[j]
            if a != b:
                tuple = (a,b)
                graph.append(tuple)
            j = j + 1
        i = i + 1
    return graph

#########

def get_degree(tour):
    degree = {}
    for x, y in tour:
        degree[x] = degree.get(x, 0) + 1
        degree[y] = degree.get(y, 0) + 1
    return degree

def check_edge(t, b, nodes):
    """
    t: tuple representing an edge
    b: origin node
    nodes: set of nodes already visited

    if we can get to a new node from `b` following `t`
    then return that node, else return None
    """
    if t[0] == b:
        if t[1] not in nodes:
            return t[1]
    elif t[1] == b:
        if t[0] not in nodes:
            return t[0]
    return None

def connected_nodes(tour):
    """return the set of nodes reachable from
    the first node in `tour`"""
    a = tour[0][0]
    nodes = set([a])
    explore = set([a])
    while len(explore) > 0:
        # see what other nodes we can reach
        b = explore.pop()
        for t in tour:
            node = check_edge(t, b, nodes)
            if node is None:
                continue
            nodes.add(node)
            explore.add(node)
    return nodes

def is_eulerian_tour(nodes, tour):
    # all nodes must be even degree
    # and every node must be in graph
    degree = get_degree(tour)
    for node in nodes:
        try:
            d = degree[node]
            if d % 2 == 1:
                print "Node %s has odd degree" % node
                return False
        except KeyError:
            print "Node %s was not in your tour" % node
            return False
    connected = connected_nodes(tour)
    if len(connected) == len(nodes):
        return True
    else:
        print "Your graph wasn't connected"
        return False

def test():
    nodes = [20, 21, 22, 23, 24, 25]
    tour = create_tour(nodes)
    return is_eulerian_tour(nodes, tour)


#nodes = [20, 21, 22, 23, 24, 25]
#print nodes[1]
#print create_tour(nodes)
#b= 12
#c = 24
#a = (b,c)
#print a
#print test()

