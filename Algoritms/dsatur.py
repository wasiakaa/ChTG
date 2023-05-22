
def dsatur(G, k):
    n = len(G)
    satur = [0] * n
    degree = find_degrees(G)
    coloring = [0] * n
    col_count = [0] * n
    for i in range(n):
        v = next_vertice(satur, degree, coloring)
        color = best_color(G, v, coloring, col_count, k)
        coloring[v] = color + 1
        col_count[color] += 1
        satur[v] = 0
        for j in G[v + 1]:
            if coloring[j - 1] == 0:
                satur[j - 1] += 1
    return coloring


# Zwraca najlepszy kolor do zastosowania w wierzchołku v. Zwraca indeks koloru, nie numer.
def best_color(G, v, coloring, col_count, k):
    candidates = [i for i, j in enumerate(col_count) if col_count[i] < k]  # wyznacza listę kolorów które nie zostały wyczerpane
    for i in candidates:
        good_color = True
        for j in G[v + 1]:
            if coloring[j - 1] == i + 1:
                good_color = False
        if good_color:
            return i


# Wyznacza nastepny wierzcholek do DSatur-a - taki o największym stopniu saturacji, a w przypadku remisu
# o największym stopniu wierzchołka.
# Zwraca index wierzchołka, a nie sam numer wierchołka.
def next_vertice(satur, degree, coloring):
    m = max(satur)
    candidates = [i for i, j in enumerate(satur) if j == m]  # wyznacza listę wierzchołków o największym st. saturacji
    candidates = [i for i in candidates if coloring[i] == 0]  # usuwa elementy pokolorowane
    if len(candidates) == 1:  # jeśli jest tylko jeden taki to go zwracamy, w p.p. zdecduje st. wierzchołka
        return candidates[0]
    best_cand = -1
    best_cand_deg = -1
    for i in candidates:
        if degree[i] > best_cand_deg:
            best_cand_deg = degree[i]
            best_cand = i
    return best_cand


# Wyznacza stopień wierchołków danego grafu
def find_degrees(G):
    degree = [0] * len(G)
    for v in G:
        degree[v - 1] = len(G[v])
    return degree


#graph = {1: [2, 3], 2: [1, 3], 3: [1, 2, 4], 4: [3]}
#degs = find_degrees(graph)
#graph = {1: [2, 3], 2: [1, 9], 3: [1, 4, 6, 9], 4: [3, 5], 5: [4, 7], 6: [3, 7, 9], 7: [5, 6, 8, 11], 8: [7], 9: [2, 3, 6, 10], 10: [9, 11], 11: [7, 10, 12], 12: [11]}
#print(dsatur_2(graph, 3))
