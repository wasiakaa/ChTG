def rearrange_graph (G,a): # G - graf, a - lista jego wierzchołków w kolejności
    newG ={}
    for v in a:
        newG[v] = G[v]
    return newG #Graf z zadaną kolejnością wierzchołków


# Przykład
G = {1: [2, 3], 2: [1, 3], 3: [1, 2, 4], 4: [3]}
a = [4, 3, 2, 1]
print(G)
print (rearrange_graph(G,a))