####---------------Things I was already familiar with-------------------####

#####--Abstract Data Types--######

Stack: LIFO(Last in, First Out) container with push(add element) and pop(remove last element added) properties
Queue: FIFO(First in, First Out) container with enque(add to end of queue) and dequeue(remove from front)
Deque: Elements can be added to front/back.
Double-ended Heap: Similar to priority queue but offers efficient removal of min/max values.
    Removal in asc/desc order is possible.


#####--Data structures--#####

Array: container for elements, generally of same type, with specific order and element access via integer index
Tuple: Ordered group of elements 
Map: associative array or a dict, unordered
Tree: hierarchical tree with root value and parent/child nodes
List: sequence of elements that allows for duplicates
Set: no order or duplicates, generally used for membership testing
Graph: finite set of nodes and vertices
Heap: partially sorted binary tree, priority queue(abstract data type)
      nodes conform to sorting pattern such as min or max heap 
      where each node has a value less/greater than its child.
      complete tree(every level filled)
Binary Tree: tree structure where each node has at most two children

#####--Asymptotic Running Times--#####

O(1)            Constant            Hash table lookup, modification 

O(lgn)          Logarithmic         Binary search

O(n)            Loglinear           Iterating over list

O(n lg n)       Loglinear           Optimal sorting of abrtitrary values; same as (O(log n!))

O(n^2)          Quadratic           Comparing n objects to each other

O(n^3)          Cubic               Floyd and Warshalls algorithm (shortest paths with +/- edge weights, no cycles)

O(n^k)          Polynomial          k nested loops over n (if k > 0)

Ω(k^n)          Exponential         All subsets of n items for any k > 1 
    
O(n!)           Factorial           Producing every ordering of n values


#####--Graphs and Trees--#####

- A graph G = (V, E) consists of a set of nodes, V, and edges between them, E. If the
edges have a direction, we say the graph is directed.

- Nodes with an edge between them are adjacent. The edge is then incident to both.
The nodes that are adjacent to v are the neighbors of v.

- A subgraph of G = (V, E) consists of a subset of V and a subset of E. A path in G is a
subgraph where the edges connect the nodes in a sequence, without revisiting any
node. A cycle is like a path, except that the last edge links the last node to the first.

- If we associate a weight with each edge in G, we say that G is a weighted graph. The
length of a path or cycle is the sum of its edge weights, or, for unweighted graphs,
simply the number of edges.

- A forest is a cycle-free graph, and a connected graph is a tree. In other words, a
forest consists of one or more trees.


#Finding eulerian tour in graph

graph = ([(1, 13), (1, 6), (6, 11), (3, 13),
(8, 13), (0, 6), (8, 9),(5, 9), (2, 6), (6, 10), (7, 9),
(1, 12), (4, 12), (5, 14), (0, 1),  (2, 3), (4, 11), (6, 9),
(7, 14),  (10, 13)])

def find_eulerian_tour(graph):
    tour = []
    current_vertex = graph[0][0]
    tour.append(current_vertex)
    while len(graph) > 0:
        for edge in graph:
            if current_vertex in edge:
                if edge[0] == current_vertex:
                    current_vertex = edge[1]
                else:
                    current_vertex = edge[0]
                graph.remove(edge)
                tour.append(current_vertex)
                break 
        else:
            break
    return tour

#Recursive russian peasant algorithm for multiplication

def rec_russian(a, b):
    if a == 0:
        return 0
    if a % 2 == 0:
        return 2 * rec_russian(a/2, b)
    return b + 2 * rec_russian((a - 1) / 2, b)

#Finding neighbors 
def get_neighbors(graph):
    g = {}
    for x, y in graph:
        g.setdefault(x, set()).add(y)
        g.setdefault(y, set()).add(x)
    return g

#Traversing graph, finding path (traversal==skeleton key)
def find_path(g, st, end, path=[]):
        path = path + [st]
        if st == end:
            return path
        if not g.has_key(st):
            return None
        for node in g[s]:
            if node not in path:
                newpath = find_path(g, node, end, path)
                if newpath: 
                    return newpath
        return None

#Walking (traversal) through connected components
def walk(G, s, S=set()): #Walk the graph from node s
    #Predecessors + "to do" queue
    P, Q = dict(), set()
    #s has no predecessor
    P[s] = None
    #We plan on starting with s
    Q.add(s)
    #Still nodes to visit
    while Q:
        #Pick one, arbitrarily
        u = Q.pop()
        #New nodes?
        for v in G[u].difference(P, S):
            #We plan to visit them!
            Q.add(v)
            #Remember where we came from
            P[v] = u
    return P

#Finding connected components
def components(G): #The connected components
    comp = []
    #Nodes we've already seen
    seen = set()
    #Try every starting point
    for u in G:
        if u in seen:
            #Seen? Ignore it
            continue
        #Traverse component
        C = walk(G, u)
        #Add keys of C to seen
        seen.update(C)
        #Collect the components
        comp.append(C)
    return comp

#Recursive traversal - let's walk in circles
def tree_walk(T, r):#Traverse T from root r
    #For each child...
    for u in T[r]:
        tree_walk(T, u) 

#Making links
def make_link(graph, weight=1):
    G = {}
    for node1, node2 in graph:
        if node1 not in G:
            G[node1] = {}
        G[node1][node2] = weight
        if node2 not in G:
            G[node2] = {}
        G[node2][node1] = weight
    return G 

#Making links with weights
def make_link_with_weight(G, node1, node2, weight=1):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = weight
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = weight
    return G

#Binary Tree Class
class Tree:
    def __init__(self, left, right):
        self.left = left
        self.right = right

#Recurrence            #Solution
T(n) = T(n/2) + 1       Θ(lg n)  

#Bunch Pattern - flexible class that allow you set attributes in the constructor
class Bunch(dict):
    def __init__(self, *args, **kwds):
        super(Bunch, self).__init__(*args, **kwds)
        self.__dict__ = self

T = Bunch
t = T(left=T(left="a", right="b"), right=T(left="c"))
print t.left
>>> {'right': 'b', 'left': 'a'}

#Properties of balanced binary tree
n = root
height = lg n;
number of children = 2^h
sum of internal nodes = n - 1

"""
                                n 
                            /       \
                           /         \
                         n/2         n/2 
                      /   \         /     \
h = lg n = 3         /     \       /       \
                    n/4    n/4    n/4      n/4     sum of each level == n
                  /   \   /  \   /   \     /   \
                 /     \  /   \ /     \   /     \
                1       1 1   1 1      1  1      1 
                            2 ^ h = 8

"""

####--Creating and rotating an array--####

def create_2d_array():
    return [[x+1 for x in range(5)] for x in range(5)]

def rotate_array_90(array):
    height = len(array)
    width = len(array[0])
    return [[array[row][col] for row in range(0, height)] for col in range(0, width)]

def rotate_array_180(array):
    first_rotation = rotate_array_90(array)
    height = len(first_rotation)
    width = len(first_rotation[0])
    return [[first_rotation[row][col] for row in range(0, height)] for col in range(0, width)]































