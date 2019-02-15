#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="epasseto"
__date__ ="$19/11/2012 16:40:59$"

#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="epasseto"
__date__ ="$19/11/2012 15:20:00$"

#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="epasseto"
__date__ ="$13/11/2012 14:30:10$"

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
#G = {'a': {'c': 1, 'b': 1}, 'b': {'a': 1, 'd': 1}, 'c': {'a': 1, 'd': 1}, 'd': {'c': 1, 'b': 1, 'e': 1}, 'e': {'d': 1, 'g': 1, 'f': 1}, 'f': {'e': 1, 'g': 1}, 'g': {'e': 1, 'f': 1}}

def create_rooted_spanning_tree(G, root):
    S = {}
    R = {}
    open_list = [root] #we will start here
    while len(open_list) > 0:
        node = open_list.pop()
        #print "Node", node
        R[node] = True
        search_in = G[node]
        dictree = {}
        for entries in search_in.keys():
            #print entries
            if entries in R:
                #print "TRUE"
                if entries in S:
                    verigreen = S[entries]
                    #print "verigreen", entries, verigreen
                    if node in verigreen:
                        if verigreen[node] == 'green':
                            dictree[entries] = 'green' #save this one of being red
                            continue #recicle
                dictree[entries] = 'red' #for a node that was almost reached
            else:
                #print "FALSE"
                dictree[entries] = 'green' #for a node not untill reached
                open_list.append(entries)
                R[entries] = True
        S[node] = dictree
    #print "Reached", R
    #print "Tree", S
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

#print test_create_rooted_spanning_tree()

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
            #print 'food:', food
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

#print test_post_order()

##############

def descendants_of_node(S, node, visited={}): #num of descendants of ONE node
    open_list = [node]
    visited2 = dict(visited) #I copy the visited dic
    visited2[node] = True #may check if is necessary
    #print S
    #print visited2
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
            #print current, "Neighbor:", neighbor, color, visited2
            if color == 'green' and neighbor not in visited2:
                food.append(neighbor)
        #print current, 'food:', food
        while len(food) > 0:
            meat = food.pop()
            if meat not in visited2:
                open_list.append(meat)
                visited2[meat] = True
                descendants += 1
                #print current, "meat", meat, "descentants", descendants
    #print node, "descendants", descendants
    #print "visited2 final", visited2
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
            #print current, "Neighbor:", neighbor, color, visited
            if color == 'green' and neighbor not in visited:
                food.append(neighbor)
        #print current, 'food:', food
        while len(food) > 0:
            meat = food.pop()
            if meat not in visited:
                open_list.append(meat)
                nd[meat] = descendants_of_node(S, meat, visited)
                visited[meat] = True
                #print current, "meat", meat
    #print "visited final", visited
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

#print test_number_of_descendants()

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

def direct_lienage(S, root, node, never_visit):
    if node == root: return [root]
    else:
        path = [root]
        open_list = [root]
        hash = {}
        hash[root] = True
        while len(open_list) > 0:
            pick = len(open_list)-1 #DFS
            current = open_list[pick]
            del open_list[pick]
            neighborhood = S[current].keys()
            colors = S[current]
            for neighbor in neighborhood:
                color = colors[neighbor]
                if neighbor not in hash and neighbor not in never_visit and color == 'green':
                    path.append(neighbor)
                    if neighbor == node: return True, path
                    open_list.append(neighbor)
                    hash[neighbor] = True
                    break #I want only one sunray!
    never = path.pop()
    return None, never

#S = {'a': {'c': 'green', 'b': 'green'}, 'b': {'a': 'green', 'd': 'red'}, 'c': {'a': 'green', 'd': 'green'}, 'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 'f': {'e': 'green', 'g': 'red'}, 'g': {'e': 'green', 'f': 'red'}}
#never_visit = {'g': True, 'f': True, 'e': True, 'd': True, 'c': True}
#print direct_lienage(S, 'a', 'b', never_visit)

def find_lineage(S, root, node, never_visit = {}):
    x = direct_lienage(S, root, node, never_visit)
    if x[0] == True: return x[1]
    else:
        never = x[1]
        never_visit[never] = True
        return find_lineage(S, root, node, never_visit)

