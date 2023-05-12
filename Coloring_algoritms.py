from algorytm_zachlanny import *


def rearrange_graph(G, ordered_vertices):  # G - graf, a - lista jego wierzchołków w kolejności
    newG = {}
    for v in ordered_vertices:
        newG[v] = G[v]
    return newG  # Graf z zadaną kolejnością wierzchołków


def largest_first(G, k):
    sorted_vertices = sorted(G, key=lambda v: len(G[v]), reverse=True)
    sorted_graph = rearrange_graph(G, sorted_vertices)
    print(sorted_graph)
    return greedy(sorted_graph, k)



# Przykład
Graph = {1: [2, 3], 2: [1, 3], 3: [1, 2, 4], 4: [3]}
a = [4, 3, 2, 1]
#print(Graph)
print(Graph)
print(largest_first(Graph, 2))
