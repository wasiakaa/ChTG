from coloring_algoritms import *
from graph_generators import *


def time_it_random(n):  # funkcja mierząca czas pracy algorytmów kolorujących
    G = generate_random_graph(n, n*8)
    k = n / 5
    return time_it(G, k)


def time_it_complete(n):
    G = generate_complete_graph(n)
    k = n / 5
    return time_it(G, k)


def time_it_cycle(n):
    G = generate_cycle_graph(n)
    k = n / 5
    return time_it(G, k)


def time_it_empty(n):
    G = generate_empty_graph(n)
    k = n / 5
    return time_it(G, k)


def time_it_bipartite(n):
    G = generate_empty_graph(n)
    k = n / 5
    return time_it(G, k)


def time_it(G, k):
    start_largest_first = time.time()
    largest_first(G, k)
    end_largest_first = time.time()
    start_smallest_last = time.time()
    smallest_last(G, k)
    end_smallest_last = time.time()
    start_dsatur_2 = time.time()
    dsatur_2(G, k)
    end_dsatur_2 = time.time()
    return [end_largest_first - start_largest_first, end_smallest_last - start_smallest_last,
            end_dsatur_2 - start_dsatur_2]


print(time_it_random(1000))
print(time_it_complete(200))
print(time_it_cycle(1000))
print(time_it_empty(1000))
print(time_it_bipartite(1000))