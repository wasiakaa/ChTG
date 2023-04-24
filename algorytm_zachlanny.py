def greedy(G, k):
    n = len(G)  # liczba wierzchołków grafu G
    col = [0] * n  # tu będziemy zapisywać kolory kolejnych wierzchołków
    col_numb = [0] * n  # tu zliczamy ile jest wierzchołków w danym kolorze
    for i in range(1, n+1):
        for j in range(1, n+1):
            if col_numb[j-1] < k:  # sprawdzamy, czy kolor j nie został jeszcze użyty k razy
                if col[i-1] == 0:  # sprawdzamy, czy wierzchołek i nie został jeszcze pokolorowany
                    checksum = 0  # warunek sprawdza, czy kolor j nie jest zajęty przez sąsiadów
                    for v in G[i]:
                        if v < i:  # pokolorowani sąsiedzi wierzchołka i
                            if col[v-1] != j:          # sprawdzamy czy sąsiad v wierzchołka i
                                checksum = checksum    # nie ma koloru j
                            else:
                                checksum = checksum + 1
                    if checksum == 0:
                        col[i-1] = j  # kolorujemy wierzchołek i na kolor j
                        col_numb[j-1] = col_numb[j-1] + 1  # zwiększamy l. wierzchołków w kolorze j
    return col
