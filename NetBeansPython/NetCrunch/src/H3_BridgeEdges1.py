#from numpy.numarray.session import keys
#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="epasseto"
__date__ ="$11/09/2012 10:56:13$"
# Bridge Edges v4
# Find the bridge edges in a graph given the algorithm in lecture.
# Complete the intermediate steps
#  - create_rooted_spanning_tree
#  - post_order (I)
#  - number_of_descendants (II)
#  - lowest_post_order (III)
#  - highest_post_order (IV)
#
# And then combine them together in `bridge_edges`
#
# So far, we've represented graphs as a dictionary where G[n1][n2] == 1
# meant there was an edge between n1 and n2
#
# In order to represent a spanning tree we need to create two classes of edges
# we'll refer to them as "green" and "red" for the green and red edges as specified in lecture
#
# So, for example, the graph given in lecture
# G = {'a': {'c': 1, 'b': 1},
#      'b': {'a': 1, 'd': 1},
#      'c': {'a': 1, 'd': 1},
#      'd': {'c': 1, 'b': 1, 'e': 1},
#      'e': {'d': 1, 'g': 1, 'f': 1},
#      'f': {'e': 1, 'g': 1},
#      'g': {'e': 1, 'f': 1}
#      }
# would be written as a spanning tree
# S = {'a': {'c': 'green', 'b': 'green'},
#      'b': {'a': 'green', 'd': 'red'},
#      'c': {'a': 'green', 'd': 'green'},
#      'd': {'c': 'green', 'b': 'red', 'e': 'green'},
#      'e': {'d': 'green', 'g': 'green', 'f': 'green'},
#      'f': {'e': 'green', 'g': 'red'},
#      'g': {'e': 'green', 'f': 'red'}
#      }
#
# reached list
# R = { a : True, b : True, c : True, d : True, e : True, f : True }
#
G = {'a': {'c': 1, 'b': 1}, 'b': {'a': 1, 'd': 1}, 'c': {'a': 1, 'd': 1}, 'd': {'c': 1, 'b': 1, 'e': 1}, 'e': {'d': 1, 'g': 1, 'f': 1}, 'f': {'e': 1, 'g': 1}, 'g': {'e': 1, 'f': 1}}

def create_rooted_spanning_tree(G, root):
    S = {}
    R = {}
    open_list = [root] #we will start here
    while len(open_list) > 0:
        node = open_list.pop()
        print "Node", node
        R[node] = True
        search_in = G[node]
        dictree = {}
        for entries in search_in.keys():
            print entries
            if entries in R:
                print "TRUE"
                if entries in S:
                    verigreen = S[entries]
                    print "verigreen", entries, verigreen
                    if node in verigreen:
                        if verigreen[node] == 'green':
                            dictree[entries] = 'green' #save this one of being red
                            continue #recicle
                dictree[entries] = 'red' #for a node that was almost reached
            else:
                print "FALSE"
                dictree[entries] = 'green' #for a node not untill reached
                open_list.append(entries)
                R[entries] = True
        S[node] = dictree
    print "Reached", R
    print "Tree", S
    return S

#print create_rooted_spanning_tree(G, 'a')
# This is just one possible solution. There are other ways to create a
# spanning tree, and the grader will accept any valid result
# feel free to edit the test to match the solution your program produces
def test_create_rooted_spanning_tree():
    G = {'a': {'c': 1, 'b': 1},
         'b': {'a': 1, 'd': 1},
         'c': {'a': 1, 'd': 1},
         'd': {'c': 1, 'b': 1, 'e': 1},
         'e': {'d': 1, 'g': 1, 'f': 1},
         'f': {'e': 1, 'g': 1},
         'g': {'e': 1, 'f': 1}
         }
    S = create_rooted_spanning_tree(G, "a")
    assert S == {'a': {'c': 'green', 'b': 'green'},
                 'b': {'a': 'green', 'd': 'red'},
                 'c': {'a': 'green', 'd': 'green'},
                 'd': {'c': 'green', 'b': 'red', 'e': 'green'},
                 'e': {'d': 'green', 'g': 'green', 'f': 'green'},
                 'f': {'e': 'green', 'g': 'red'},
                 'g': {'e': 'green', 'f': 'red'}
                 }
###########

def reachable(S, root):
    visited = {}
    open_list = [root]
    visited[root] = True
    while len(open_list) > 0:
        current = open_list[0] #BFS
        del open_list[0]
        food = [] 
        meat = S[current]
        guys = meat.keys()
        #print current, meat, guys
        for element in guys:
            if meat[element] == 'green': food.append(element) #get only the green ones!
        #print 'food', food
        for neighbor in food:
            if neighbor not in visited:
                open_list.append(neighbor)
                visited[neighbor] = True
    return len(visited)

