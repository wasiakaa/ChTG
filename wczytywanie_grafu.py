from algorytm_zachlanny import *
def load_graph_from_file(filepath):
    loaded_graph = {}  # to będzie nasz wczytany graf
    with open(filepath) as f:
        for line in f.readlines():
            line_ints = [int(s) for s in line.split(' ')]  # rzutujemy linię wejścia na listę intów
            loaded_graph[line_ints[0]] = line_ints[1:]  # pierwszy element to wierzchołek, a wszystkie następne to lista krawędzi
    return loaded_graph


def save_greedy_to_file(graph_to_color, filepath, k):
    f = open(filepath, "w")  # "w" oznacza, że jeżeli plik nie isnieje, to zostanie utworozny, jeżeli istnieje, to go nadpiszemy
    f.write(str(greedy(graph_to_color, k)))
    f.close()
    return


graph = load_graph_from_file("graph_example.txt")
save_greedy_to_file(graph, "example_colored.txt", 2)
