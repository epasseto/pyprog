#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="epasseto"
__date__ ="$27/12/2012 13:37:20$"

#Heap drives
def parent(i):
    return (i-1)/2 #returns -1 when in ROOT
def left_child(i):
    return 2*i+1
def right_child(i):
    return 2*i+2
def is_leaf(L,i):
    return (left_child(i) >= len(L)) and (right_child(i) >= len(L))
def one_child(L,i):
    return (left_child(i) < len(L)) and (right_child(i) >= len(L))
def up_heapify(L, i,control): #use this when you add one number to the end of the heap
    if parent(i) >= 0:
        print L[i][1]
        if L[i][1] < L[parent(i)][1]:
            L[i],L[parent(i)] = L[parent(i)],L[i]
            up_heapify(L,parent(i),control)
    control[L[i][0]] = i
'''H = [0, 1, 1, 2, 2, 3, 5, 2, 3, 6, 11]
i = 11
control = 1
H.append(i)
print up_heapify(H, i, control)'''

def down_heapify(L, i,control): #use this when you remove the top number of the heap (ROOT)
    if is_leaf(L, i):
        control[L[i][0]] = i
        return
    if one_child(L, i):
        if L[i][1] > L[left_child(i)][1]:
        (L[i], L[left_child(i)]) = (L[left_child(i)], L[i])
        control[L[i][0]] = i
        return
    if min(L[left_child(i)][1], L[right_child(i)][1]) >= L[i][1]:
        control[L[i][0]] = i
        return
    if L[left_child(i)][1] < L[right_child(i)][1]:
        (L[i], L[left_child(i)]) = (L[left_child(i)], L[i])
        down_heapify(L, left_child(i),control)
        control[L[i][0]] = i
        return
    else:
        (L[i], L[right_child(i)]) = (L[right_child(i)], L[i])
        down_heapify(L, right_child(i),control)
        control[L[i][0]] = i
        return

def shortest_dist_node(H,control):
    if H[0] == H[len(H)-1]:
        return H.pop()[0]
    best_node = H[0]
    H[0] = H.pop()
    down_heapify(H,0,control)
    return best_node[0]
H = [0, 1, 1, 2, 2, 3, 5, 2, 3, 6, 11]
control = 0
print shortest_dist_node(H,control)

def insert_heap(H,val,control):
    H.append(val)
    up_heapify(H,len(H)-1,control)

def update_heap(H,val,control):
    index = control[val[0]]
    H[index] = val
    down_heapify(H,index,control)

def dijkstra(G,v):
    H = []
    control = {}
    dist_so_far = {}
    dist_so_far[v] = 0
    insert_heap(H,(v,dist_so_far[v]),control)
    final_dist = {}
    while len(final_dist) < len(G):
        w = shortest_dist_node(H,control)
        final_dist[w] = dist_so_far[w]
        del dist_so_far[w]
        for x in G[w]:
            if x not in final_dist:
                if x not in dist_so_far:
                    dist_so_far[x] = final_dist[w] + G[w][x]
                    insert_heap(H,(x,dist_so_far[x]),control)
                elif final_dist[w] + G[w][x] < dist_so_far[x]:
                    dist_so_far[x] = final_dist[w] + G[w][x]
                    update_heap(H,(x,dist_so_far[x]),control)
    return final_dist

############
#
# Test

def make_link(G, node1, node2, w):
    if node1 not in G:
        G[node1] = {}
    if node2 not in G[node1]:
        (G[node1])[node2] = 0
    (G[node1])[node2] += w
    if node2 not in G:
        G[node2] = {}
    if node1 not in G[node2]:
        (G[node2])[node1] = 0
    (G[node2])[node1] += w
    return G

def test():
    # shortcuts
    (a,b,c,d,e,f,g) = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
    triples = ((a,c,3),(c,b,10),(a,b,15),(d,b,9),(a,d,4),(d,f,7),(d,e,3),
               (e,g,1),(e,f,5),(f,g,2),(b,f,1))
    G = {}
    for (i,j,k) in triples:
        make_link(G, i, j, k)

    dist = dijkstra(G, a)
    assert dist[g] == 8 #(a -> d -> e -> g)
    assert dist[b] == 11 #(a -> d -> e -> g -> f -> b)

    '''Your implementation has some issues. First, all the heap operations should have O(log(N)) complexity. This is not the case in your implementation. The code you use to change the weight (or cost) of a node in the heap is O(N) due to this line of code:
                 del H[control[x]]
Removing an arbitrary element inside an array is O(N).
You can solve this problem by simply replacing the following 4 lines of code:
                del H[control[x]]
                del control[x]
                H.append((x,dist_so_far[x]))
                up_heapify(H,len(H)-1,control)
by these lines:
               H[control[x]] = (x,dist_so_far[x])
               up_heapify(H,control[x],control)
In addition to the complexity problem I think that your implementation is not correct since deleting an element inside a heap as you do and reinserting it at the end followed by a up_heapify is not enough to restore the heap invariant.
From a structural point of view, I think it is better to hide all the heap operations behind a priority queue abstraction. This priority queue would of course be implemented with a heap and would offer a clear separation of concerns between the heap manipulation and the Dijstra Algorithm.'''