#S = {'a': {'c': 'green', 'b': 'green'}, 'b': {'a': 'green', 'd': 'red'}, 'c': {'a': 'green', 'd': 'green'}, 'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 'f': {'e': 'green', 'g': 'red'}, 'g': {'e': 'green', 'f': 'red'}}
#print find_lineage(S, 'a', 'e')

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
    tested = {}
    tested[root] = True
    terminate = False
    while len(open_list) > 0:
        current = open_list[0] #BFS
        del open_list[0]
        if current == node: terminate = True
        #neighborhood = S[current].keys()
        crunchies = S[current]
        #print current, 'current', crunchies
        for biscuit in crunchies.keys():
            if biscuit not in tested and crunchies[biscuit] == 'green':
                if terminate == True: directheritage.append(biscuit)
                open_list.append(biscuit)
                tested[biscuit] = True
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
        #print current, 'current', crunchies, to_visit, dont_visit
        if len(to_visit) == 0: return current
        else:
            while len(to_visit) > 0:
                guy = to_visit.pop()
                open_list.append(guy)
    return None

#S = {'a': {'c': 'green', 'b': 'green'}, 'b': {'a': 'green', 'd': 'red'}, 'c': {'a': 'green', 'd': 'green'}, 'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 'f': {'e': 'green', 'g': 'red'}, 'g': {'e': 'green', 'f': 'red'}}
#dont_visit = {'g': True, 'f': True, 'e': True, 'd': True, 'b': True, 'c': True, 'a': True}
#print leaf(S, 'a', dont_visit)

def lowredify(nodeval, rednodes, l):
    for node in rednodes:
        if node not in l:
            l[node] = nodeval
        else:
            if nodeval < l[node]: l[node] = nodeval
    return len(rednodes)

def lowgreenify(nodeval, lineage, l):
    for node in lineage:
        if node not in l:
            l[node] = nodeval
        else:
            if nodeval < l[node]: l[node] = nodeval
    return len(lineage)

def find_order_node(po, order):
    for node in po.keys():
        if po[node] == order: return node
    return None

#po = {'a':7, 'b':1, 'c':6, 'd':5, 'e':4, 'f':2, 'g':3}
#print find_order_node(po, 7)

def lowest_post_order(S, root, po):
    l = {}
    #print l
    #l = {'a': 1, 'c': 1, 'b': 1, 'd': 1}
    nodeval = 1
    degrees = len(S.keys())
    #print degrees
    while nodeval < degrees:
        node = find_order_node(po, nodeval)
        #print "node:", node
        rednodes = low_red_propagation(S, node)
        #print "red propagation:", rednodes
        lineage = find_lineage(S, root, node, {}) #this is for the green lineage!
        #print "direct lineage:", lineage, "rednodes:", rednodes
        while len(rednodes) > 0:
            rnode = rednodes.pop()
            lineagered = find_lineage(S, root, rnode, {})
            #print "red lineage:", lineagered
            lineage = lineage + list(set(lineagered) - set(lineage))
        #print "lineagetotal", lineage
        for node in lineage:
            #print node, l
            if node not in l:
                l[node] = nodeval #fill with values
        if len(l.keys()) == degrees: return l
        nodeval += 1
        #print nodeval, "cycle"
    return l

#S = {'a': {'c': 'green', 'b': 'green'}, 'b': {'a': 'green', 'd': 'red'}, 'c': {'a': 'green', 'd': 'green'}, 'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 'f': {'e': 'green', 'g': 'red'}, 'g': {'e': 'green', 'f': 'red'}}
#po = {'a':7, 'b':1, 'c':6, 'd':5, 'e':4, 'f':2, 'g':3}
#print lowest_post_order(S, 'a', po)

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

#print test_lowest_post_order()

################

def highest_post_order(S, root, po):
    h = {}
    nodes = S.keys()
    for node in nodes:
        orderval = po[node]
        bypass = low_red_propagation(S, node)
        #print orderval, node, "node", orderval, bypass
        if len(bypass) == 0: #no red messes
            h[node] = orderval
            #print h
            continue
        altvalues = []
        while len(bypass) > 0:
            guy = bypass.pop()
            altvalue = po[guy]
            #print "altvalue:", altvalue
            altvalues.append(altvalue)
        maximum = max(altvalues)
        if maximum > orderval: h[node] = maximum
        else: h[node] = orderval
        #print orderval, node, "altvalues:", altvalues, maximum, h
    return h

