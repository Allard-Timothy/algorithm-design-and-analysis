import sys
import resource

# increase dat recursion level
sys.setrecursionlimit(100000)

# This sucks and is a total hack, will also fail if not run as root.
# Since this hits such a high recursion level, we'll need to increase the limit.
# If not run as root this will complain, python is definitely not designed to handle such
#   a large recursive algorithm and implementing the following with an iterative solution
#   will yield better results and eliminate the need for this. But since the algorithm was
#   explained in class via recursion, I'm implementing it that way, even though an iterative
#   solution is arguably better.

resource.setrlimit(resource.RLIMIT_STACK, (resource.RLIM_INFINITY, resource.RLIM_INFINITY))

def make_graph(file_name):
    """Make a graph from the contents in the file represented by file_name."""
    f = open(file_name, 'r')    
    lines = f.readlines()
    n = int(lines[len(lines)-1].split()[0])
    i = {i:[] for i in range(1, n + 1)}
    j = {i:[] for i in range(1, n + 1)}
    for line in lines:
        curr_line = line.split()
        vec_1 = int(curr_line[0])
        vec_2 = int(curr_line[1])
        i[vec_1].append(vec_2)
        j[vec_2].append(vec_1)
    f.close()
    return i, j

def dfs(G, i, explored, s, pred, processed_nodes, final_nodes):
    """Performs a depth first search in graph G starting from vertex s."""
    explored.add(i)
    pred[i] = s[0]
    for j in G[i]:
        if j not in explored:
            dfs(G, j, explored, s, pred, processed_nodes, final_nodes)
    processed_nodes[0] += 1 
    final_nodes[i] = processed_nodes[0]

def dfs_loop(G, n):
    """Top. sort graph G using dfs."""
    explored = set()
    final_nodes = {i:0 for i in range(1, n + 1)}
    pred = {i:0 for i in range(1, n + 1)}
    processed_nodes = [0]
    s = [0]
    while n > 0:
        if n not in explored:
            s[0] = n
            dfs(G, n, explored, s, pred, processed_nodes, final_nodes)
        n -= 1
    return final_nodes, pred

def create_graph_order(G, n, final_nodes):
    """Create graph based on order of final_nodes."""
    graph = {}
    for i in range(1, n + 1):
        tmp = set()
        for x in G[i]:
            temp.add(final_nodes[x])
        graph[final_nodes[i]] = tmp
    return graph
    
def process_file(file_name):
    i, j = make_graph(file_name)
    n = max(i, key=int)
    t = max(j, key=int)
    final_nodes, pred = dfs_loop(j, t)
    new_graph = create_graph_order(i, n, final_nodes)
    new = max(new_graph, key=int)
    final_nodes, pred = dfs_loop(new_graph, new)

    sorted_pred = sorted(pred.values())
    scc = set()
    start = 0 
    for i in range(n - 1):
        if sorted_pred[i] != sorted_pred[i + 1]:
            scc.add(i - (start + 1))
            start = i + 1
    scc.add(n - start)
    scc = sorted(scc)
    print "The five largest SCCs are: {}".format(scc[:-6:-1])

if __name__ == '__main__':
    file_name = '/users/timallard/git_repo/coursera_design_analysis_algorithms/Week4/SCC.txt'
    process_file(file_name)


