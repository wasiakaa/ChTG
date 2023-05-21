def greedy(G, k):
    n = len(G)  # liczba wierzchołków grafu G
    col = [0] * n  # tu będziemy zapisywać kolory kolejnych wierzchołków
    col_numb = [0] * n  # tu zliczamy ile jest wierzchołków w danym kolorze
    for i in range(n):
        for j in range(1, n+1):
            if col_numb[j-1] < k:  # sprawdzamy, czy kolor j nie został jeszcze użyty k razy
                if col[i] == 0:  # sprawdzamy, czy wierzchołek i nie został jeszcze pokolorowany
                    checksum = 0  # warunek sprawdza, czy kolor j nie jest zajęty przez sąsiadów
                    for v in G[i+1]:
                        if v < i+1:  # pokolorowani sąsiedzi wierzchołka i
                            if col[v-1] != j:          # sprawdzamy czy sąsiad v wierzchołka i
                                checksum = checksum    # nie ma koloru j
                            else:
                                checksum = checksum + 1
                    if checksum == 0:
                        col[i] = j  # kolorujemy wierzchołek i na kolor j
                        col_numb[j-1] = col_numb[j-1] + 1  # zwiększamy l. wierzchołków w kolorze j
    return col


# Ten greedy nie iteruje po wierchołkach po kolei jak są w G, tylko iteruje w kolejności zadanej przez listę order.
def greedy_with_order(G, k, order):
    n = len(G)  # liczba wierzchołków grafu G
    col = [0] * n  # tu będziemy zapisywać kolory kolejnych wierzchołków
    col_numb = [0] * n  # tu zliczamy ile jest wierzchołków w danym kolorze
    for i in order:
        i = i - 1
        for j in range(1, n+1):
            if col_numb[j-1] < k:  # sprawdzamy, czy kolor j nie został jeszcze użyty k razy
                if col[i] == 0:  # sprawdzamy, czy wierzchołek i nie został jeszcze pokolorowany
                    checksum = 0  # warunek sprawdza, czy kolor j nie jest zajęty przez sąsiadów
                    for v in G[i+1]:
                        # if v < i+1:  # zakomentowane bo w tej wersji greedy nie kolorujemy od najmniejszej do najwiekszej
                            if col[v-1] != j:          # sprawdzamy czy sąsiad v wierzchołka i
                                checksum = checksum    # nie ma koloru j
                            else:
                                checksum = checksum + 1
                    if checksum == 0:
                        col[i] = j  # kolorujemy wierzchołek i na kolor j
                        col_numb[j-1] = col_numb[j-1] + 1  # zwiększamy l. wierzchołków w kolorze j
    return col
