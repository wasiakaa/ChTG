def greedy(G, k):
    n = len(G)
    col = [0] * n
    col_numb = [0] * n
    for i in range(1, n+1):
        for j in range(1, n+1):
            if col_numb[j-1] < k:
                if col[i-1] == 0:
                    checksum = 0
                    for v in G[i]:
                        if v < i:
                            if col[v-1] != j:
                                checksum = checksum
                            else:
                                checksum = checksum + 1
                    if checksum == 0:
                        col[i-1] = j
                        col_numb[j-1] = col_numb[j-1] + 1
    return col


g = {1: [2, 3], 2: [1, 3], 3: [1, 2, 4], 4: [3]}

print(greedy(g, 2))
