import unittest
import statistics
from statistics import mode
from Coloring_algoritms import *
from wczytywanie_grafu import *


# Sprawdza czy żadne dwa sąsiadujące wierzchołki nie są pokolorowane na ten sam kolor
def is_coloring_correct(G, coloring):
    result = True
    for v in G:
        for u in G[v]:
            if coloring[v-1] == coloring[u-1]:
                result = False
    return result


class MyTestCase(unittest.TestCase):
    def test_LF(self):
        # given
        G = load_graph_from_file("graph_example_1.txt")
        k = 3
        expected_number_of_colors = 3
        # when
        result = largest_first(G, k)
        number_of_colors = max(result)
        max_repetitions = result.count(mode(result))
        # then
        self.assertEqual(number_of_colors, expected_number_of_colors)  # sprawdzam liczbę użytych kolorów
        self.assertLessEqual(max_repetitions, k)  # sprawdzam liczbę wierzchołków w danym kolorze
        self.assertTrue(is_coloring_correct(G, result))   # sprawdzam poprawność kolorowania

# DSatur

# def test_dsatur1(self):
#     # given
#     G1 =
#     k =
#     expected_result

# when

# then


# SL

# given

# when

# then
