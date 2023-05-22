import sys
from Algoritms.greedy_coloring_algorithm import *
from Algoritms.dsatur import *
import time


# # G - graf, ordered_vertices - lista jego wierzchołków w kolejności
# Zamienia wierzchołki grafu G kolejnością tak, by odpowiadały kolejności ordered_vertices
# def rearrange_graph(G, ordered_vertices):
#     newG = {}
#     for v in ordered_vertices:
#         newG[v] = G[v]
#     return newG  # Graf z zadaną kolejnością wierzchołków
#
#
# # Zamienia kolejność w liście kolorowania, tak by kolorowanie odpowiadało grafowi wejściowemu, a nie posortowanemu
# def rearrange_coloring(coloring, ordered_vertices):
#     fixed_coloring = [0] * len(ordered_vertices)
#     it = 0
#     for v in ordered_vertices:
#         fixed_coloring[v-1] = coloring[it]
#         it += 1
#     return fixed_coloring


def largest_first(G, k):
    sorted_vertices = sorted(G, key=lambda v: len(G[v]), reverse=True)  # Sortuje G względem stopnia wierzchołków
    #sorted_graph = rearrange_graph(G, sorted_vertices)
    coloring = greedy_with_order(G, k, sorted_vertices)
    return coloring


# def time_it_random(n):  # funkcja mierząca czas pracy algorytmów kolorujących
#     # G = generate_complete_graph(n)
#     G = generate_random_graph(n, n*8)
#     k = n
#     start_largest_first = time.time()
#     largest_first(G, k)
#     end_largest_first = time.time()
#     start_smallest_last = time.time()
#     smallest_last(G, k)
#     end_smallest_last = time.time()
#     start_dsatur_2 = time.time()
#     dsatur_2(G, k)
#     end_dsatur_2 = time.time()
#     return [end_largest_first - start_largest_first, end_smallest_last - start_smallest_last, end_dsatur_2 - start_dsatur_2]
#
#
# def time_it (G, k):
#     start_largest_first = time.time()
#     largest_first(G, k)
#     end_largest_first = time.time()
#     start_smallest_last = time.time()
#     smallest_last(G, k)
#     end_smallest_last = time.time()
#     start_dsatur_2 = time.time()
#     dsatur_2(G, k)
#     end_dsatur_2 = time.time()
#     return [end_largest_first - start_largest_first, end_smallest_last - start_smallest_last, end_dsatur_2 - start_dsatur_2]


# def sec(pair):
#     return pair[0]
#
#
# def smallest_last(G, k):
#     G2 = graph_to_nx_graph(G)
#     n = len(G)
#     sorted_vertices = [None]*n
#     for i in range(n):
#         v_out = sorted(list(G2.degree(list(G2.nodes()))), key=sec)[0][0]
#         sorted_vertices[n-1-i] = v_out
#         G2.remove_node(v_out)
#     return greedy_with_order(G, k, sorted_vertices)


def smallest_last(G, k):
    n = len(G)
    degrees = find_degrees(G)
    sl_order = [0] * n
    for i in range(n):
        v = degrees.index(min(degrees))
        sl_order[i] = v + 1
        for w in G[v + 1]:
            degrees[w - 1] -= 1
        degrees[v] = sys.maxsize
    sl_order.reverse()
    return greedy_with_order(G, k, sl_order)


# def graph_to_nx_graph(G):
#     nx_graph = nx.Graph()
#     nx_graph.add_nodes_from(list(G.keys()))
#     for i in range(len(G)):
#         for v in G[i+1]:
#             nx_graph.add_edge(i+1, v)
#     return nx_graph


# Przykład
Graph = {1: [2, 3], 2: [1, 3], 3: [1, 2, 4], 4: [3]}
graph2 = {1: [2, 3], 2: [1, 9], 3: [1, 4, 6, 9], 4: [3, 5], 5: [4, 7], 6: [3, 7, 9], 7: [5, 6, 8, 11], 8: [7], 9: [2, 3, 6, 10], 10: [9, 11], 11: [7, 10, 12], 12: [11]}
# a = [4, 3, 2, 1]
# print(Graph)
# print(largest_first(Graph, 2))
# print(generate_random_graph(5,7))
# nds = list(nx.gnm_random_graph(1000,8000))
# print(nds[0])
# print(time_it_random(1000))
# print(time_it_random(5000))
# print(smallest_last(Graph, 2))

