import sys
from Algoritms.greedy_coloring_algorithm import *
from Algoritms.dsatur import *


def largest_first(G, k):
    sorted_vertices = sorted(G, key=lambda v: len(G[v]), reverse=True)  # Sortuje G względem stopnia wierzchołków
    coloring = greedy_with_order(G, k, sorted_vertices)
    return coloring


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
