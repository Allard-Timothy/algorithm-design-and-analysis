#####------------Week 4 Notes----------#####

###----Graph Search----###
  # - Breadth First Search
  # - Depth First Search
  # - Finding connected components

# Motivations for graph search
  # - Check if network is connected (phone network, movie network)
  # - Driving directions (shortest path, no tolls) 
    # - Path abstraction: a path is simply a series of decisions
  # - Formulate plan; ie. how to fill in sudoku puzzle

# Goals of graph sub-routines
  # - Find everything findable from given start vertex
                       
         '''          S
                     /
                    *    _
                  /   \   |
                 *     *   ---- Findable vertices 
                  \   /   |
                    *    _
         ''' 
  # - Don't explore anything twice ie. O(m + n) - Linear to size of graph
#
#
#
# Generic Algorithm for searching graph
#
# graph_search(graph G, vertext s)
#     - initially s explored; all other vertices unexplored
#     - while possible:
#           - choose an edge (u, v) u explored, v unexplored  (if none, halt)
#           - mark v explored 
#
# Claim: at end of algorithm, V explored => G has a path from S to V
# Proof: induction on number of iterations
#        by contradicton: suppose G has path P frm S to V,
#                         but V unexplored at end of algorithm.
#                         Since the algorithm won't terminate
#                         unless there is no explored node,
#                         impossible for node to terminate prior 
#                         to the last node being explored:
#        
'''
                     S*-----*------*------*-----*-----*-----*------V*
'''
#         
####------BFS vs DFS-------####
#
# Note: how to choose among the possibly many "frontier" edges?
# 
# Breadth First Search (BFS): O(m+n)  O(m+n) using queue (FIFO)
#  - Explore nodes via layers ie. Start with node S == layer 0 =>
#                                            neighbors of 0 == layer 1 =>
#                                            nieghbors of layer 1 == layer 2
#  - Can compute shortest paths
#  - Can compute connected components of undirected graph
#
# Depth First Search (DFS):  O(m+n) using a stack (LIFO) or via recursion
#  - Explore aggressively like a maze, backtrack when necessary
#  - Compute topological ordering of directed acyclic graph
#  - Compute connected components in direction graphs
#
######----BFS Analysis-----#######
#  - Explore nodes in layers
#  - Compute shortest paths
#  - connected components of undirected graph
#  - O(m+n) linear time
#
#
'''
            A*-----------C*----E*  ------- layer 3
            /            / \    |
           /            /   \   |
          /            /     \  |
        S*-----------B*--------D*
          |            |        |
          |            |        |
        layer 0       layer 1  layer 2
'''
#
# BFS(G graph, s start-vertex)   - all nodes initially unexplored 
#    - mark s as explored
#    - let Q = queue, initialized with s
#    - while Q != 0:
#        - remove first node of Q, call it v
#        - for each edge(v, w):
#              - if w unexplored:
#                 - mark w as explored
#                 - add w to Q
#
# Claim 1: at end of BFS, v explored <=> G has path from s to v
# Reason: special case of generic algorithm
# 
# Claim 2: running time of main while loop
#          == O(Ns + Ms), where Ns = # of nodes reachable from s 
#                               Ms = # of edges reachable from s
# Reason: by inspection of code - 
#         - while loop: never dealing with node more than once
#         - may deal with edges more than once
#
###-----BFS and Shortest Path------###
# Goal: compute dist(v), the fewest # of edges on a path from s to v
# Solution: add node depth from root, to BFS - 
#   - initialize dist(v) = {0 if v = s; += inf if v!= s}
#   - when considering edge(v, w):
#       if w unexplored:
#           set dist(w) = dist(v) + 1
'''
            1            2      3
            A*-----------C*----E*
            /            / \    |
           /            /   \   |
          /            /     \  |
        S*-----------B*--------D*
      dist=0          1        2
'''
# Claim: at termination, dist(v) = i => v in ith layer
# Proof: by induction, for every layer in i, node w is added to Q by
#        a layer in (i-1) or node v, via the edge(v,w)
#
####-----Undirected Connectivity-----###
#
# Let G = (v,e) be an undirected graph.
# connected component = the pieces of G.
# Goal: compute all connected components in O(m+n) time
# Why?: - network connectivity; ie checking if network is fully connected
#       - data visualization; clustering
#
###-------Connected Components via BFS----###
#
# undirected_comp:
#     - all nodes unexplored
#     - for i = 1 to n:
#           if i not yet explored:
#               BFS(G,i)
#
######------------Depth First Search DFS-----------##########
#
# DFS:
#   - explore aggressively
#   - backtrack when necessary
#   - compute topological ordering of directed acyclic graph
#   - strongly connected components of directed graphs
#   - can modify BFS by removing queue and using stack + minor mods
# Run Time: O(m+n)
#
'''         2            3     4
            A*-----------C*----E* 
            /            / \    |
           /            /   \   |
          /            /     \  |
        S*-----------B*--------D* 
        1            6         5
'''
# DFS(graph G, start vertex s):
#     - mark s as explored
#     - for every edge(s,v):
#         if v unexplored:
#             DFS(G, v)
#
# Claim 1: at end; v marked as explored => path from s to v in G
# Proof: particular instantiation of generic search procedure
# Claim 2: Run time - O(m+n) where m=#of nodes reachable from s
#                            where n=# of edges reachable from s
# Proof: look at each edge in connected component of s once and each
#         edge at most twice.
#
#
#
#
#
#














