#S = {'a': {'c': 'green', 'b': 'green'}, 'b': {'a': 'green', 'd': 'red'}, 'c': {'a': 'green', 'd': 'green'}, 'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 'f': {'e': 'green', 'g': 'red'}, 'g': {'e': 'green', 'f': 'red'}}
#print reachable(S, 'a')

def post_order(S, root): #(I) - with only one cycle!
    nnodes = reachable(S, root) #find number of reachable nodes
    po = {} #this is the post order dic
    #print root, S
    #S2 = dict(S) #I will delete elements after labelling - del S2[node]
    index = 1
    cycle = True #this is the cycle flag
    while cycle == True:
        open_list = [root]
        visited = {}
        visited[root] = True
        while len(open_list) > 0:
            current = open_list[0] #breadth-first search
            del open_list[0]
            neighborhood = S[current].keys()
            food = [] #only search for green nodes
            for neighbor in neighborhood:
                guys = S[current]
                color = guys[neighbor]
                #print current, "Neighbor:", neighbor, color, visited
                if color == 'green' and neighbor not in visited and neighbor not in po:
                    food.append(neighbor)
            print 'food:', food
            if len(food) == 0: #an endpoit was found
                po[current] = index
                index += 1
                continue #recycle
            while len(food) > 0:
                meat = food.pop()
                if meat not in visited:
                    open_list.append(meat)
                    visited[meat] = True
        #print po
        if nnodes == len(po): cycle = False #stop cycling when all nodes were labeled
    return po

#S = {'a': {'c': 'green', 'b': 'green'}, 'b': {'a': 'green', 'd': 'red'}, 'c': {'a': 'green', 'd': 'green'}, 'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 'f': {'e': 'green', 'g': 'red'}, 'g': {'e': 'green', 'f': 'red'}}
#print post_order(S, 'a')

# This is just one possible solution. There are other ways to create a
# spanning tree, and the grader will accept any valid result.
# feel free to edit the test to match the solution your program produces
def test_post_order():
    S = {'a': {'c': 'green', 'b': 'green'},
         'b': {'a': 'green', 'd': 'red'},
         'c': {'a': 'green', 'd': 'green'},
         'd': {'c': 'green', 'b': 'red', 'e': 'green'},
         'e': {'d': 'green', 'g': 'green', 'f': 'green'},
         'f': {'e': 'green', 'g': 'red'},
         'g': {'e': 'green', 'f': 'red'}
         }
    po = post_order(S, 'a')
    assert po == {'a':7, 'b':1, 'c':6, 'd':5, 'e':4, 'f':2, 'g':3}

##############

def descendants_of_node(S, node, visited={}): #num of descendants of ONE node
    open_list = [node]
    visited2 = dict(visited) #I copy the visited dic
    visited2[node] = True #may check if is necessary
    print S
    print visited2
    #print "visited2", visited2
    #visited2[node] = True #verify if is necessary
    descendants = 1
    while len(open_list) > 0:
        current = open_list[0] #BFS
        del open_list[0] #not reach red connections
        neighborhood = S[current].keys()
        food = [] #only search for green nodes
        for neighbor in neighborhood:
            guys = S[current]
            color = guys[neighbor]
            print current, "Neighbor:", neighbor, color, visited2
            if color == 'green' and neighbor not in visited2:
                food.append(neighbor)
        print current, 'food:', food
        while len(food) > 0:
            meat = food.pop()
            if meat not in visited2:
                open_list.append(meat)
                visited2[meat] = True
                descendants += 1
                print current, "meat", meat, "descentants", descendants
    print node, "descendants", descendants
    print "visited2 final", visited2
    return descendants

#S = {'a': {'c': 'green', 'b': 'green'}, 'b': {'a': 'green', 'd': 'red'}, 'c': {'a': 'green', 'd': 'green'}, 'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 'f': {'e': 'green', 'g': 'red'}, 'g': {'e': 'green', 'f': 'red'}}
#print descendants_of_node(S, 'a')

