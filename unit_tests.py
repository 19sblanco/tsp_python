import unittest
import random
import math as m

import tsp

class TestAddFunction(unittest.TestCase):

    def test_calculate_distances_simple(self):
        cities = [
            (0, 0),
            (0, 1),
        ]
        distances = tsp.calculate_distances(cities)
        correct_distances = [[0.0, 1.0], [1.0, 0.0]]
        self.assertEqual(distances, correct_distances)

    def test_calculate_distances_medium(self):
        cities = [
            (0, 0),
            (0, 3),
            (4, 0),
        ]
        distances = tsp.calculate_distances(cities)
        correct_distances = [
            [0, 3, 4],
            [3, 0, 5],
            [4, 5, 0],
        ]
        self.assertAlmostEquals(distances, correct_distances)

    def test_tsp_0(self):
        cities = [
            (0, 0),
            (0, 3),
            (4, 0),
        ]
        distances = tsp.calculate_distances(cities)
        shortest_dist, shortest_path = tsp.tsp(list(range(len(cities))), distances)
        self.assertEqual(12, shortest_dist)


    def test_tsp_1(self):
        cities = [
            (0, 0),
            (0, 3),
            (4, 0),
            (0, 9),
        ]
        distances = tsp.calculate_distances(cities)
        shortest_dist, shortest_path = tsp.tsp(list(range(len(cities))), distances)
        true_dist = 3 + 6 + m.sqrt(97) + 4
        self.assertEqual(true_dist, shortest_dist)

    def test_tsp_2(self):
        cities = [
            (0, 0),
            (-1, 1),
            (1, 1),
            (0, -1)
        ]
        distances = tsp.calculate_distances(cities)
        shortest_dist, shortest_path = tsp.tsp(list(range(len(cities))), distances)
        true_dist = m.sqrt(2) + 2 + m.dist((0,1), (-1,-1)) + 1
        self.assertEqual(true_dist, shortest_dist)


    def test_tsp_3(self):
        cities = [
            (0, 0),
            (0, 0),
            (0, 0),
        ]
        distances = tsp.calculate_distances(cities)
        shortest_dist, shortest_path = tsp.tsp(list(range(len(cities))), distances)
        self.assertEqual(0, shortest_dist)


# library functions
def bubble_sort(lst):
    new_lst = []
    for i in range(len(lst)):
        new_lst.append(lst[i])
    while True:
        swapped = False
        for i in range(len(new_lst)-1):
            if new_lst[i] > new_lst[i+1]:
                left = new_lst[i]
                right = new_lst[i+1]
                new_lst[i] = right
                new_lst[i+1] = left
                swapped = True
        if not swapped:
            break
    return new_lst

            
if __name__ == '__main__':
    unittest.main()






    
            