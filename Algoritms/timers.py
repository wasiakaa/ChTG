from coloring_algoritms import *
from graph_generators import *


def time_it_random(n):  # funkcja mierząca czas pracy algorytmów kolorujących dla losowych grafów
    G = generate_random_graph(n, n*8)
    k = n / 5
    return time_it(G, k)


def time_it_complete(n):  # funkcja mierząca czas pracy algorytmów kolorujących dla grafów pełnych
    G = generate_complete_graph(n)
    k = n / 5
    return time_it(G, k)


def time_it_cycle(n):  # funkcja mierząca czas pracy algorytmów kolorujących dla cykli
    G = generate_cycle_graph(n)
    k = n / 5
    return time_it(G, k)


def time_it_bipartite(n):  # funkcja mierząca czas pracy algorytmów kolorujących dla grafów dwudzielnych
    G = generate_bipartite_graph(n)
    k = n / 5
    return time_it(G, k)


def time_it(G, k):
    start_largest_first = time.time()
    largest_first(G, k)
    end_largest_first = time.time()
    start_smallest_last = time.time()
    smallest_last(G, k)
    end_smallest_last = time.time()
    start_dsatur = time.time()
    dsatur(G, k)
    end_dsatur = time.time()
    return [end_largest_first - start_largest_first, end_smallest_last - start_smallest_last,
            end_dsatur - start_dsatur]

n = 100
print(time_it_random(n))
print(time_it_complete(n))
print(time_it_cycle(n))
print(time_it_bipartite(n))