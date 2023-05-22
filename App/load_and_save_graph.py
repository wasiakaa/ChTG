from Algoritms.coloring_algoritms import *
from Algoritms.dsatur import *
from Algoritms.timers import time_it


def load_graph_from_file(filepath):
    loaded_graph = {}
    with open(filepath) as f:
        for line in f.readlines():
            line_ints = [int(s) for s in line.split(' ')]  # rzutujemy linię wejścia na listę intów
            loaded_graph[line_ints[0]] = line_ints[1:]  # pierwszy element to wierzchołek, a wszystkie następne to lista krawędzi
    return loaded_graph


def save_colorings_to_file(graph_to_color, filepath, k):
    f = open(filepath, "w")  # "w" oznacza, że jeżeli plik nie isnieje, to zostanie utworozny, jeżeli istnieje, to go nadpiszemy
    f.write("largest first = " + str(largest_first(graph_to_color, k)) + '\n')
    f.write("smallest last = " + str(smallest_last(graph_to_color, k)) + '\n')
    f.write("dsatur = " + str(dsatur(graph_to_color, k)) + '\n')
    f.write("largest first liczba kolorow = " + str(max(largest_first(graph_to_color, k))) + '\n')
    f.write("smallest last liczba kolorow = " + str(max(smallest_last(graph_to_color, k))) + '\n')
    f.write("dsatur liczba kolorow = " + str(max(dsatur(graph_to_color, k))) + '\n')
    f.write("czasy wykonania = " + str(time_it(graph_to_color, k)) + '\n')
    f.close()
    return


graph = load_graph_from_file("../Example_in/graph_example_1.txt")
save_colorings_to_file(graph, "../Example_out/example_colored_1.txt", 2)
print(graph)

graph = load_graph_from_file("../Example_in/graph_example_2.txt")
save_colorings_to_file(graph, "../Example_out/example_colored_2.txt", 3)