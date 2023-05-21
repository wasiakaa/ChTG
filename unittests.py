import unittest
import statistics
from statistics import mode
from coloring_algoritms import *
from load_and_save_graph import *


# Sprawdza czy żadne dwa sąsiadujące wierzchołki nie są pokolorowane na ten sam kolor
def is_coloring_correct(G, coloring):
    result = True
    for v in G:
        for u in G[v]:
            if coloring[v-1] == coloring[u-1]:
                result = False
    return result


class MyTestCase(unittest.TestCase):
# LARGEST FIRST
    def test_largest_first_1(self):
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

    def test_largest_first_2(self):
        # given
        G = load_graph_from_file("graph_example_2.txt")
        k = 2
        expected_number_of_colors = 3
        # when
        result = largest_first(G, k)
        number_of_colors = max(result)
        max_repetitions = result.count(mode(result))
        # then
        self.assertEqual(number_of_colors, expected_number_of_colors)
        self.assertLessEqual(max_repetitions, k)
        self.assertTrue(is_coloring_correct(G, result))

    def test_largest_first_3(self):
        # given
        G = load_graph_from_file("graph_example_3.txt")
        k = 3
        expected_number_of_colors = 2
        # when
        result = largest_first(G, k)
        number_of_colors = max(result)
        max_repetitions = result.count(mode(result))
        # then
        self.assertEqual(number_of_colors, expected_number_of_colors)
        self.assertLessEqual(max_repetitions, k)
        self.assertTrue(is_coloring_correct(G, result))

    def test_largest_first_4(self):
        # given
        G = load_graph_from_file("graph_example_3.txt")
        k = 2
        expected_number_of_colors = 4
        # when
        result = largest_first(G, k)
        number_of_colors = max(result)
        max_repetitions = result.count(mode(result))
        # then
        self.assertEqual(number_of_colors, expected_number_of_colors)
        self.assertLessEqual(max_repetitions, k)
        self.assertTrue(is_coloring_correct(G, result))

    def test_largest_first_5(self):
        # given
        G = load_graph_from_file("graph_example_4.txt")
        k = 3
        expected_number_of_colors = 4
        # when
        result = largest_first(G, k)
        number_of_colors = max(result)
        max_repetitions = result.count(mode(result))
        # then
        self.assertEqual(number_of_colors, expected_number_of_colors)
        self.assertLessEqual(max_repetitions, k)
        self.assertTrue(is_coloring_correct(G, result))

    def test_largest_first_6(self):
        # given
        G = load_graph_from_file("graph_example_4.txt")
        k = 4
        expected_number_of_colors = 3
        # when
        result = largest_first(G, k)
        number_of_colors = max(result)
        max_repetitions = result.count(mode(result))
        # then
        self.assertEqual(number_of_colors, expected_number_of_colors)
        self.assertLessEqual(max_repetitions, k)
        self.assertTrue(is_coloring_correct(G, result))

# SMALLEST LAST
    def test_smallest_last_1(self):
        # given
        G = load_graph_from_file("graph_example_1.txt")
        k = 3
        expected_number_of_colors = 3
        # when
        result = largest_first(G, k)
        number_of_colors = max(result)
        max_repetitions = result.count(mode(result))
        # then
        self.assertEqual(number_of_colors, expected_number_of_colors)
        self.assertLessEqual(max_repetitions, k)
        self.assertTrue(is_coloring_correct(G, result))

    def test_smallest_last_2(self):
        # given
        G = load_graph_from_file("graph_example_2.txt")
        k = 2
        expected_number_of_colors = 3
        # when
        result = largest_first(G, k)
        number_of_colors = max(result)
        max_repetitions = result.count(mode(result))
        # then
        self.assertEqual(number_of_colors, expected_number_of_colors)
        self.assertLessEqual(max_repetitions, k)
        self.assertTrue(is_coloring_correct(G, result))
    def test_smallest_last_3(self):
        # given
        G = load_graph_from_file("graph_example_3.txt")
        k = 3
        expected_number_of_colors = 2
        # when
        result = largest_first(G, k)
        number_of_colors = max(result)
        max_repetitions = result.count(mode(result))
        # then
        self.assertEqual(number_of_colors, expected_number_of_colors)
        self.assertLessEqual(max_repetitions, k)
        self.assertTrue(is_coloring_correct(G, result))
    def test_smallest_last_4(self):
        # given
        G = load_graph_from_file("graph_example_3.txt")
        k = 2
        expected_number_of_colors = 4
        # when
        result = largest_first(G, k)
        number_of_colors = max(result)
        max_repetitions = result.count(mode(result))
        # then
        self.assertEqual(number_of_colors, expected_number_of_colors)
        self.assertLessEqual(max_repetitions, k)
        self.assertTrue(is_coloring_correct(G, result))
    def test_smallest_last_5(self):
        # given
        G = load_graph_from_file("graph_example_4.txt")
        k = 3
        expected_number_of_colors = 4
        # when
        result = largest_first(G, k)
        number_of_colors = max(result)
        max_repetitions = result.count(mode(result))
        # then
        self.assertEqual(number_of_colors, expected_number_of_colors)
        self.assertLessEqual(max_repetitions, k)
        self.assertTrue(is_coloring_correct(G, result))
    def test_smallest_last_6(self):
        # given
        G = load_graph_from_file("graph_example_4.txt")
        k = 4
        expected_number_of_colors = 3
        # when
        result = largest_first(G, k)
        number_of_colors = max(result)
        max_repetitions = result.count(mode(result))
        # then
        self.assertEqual(number_of_colors, expected_number_of_colors)
        self.assertLessEqual(max_repetitions, k)
        self.assertTrue(is_coloring_correct(G, result))

# DSatur

# def test_dsatur1(self):
#     # given
#     G1 =
#     k =
#     expected_result

# when

# then