def number_of_descendants(S, root): #self counts as 1 descendant
    open_list = [root] #need to call descendants_of_node
    nd = {}
    visited = {}
    nd[root] = descendants_of_node(S, root)
    visited[root] = True
    while len(open_list) > 0:
        current = open_list[0] #BFS
        del open_list[0] #not reach red connections
        neighborhood = S[current].keys()
        food = [] #only search for green nodes
        for neighbor in neighborhood:
            guys = S[current]
            color = guys[neighbor]
            print current, "Neighbor:", neighbor, color, visited
            if color == 'green' and neighbor not in visited:
                food.append(neighbor)
        print current, 'food:', food
        while len(food) > 0:
            meat = food.pop()
            if meat not in visited:
                open_list.append(meat)
                nd[meat] = descendants_of_node(S, meat, visited)
                visited[meat] = True
                print current, "meat", meat
    print "visited final", visited
    return nd

#S = {'a': {'c': 'green', 'b': 'green'}, 'b': {'a': 'green', 'd': 'red'}, 'c': {'a': 'green', 'd': 'green'}, 'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 'f': {'e': 'green', 'g': 'red'}, 'g': {'e': 'green', 'f': 'red'}}
#print number_of_descendants(S, 'a')

def test_number_of_descendants():
    S =  {'a': {'c': 'green', 'b': 'green'},
          'b': {'a': 'green', 'd': 'red'},
          'c': {'a': 'green', 'd': 'green'},
          'd': {'c': 'green', 'b': 'red', 'e': 'green'},
          'e': {'d': 'green', 'g': 'green', 'f': 'green'},
          'f': {'e': 'green', 'g': 'red'},
          'g': {'e': 'green', 'f': 'red'}
          }
    nd = number_of_descendants(S, 'a')
    assert nd == {'a':7, 'b':1, 'c':5, 'd':4, 'e':3, 'f':1, 'g':1}

###############

def find_lowest_node(S, root, po):
    orderval = po[root]
    if orderval == 1: return root #lowest is root
    open_list = [root]
    visited = {}
    visited[root] = True
    while len(open_list) > 0:
        current = open_list[0] #BFS
        del open_list[0]
        for neighbor in S[current].keys():
            if po[neighbor] == 1: return neighbor
            if neighbor not in visited:
                open_list.append(neighbor)
                visited[neighbor] = True
    return None

#S = {'a': {'c': 'green', 'b': 'green'}, 'b': {'a': 'green', 'd': 'red'}, 'c': {'a': 'green', 'd': 'green'}, 'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 'f': {'e': 'green', 'g': 'red'}, 'g': {'e': 'green', 'f': 'red'}}
#po = {'a':7, 'b':1, 'c':6, 'd':5, 'e':4, 'f':2, 'g':3}
#print find_lowest_node(S, 'a', po)

def low_red_propagation(S, node):
    propagation = [] #all nodes in red
    if node in S: neighborhood = S[node] #test before picking it
    else: return None
    for node in neighborhood:
        if neighborhood[node] == 'red': propagation.append(node)
    return propagation

#S = {'a': {'c': 'green', 'b': 'green'}, 'b': {'a': 'green', 'd': 'red'}, 'c': {'a': 'green', 'd': 'green'}, 'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 'f': {'e': 'green', 'g': 'red'}, 'g': {'e': 'green', 'f': 'red'}}
#po = {'a':7, 'b':1, 'c':6, 'd':5, 'e':4, 'f':2, 'g':3}
#print low_red_propagation(S, 'b', po)

def direct_parent_heritage(S, root, node): #return direct heritage of one node
    directheritage = []
    open_list = [root]
    visited = {}
    visited[root] = True
    terminate = False
    while len(open_list) > 0:
        current = open_list[0] #BFS
        del open_list[0]
        if current == node: terminate = True
        #neighborhood = S[current].keys()
        crunchies = S[current]
        #print current, 'current', crunchies
        for biscuit in crunchies.keys():
            if biscuit not in visited and crunchies[biscuit] == 'green':
                if terminate == True: directheritage.append(biscuit)
                open_list.append(biscuit)
                visited[biscuit] = True
        if terminate == True: return directheritage
    return None

#S = {'a': {'c': 'green', 'b': 'green'}, 'b': {'a': 'green', 'd': 'red'}, 'c': {'a': 'green', 'd': 'green'}, 'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 'f': {'e': 'green', 'g': 'red'}, 'g': {'e': 'green', 'f': 'red'}}
#print direct_parent_heritage(S, 'a', 'b')

def leaf(S, root, dont_visit): #DFS
    if root in dont_visit: return None
    open_list = [root]
    visited = {}
    visited[root] = True
    while len(open_list) > 0:
        pick = len(open_list) - 1 #DFS
        current = open_list[pick]
        del open_list[pick]
        crunchies = S[current]
        to_visit = []
        for biscuit in crunchies.keys():
            if biscuit not in visited and crunchies[biscuit] == 'green' and biscuit not in dont_visit:
                to_visit.append(biscuit)
                visited[biscuit] = True
        print current, 'current', crunchies, to_visit, dont_visit
        if len(to_visit) == 0: return current
        else:
            while len(to_visit) > 0:
                guy = to_visit.pop()
                open_list.append(guy)
    return None

