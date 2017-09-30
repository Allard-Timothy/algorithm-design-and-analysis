####---------Week 5---------------###
##--------------Dijkstra's Shortest Path--------#####

##------Single Source Shortest Paths----------##

# Input: directed graph G=(v,e). (m=1e1, n=1v1)
#     - each edge has non-negative length Le
#     - source vertex s
#
# Output: for each veV, compute L(v) = length of shortest path s-v path in G
#    where length of path == sum of edge lengths
#
# Assumptions: 
#    - directed path from s-v for every different vertex(v)
#    - non-negative edge lengths  *----*----*------*
#                                    1    2    3   path_length = 6 
# Why not use BFS?
#     - You can, if length for every edge == 1 or all edge lengths are the same 
# 
# Why not replace each edge with a path of edges and use BFS? 
# Isn't computing shortest path with general edge weights the same as shortest path
#   with unit edge weights?
#   - graph grows far too large
# 
# Dijkstra(graph G, vertex s)
#    - X = {s} [vertices processed so far]
#    - A[s] = 0 [computed shortest path distances]
#    - B[s] = []  [computed shortest path, initialized as empty] - only used for explaination 
#    
#    - while X != V:  # grow X by one node
#        - among all edges (v,w), pick one that minimizes A[v] + Lvw == v*, w*
#        - add w* to X
#        - set A[w*] = A[v*] + Lv*, w*
#        - set B[w*] = B[v*] + (v*,w*)
#
# Running Time: O(mn) where m = edges; n = vertices
#  - (n-1) iterations of while loop
#  - O(m) work per iteration
#    - [O(1) work per edge]
##***************Danger - Does not support negative edge weights********************#
#
###-------Heaps and Heap Operations----###
#
# Key to linear implementation is data structure: Heap Operations
# 
# Key to heap: perform insert and extract-min
# Complete balanced, binary tree
# Heap property: at every node, key <= childrens key
# extract-min: swapping last lead, bubbling down
# insert: bubbling up
# height = log2n
# Running time: O(logn)
#
####-----implement heap----######
#----------Invariants--------#
# 1: elements in heap: vertices of v-x
# 2: for v in heap !_in X, key[v] = smallest dijksras score of an edge 
# 
# Point: by invariant extraction, extract-min yeilds
#        correct vertext w* to add to X next
#        (we set A[w*] to key[w*])
# 
#-------Maintaining the Invariants-----------#
# Inv_1: vertices that remain in heap will by definition 
#        will not have been processed (outside Capt. X)
#
# Inv_2: update keys that cross frontier
#
#---------#
# Sudo code to implement:
#
# A[w] + L(arch)wv
# for each edge (w,v) e E:
#   - v e V-x == added to heap
#   - delete v from heap
#   - recompute key[v] = min[key[v], A[w]+Lwv]
#   - re-insert v into heap
# 
####----Running Time------####
#
# - Heap Ops: O(logn) each
# - (n-1) for each extract-min
# - (n-1) outgoing key updates = O(n^2) or
#   - each edge (v,w) triggers one insert-delete combo
# 
# # heap Ops: O(m+n)= O(m) since graph weakly connected
# Running Time: O(mlogn) 
#
#####-----------Balanced Search Trees: Operations and Applications--------###########
#
# High-level thought: Dynamic version of sorted array
#    - can accomodate insertion and deletion
# 
# Operations of sorted array:
#    - search: O(logn) - each iteration, halve search space
#    - select: O(1)
#    - min/max: O(1)
#    - pred/succ: O(1)
#    - rank(# of keys <= given key): O(logn)
#    - output sorted order: O(n)
#    
# Raison d'etre: like sorted array, but w/ fast insert/delete (O(n))
# Operations of balanced search trees:
#   - search: O(logn)
#   - select: O(logn)
#   - min/max: O(logn)
#   - pred/succ: O(logn)
#   - rank: O(logn)
#   - output sorted order: O(n)
#   - insert: O(logn)
#   - delete: O(logn)
#
#####----Implementing Balanced Search Trees-------#######
#  - exactly one node per key
#  - each node has                                     *3    - Root
#      - left child pointer                         /       \
#      - right child pointer                       *1        *5
#      - parent pointer                            |          |
#                                                  *2         *4  - Leaves
#
# Search Tree Properties: 
#    - all keys in left sub-tree are smaller
#    - all keys in right sub-tree are larger
#
####------Height of BST------####
# Can be anywhere from log2n => n
#    - log2n: best case, perfectly balanced 
# 
#####----Searching and Inserting----#####
# Search:
# - start at root
# - traverse right if k > key; left if k < key
# - return node with key k or NULL
#
# Insert:
# - search for k (unsuccessfully)
# - rewrire pointer to point to new node with key k
# - preserve search tree property
#
####----Search Tree Basics------######
# Min Key:
#  - start at root
#  - follow left child pointers; return last key found
#
# Predecessor:
#  - if k has non-empty left sub-tree:
#      - return max key in left sub-tree
#  - otherwise:
#      - follow parent pointers until you find key less than k
#
####------In order Traversal-------#####
#
# - start at root, with sub-tree Tl and Tr
# - recurse on Tl
#    - by induction; prints out in ascending order
# - print r's keys
# - recurse on Tr
#    - by induction; prints out in ascending order
#
####-------Red-Black Trees----------#### 
#  - Ensure height always O(logn)
#  Red-Black Invariants 
#    - each node either Red or Black
#    - root is always black
#    - never 2 reds in a row
#      - if node is red; children must be black and parent must be black
#    - every path of root -> null pointer has same # of black nodes
#      - ie. unsuccessful search
#  
# Claim: a chain of length 3 cannot be a red-black tree
# Proof:                                 1*-------------2*------------*3
#    - Look for 0; go left and hit black null pointer == 1 black node
#    - Look for 4; go right and hit 1->2->3->black null pointer == 2 black nodes
#    - each of these violates invariant 4





















