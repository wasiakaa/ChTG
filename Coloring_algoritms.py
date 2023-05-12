from algorytm_zachlanny import *
import time
import networkx as nx


def rearrange_graph(G, ordered_vertices):  # G - graf, ordered_vertices - lista jego wierzchołków w kolejności
    newG = {}
    for v in ordered_vertices:
        newG[v] = G[v]
    return newG  # Graf z zadaną kolejnością wierzchołków


def largest_first(G, k):
    sorted_vertices = sorted(G, key=lambda v: len(G[v]), reverse=True)
    sorted_graph = rearrange_graph(G, sorted_vertices)
    return greedy(sorted_graph, k)


def time_it(n):  # funkcja mierząca czas pracy algorytmu Largest First
    #G = generate_complete_graph(n)
    G = generate_random_graph(n,n*8)
    k = n
    start = time.time()
    largest_first(G, k)
    end = time.time()
    return end - start


def generate_complete_graph(n):
    return nx_graph_to_graph(nx.complete_graph(n))


def generate_random_graph(n, m):
    return nx_graph_to_graph(nx.gnm_random_graph(n, m))


def nx_graph_to_graph(nx_graph):  #zamienia graf z biblioteki nx na słownik wierzchołków i krawędzi
    graph = {}
    for v in nx_graph.nodes:
        graph[v+1] = [x+1 for x in list(nx_graph.adj[v])]
    return graph


# Przykład
Graph = {1: [2, 3], 2: [1, 3], 3: [1, 2, 4], 4: [3]}
a = [4, 3, 2, 1]
#print(Graph)
#print(Graph)
#print(largest_first(Graph, 2))
#print(generate_graph(5))
print(time_it(1000))