#S = {'a': {'c': 'green', 'b': 'green'}, 'b': {'a': 'green', 'd': 'red'}, 'c': {'a': 'green', 'd': 'green'}, 'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 'f': {'e': 'green', 'g': 'red'}, 'g': {'e': 'green', 'f': 'red'}}
#dont_visit = {'g': True, 'f': True, 'e': True, 'd': True, 'b': True, 'c': True, 'a': True}
#print leaf(S, 'a', dont_visit)

def node_order(S, root, node): #return better order for the node
    return None

def lowest_post_order(S, root, po):
    l = {}
    while len(S.keys())> len(l.keys()): #low green propagation
        node = leaf(S, root, l)
        x = po[node]
        kids = direct_parent_heritage(S, root, node)
        if len(kids) == 0:
            l[node] = x #no kids!
        else:
            valkids = []
            for kid in kids:
                valkids.append(l[kid])
            if min(valkids) > x:
                l[node] = x
            else:
                l[node] = min(valkids)
    for node in S.keys(): #low red propagation
        greenvalue = l[node]
        rednodes = low_red_propagation(S, node)
        if len(rednodes) > 0:
            redvalues = []
            for rednode in rednodes:
                redvalues.append(l[rednode])
            redvalue = min(redvalues)
            if redvalue < greenvalue: l[node] = redvalue  
    return l

S = {'a': {'c': 'green', 'b': 'green'}, 'b': {'a': 'green', 'd': 'red'}, 'c': {'a': 'green', 'd': 'green'}, 'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 'f': {'e': 'green', 'g': 'red'}, 'g': {'e': 'green', 'f': 'red'}}
po = {'a':7, 'b':1, 'c':6, 'd':5, 'e':4, 'f':2, 'g':3}
print lowest_post_order(S, 'a', po)

def test_lowest_post_order():
    S = {'a': {'c': 'green', 'b': 'green'},
         'b': {'a': 'green', 'd': 'red'},
         'c': {'a': 'green', 'd': 'green'},
         'd': {'c': 'green', 'b': 'red', 'e': 'green'},
         'e': {'d': 'green', 'g': 'green', 'f': 'green'},
         'f': {'e': 'green', 'g': 'red'},
         'g': {'e': 'green', 'f': 'red'}
         }
    po = post_order(S, 'a')
    l = lowest_post_order(S, 'a', po)
    assert l == {'a':1, 'b':1, 'c':1, 'd':1, 'e':2, 'f':2, 'g':2}

################

def highest_post_order(S, root, po):
    # return a mapping of the nodes in S to the highest post order value
    # below that node (and you're allowed to follow 1 red edge)
    pass

def test_highest_post_order():
    S = {'a': {'c': 'green', 'b': 'green'},
         'b': {'a': 'green', 'd': 'red'},
         'c': {'a': 'green', 'd': 'green'},
         'd': {'c': 'green', 'b': 'red', 'e': 'green'},
         'e': {'d': 'green', 'g': 'green', 'f': 'green'},
         'f': {'e': 'green', 'g': 'red'},
         'g': {'e': 'green', 'f': 'red'}
         }
    po = post_order(S, 'a')
    h = highest_post_order(S, 'a', po)
    assert h == {'a':7, 'b':5, 'c':6, 'd':5, 'e':4, 'f':3, 'g':3}

#################

def bridge_edges(G, root):
    # use the four functions above and then determine which edges in G are bridge edges
    # return them as a list of tuples ie: [(n1, n2), (n4, n5)]
    pass

def test_bridge_edges():
    G = {'a': {'c': 1, 'b': 1},
         'b': {'a': 1, 'd': 1},
         'c': {'a': 1, 'd': 1},
         'd': {'c': 1, 'b': 1, 'e': 1},
         'e': {'d': 1, 'g': 1, 'f': 1},
         'f': {'e': 1, 'g': 1},
         'g': {'e': 1, 'f': 1}
         }
    bridges = bridge_edges(G, 'a')
    assert bridges == [('d', 'e')]

"""
Python never implicitly copies objects. When you set dict2 = dict1, you are making them refer to the same exact dict object, so when you mutate it, all references to it keep referring to the object in its current state.
If you want to copy the dict (which is rare), you have to do so explicitly with
dict2 = dict(dict1) or dict2 = dict1.copy()
"""
