from Algoritms.coloring_algoritms import *
from Algoritms.dsatur import *


def load_graph_from_file(filepath):
    loaded_graph = {}  # to będzie nasz wczytany graf
    with open(filepath) as f:
        for line in f.readlines():
            line_ints = [int(s) for s in line.split(' ')]  # rzutujemy linię wejścia na listę intów
            loaded_graph[line_ints[0]] = line_ints[1:]  # pierwszy element to wierzchołek, a wszystkie następne to lista krawędzi
    return loaded_graph


def save_greedy_to_file(graph_to_color, filepath, k):
    f = open(filepath, "w")  # "w" oznacza, że jeżeli plik nie isnieje, to zostanie utworozny, jeżeli istnieje, to go nadpiszemy
    f.write(str(largest_first(graph_to_color, k)))
    f.write(str(smallest_last(graph_to_color, k)))
    f.write(str(dsatur_2(graph_to_color, k)))
    f.write(str(max(largest_first(graph_to_color, k))))
    f.write(str(max(smallest_last(graph_to_color, k))))
    f.write(str(max(dsatur_2(graph_to_color, k))))
    f.write(str(time_it(graph_to_color,k)))
    f.close()
    return


graph = load_graph_from_file("../Example_in/graph_example_1.txt")
save_greedy_to_file(graph, "../Example_out/example_colored_1.txt", 2)
print(graph)

graph = load_graph_from_file("../Example_in/graph_example_2.txt")
save_greedy_to_file(graph, "../Example_out/example_colored_2.txt", 3)