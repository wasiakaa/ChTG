from App.load_and_save_graph import *

# INSTRUKCJA OBSŁUGI PROGRAMU
# Wpisz graf do pokolorowania w pliku "App/graph_to_coloring.txt".
# Poniżej w linijce 9. podaj k, czyli maksymalną liczbę wierzchołków w jednym kolorze.
# Następnie uruchom plik app.py, wynik zostanie zapisany w pliku "App/coloring_result.txt"

def app():
    graph_to_color = load_graph_from_file("../App/graph_to_coloring.txt")
    k = 2
    save_colorings_to_file(graph_to_color, "../App/coloring_result.txt", k)


app()