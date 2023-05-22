import networkx as nx


def generate_complete_graph(n):
    return nx_graph_to_graph(nx.complete_graph(n))


def generate_random_graph(n, m):
    return nx_graph_to_graph(nx.gnm_random_graph(n, m))


def generate_cycle_graph(n):
    return nx_graph_to_graph(nx.cycle_graph(n))


def generate_bipartite_graph(n):
    return nx_graph_to_graph(nx.complete_bipartite_graph(int(n/2), int(n/2)))


def nx_graph_to_graph(nx_graph):  # Zamienia graf z biblioteki nx na słownik wierzchołków i krawędzi
    graph = {}
    nodes = list(nx_graph)
    if nodes[0] == 0:
        for v in nodes:
            graph[v+1] = [x+1 for x in list(nx_graph.adj[v])]
    else:
        for v in nodes:
            graph[v] = [x for x in list(nx_graph.adj[v])]
    return graph