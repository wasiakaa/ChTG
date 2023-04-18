# 1 Opis problemu
Będziemy rozpatrywać spójne, nieskierowane grafy proste, to znaczy grafy, w
których istnieje ścieżka między dowolnymi dwoma wierzchołkami, nie ma pętli
ani krawędzi wielokrotnych. Kolorowanie wierzchołkowe grafu $G = (V, E)$ polega na przyporządkowaniu każdemu wierzchołkowi ze zbioru $V$ koloru ze zbioru
$C = {1, 2, .,l}, l \in \mathbb{N}$. Kolorowanie jest właściwe, jeśli żade dwa wierzchołki połączone krawędzią nie mają tego samego koloru. Liczbą chromatyczną $\chi (G)$ grafu
$G$ nazywamy najmniejszą liczbę kolorów potrzebną do przeprowadzenia właściwego kolorowania wierzchołkowego. Wyznaczenie liczby chromatycznej grafu
$G$ oraz znalezienie właściwego kolorowania przy użyciu $\chi (G)$ kolorów są problemami **NP**-trudnymi. Istnieją jednak algorytmy przybliżone, pozwalające na
znalezienie niekoniecznie optymalnego, ale właściwego kolorowania nawet dla
dużych grafów.  
W projekcie zaimplementujemy algorytmy: DSatur, Largest-First oraz
Smallest-Last do przeprowadzenia właściwego kolorowania grafów z ograniczoną
z góry liczbą wierzchołków w każdym kolorze. Następnie porównamy pracę tych
trzech algorytmów dla różnych grafów.  
Zaimplementowane przez nas algorytmy przetestujemy zautomatyzowanymi
testami jednostkowymi.
<br/>

# 2 Algorytmy
## 2.1 Algorytm DSatur
Stopniem saturacji wierzchołka $v$ grafu nazywamy liczbę różnych kolorów, którymi pokolorowani są sąsiedzi tego wierzchołka.
Opis algorytmu:  
1. Wejście: graf $G, k \in \mathbb{N}$  
2. Znajdujemy niepokolorowany wierzchołek $v$ grafu $G$, którego stopień saturacji jest najwyższy. Jeśli jest więcej niż jeden taki wierzchołek, wybieramy jeden z tych, które mają najwyższy stopień w podgrafie indukowanym
przez niepokolorowane wierzchołki grafu $G$.  
3. Wierzchołek $v$ kolorujemy najmniejszym dostępnym kolorem ze zbioru $C$,
to znaczy takim, którym nie jest pokolorowany żaden z jego sąsiadów oraz
takim, którym jest pokolorowanych mniej niż $k$ wierzchołków grafu $G$.  
4. Kończymy, jeśli wszystkie wierzchołki grafu G zostały pokolorowane. W
przeciwnym przypadku, wracamy do punktu 2. i powtarzamy kolejne kroki.  
5. Wyjście: właściwe kolorowanie grafu $G$, z nie więcej niż $k$ wierzchołkami
w każdym kolorze
<br/>

## 2.2 Algorytm Largest-First
Opis algorytmu:  
1. Wejście: graf $G, k \in \mathbb{N}$  
2. Wyznaczamy kolejność wierzchołków $v_1, v_2, ..., v_n$ taką, że $degv_i \ge degv_{i+1}$.  
3. For $i = 1, .., n$ do  
Kolorujemy $v_i$ najmniejszym dostępnym kolorem ze zbioru $C$, to znaczy
takim, którym nie jest pokolorowany żaden z jego sąsiadów oraz takim,
którym jest pokolorowanych mniej niż $k$ wierzchołków grafu $G$.  
4. Wyjście: właściwe kolorowanie grafu $G$, z nie więcej niż $k$ wierzchołkami
w każdym kolorze
<br/>

## 2.3 Algorytm Smallest-Last
Opis algorytmu:  
1. Wejście: graf $G, k \in \mathbb{N}$  
2. Znajdujemy wierzchołek o minimalnym stopniu i usuwamy go z grafu.  
3. Zapamiętując kolejność usuwanych wierzchołków powtarzamy procedurę z
punktu 2. dopóki graf nie jest pusty. Otrzymujemy uporządkowanie wierzchołków $v_1, v_2, ..., v_n$ takie, że $v_{i+1}$ został usunięty przed $v_i$.  
4. For $i = 1, .., n$ do  
Kolorujemy $v_i$ najmniejszym dostępnym kolorem ze zbioru $C$, to znaczy
takim, którym nie jest pokolorowany żaden z jego sąsiadów oraz takim,
którym jest pokolorowanych mniej niż $k$ wierzchołków grafu $G$.  
5. Wyjście: właściwe kolorowanie grafu $G$, z nie więcej niż $k$ wierzchołkami
w każdym kolorze
<br/>

## 3 Bibliografia
[1] Edytorzy Wikipedii, *Kolorowanie grafu*, [dostęp: 18.03.2023], 2019,
url: https://pl.wikipedia.org/wiki/Kolorowanie grafu  
[2] Edytorzy Wikipedii, *DSatur*, [dostęp: 18.03.2023], 2023,
url: https://en.wikipedia.org/wiki/DSatur