#S = {'a': {'c': 'green', 'b': 'green'}, 'b': {'a': 'green', 'd': 'red'}, 'c': {'a': 'green', 'd': 'green'}, 'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 'f': {'e': 'green', 'g': 'red'}, 'g': {'e': 'green', 'f': 'red'}}
#po = {'a':7, 'b':1, 'c':6, 'd':5, 'e':4, 'f':2, 'g':3}
#print highest_post_order(S, 'a', po)

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

#print test_highest_post_order()

#################

def bridge_edges(G, root):
    Suspects = []
    Bridges = []
    #1 create spanning tree
    Tree = create_rooted_spanning_tree(G, root)
    #print 'tree:', Tree
    #2 create the four bridge parameters
    Order = post_order(Tree, root)
    #print 'po:', Order
    Descendants = number_of_descendants(Tree, root)
    #print 'nd:', Descendants
    Lowest = lowest_post_order(Tree, root, Order)
    #print 'l:', Lowest
    Highest = highest_post_order(Tree, root, Order)
    #print 'h:', Highest
    #3 collect information from nodes
    for Node in Tree:
        if Node == root: continue #ignore the root node!
        H = Highest[Node]
        O = Order[Node]
        L = Lowest[Node]
        D = Descendants[Node]
        #print Node, 'node:', O, D, L, H
    #4 get suspect nodes
        if H <= O and L > abs(D - O): Suspects.append(Node)
    #print Suspects
    if len(Suspects) == 0: return None
    while len(Suspects) > 0:
        Guy = Suspects.pop() #get one by one
        Lineage = find_lineage(Tree, root, Guy, {})
        #print Guy, 'Guy', Lineage
        Bridges.append((Lineage[len(Lineage)-2],Guy))
    # return them as a list of tuples ie: [(n1, n2), (n4, n5)]
    return Bridges

#G = {'a': {'c': 1, 'b': 1}, 'b': {'a': 1, 'd': 1}, 'c': {'a': 1, 'd': 1}, 'd': {'c': 1, 'b': 1, 'e': 1}, 'e': {'d': 1, 'g': 1, 'f': 1}, 'f': {'e': 1, 'g': 1}, 'g': {'e': 1, 'f': 1}}
#print bridge_edges(G, 'a')

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

#print test_bridge_edges()

"""
Python never implicitly copies objects. When you set dict2 = dict1, you are making them refer to the same exact dict object, so when you mutate it, all references to it keep referring to the object in its current state.
If you want to copy the dict (which is rare), you have to do so explicitly with
dict2 = dict(dict1) or dict2 = dict1.copy()
"""

import itertools
# Find Eulerian Tour
#
# Write a function that takes in a graph
# represented as a list of tuples
# and return a list of nodes that
# you would follow on an Eulerian Tour
#
# For example, if the input graph was
#graph = [(1, 2), (2, 3), (3, 1)]
# A possible Eulerian tour would be [1, 2, 3, 1]
#graph = [(0, 1), (1, 5), (1, 7), (4, 5), (4, 8), (1, 6), (3, 7), (5, 9), (2, 4), (0, 4), (2, 5), (3, 6), (8, 9)] #failure!
#graph = [(1, 13), (1, 6), (6, 11), (3, 13), (8, 13), (0, 6), (8, 9),(5, 9), (2, 6), (6, 10), (7, 9), (1, 12), (4, 12), (5, 14), (0, 1), (2, 3), (4, 11), (6, 9), (7, 14), (10, 13)]
graph = [(8, 16), (8, 18), (16, 17), (18, 19), (3, 17), (13, 17), (5, 13),(3, 4), (0, 18), (3, 14), (11, 14), (1, 8), (1, 9), (4, 12), (2, 19),(1, 10), (7, 9), (13, 15), (6, 12), (0, 1), (2, 11), (3, 18), (5, 6), (7, 15), (8, 13), (10, 17)]
#control = [1,1,1]
#ex = itertools.compress(graph, control)
#for i in ex:
#    print i

def dictiograph(graph): # create a dictionnaire for the graph
    dictiog = {}
    while len(graph)>0:
        link = graph.pop()
        a = link[0]
        b = link[1]
        if a in dictiog:
            c = dictiog[a]
            c.append([b,0]) #0 is for an unvisited path
            dictiog[a] = c
        else:
            dictiog[a] = [[b,0]]
        if b in dictiog:
            c = dictiog[b]
            c.append([a,0])
            dictiog[b] = c
        else:
            dictiog[b] = [[a,0]]
    return dictiog

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

print find_eulerian_tour(graph)
