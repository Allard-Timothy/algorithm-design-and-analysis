"""Your task is to code up and run the randomized contraction algorithm for the min cut problem
and use it on the above graph to compute the min cut (i.e., the minimum-possible number of crossing edges).
"""

from random import choice
from copy import deepcopy

def contract(v1, v2, G):
    """Contracts two vertices from random edge in graph G into single vertex
    :param vert1: first vertex
    :param vert2: second vertex
    :param G: input graph
    """
    G[v1].extend(G[v2]) # add v2's list to v1's
    for adj_v in G[v2]: # look at every adjacent node of v2
        new_l = G[adj_v]
        for i in range(0, len(new_l)): # scan and swap v1 for v2
            if new_l[i] == v2:
                new_l[i] = v1
    while v1 in G[v1]: # remove loop in v1
        G[v1].remove(v1)    
    del G[v2] # remove v2 from graph

def find_min_cut(G):
    """Find the minimum cut in graph G using Karger's algorithm
    :param G: input graph
    """
    while len(G) > 2: # while more than two vertices in G
        v1 = choice(list(G.keys())) # first random vertex
        v2 = choice(G[v1]) # second random vertex
        contract(v1, v2, G) # contract v2 into v1
    return len(G.popitem()[1]) # pop item and return len, which is min cut

def run_find_mincut(cut_range, file_path):
    """Find the minimum cut in G using Karger's algorithm.
    """
    f = open(file_path, 'r')
    lines = f.readlines()
    G = {int(line.split()[0]): [int(v) for v in line.split()[1:] if v] for line in lines if line}
    min_cut = float("inf")

    for i in range(cut_range): 
        curr = find_min_cut(deepcopy(G))
        if curr < min_cut:
            min_cut = curr
    print "The min cut is:", min_cut

if __name__ == '__main__':
    cut_range = ''
    file_path = '/users/timallard/git_repo/coursera_design_analysis_algorithms/Week3/kargerMinCut.txt'
    run_find_mincut(cut_range, file_path)