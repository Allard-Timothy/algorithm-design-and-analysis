from prio_dict import priority_dict


def create_graph(file_name):
    f = open(file_name, 'r')
    lines = f.readlines()
    G = {int(line.split()[0]):
            {(int(pair.split(',')[0])):
                int(pair.split(',')[1])
                    for pair in line.split()[1:] if pair} for line in lines if line}
    f.close()
    return G

def dijkstra(G, start, end):
    final_distances = {}
    pred = {}
    prio_q = priority_dict()
    for vertex in G:
        prio_q[vertex] = float("inf")
        pred[vertex] = None
    prio_q[start] = 0
    for v in prio_q:
        final_distances[v] = prio_q[v]
        if v == end:
            break
        for w in G[v]:
            vw_len = final_distances[v] + G[v][w]
            if w not in prio_q or vw_len < prio_q[w]:
                prio_q[w] = vw_len
                pred[w] = v
    return final_distances, pred

def shortest_path(G, start, end):
    i, j = dijkstra(G, start, end)
    path = []
    while 1:
        path.append(end)
        if end == start:
            break
        end = j[end]
    path.reverse() # append adds at end of list
    return path

def create_paths(file_name):
    G = create_graph(file_name)
    verts = [7,37,59,82,99,115,133,165,188,197]
    paths = []
    for vert in verts:
        ret_dict, pred = dijkstra(G, 1, vert)
        if vert != verts[-1]:
            paths.append(ret_dict[vert])
        else:
            paths.append(ret_dict[vert])
    return paths


if __name__ == '__main__':
    file_name = '/users/timallard/git_repo/coursera_design_analysis_algorithms/Week5/dijkstraData.txt'
    for i in create_paths(file_name):
        print i 







