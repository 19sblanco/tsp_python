import unittest
import random
import math as m

import tsp
import lib

random.seed(0)

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

    def test_tsp_4(self):
        cities = [
            (0,0),
            (-1,2),
            (1,4),
            (-1,8),
            (1,12),
        ]
        distances = tsp.calculate_distances(cities)
        shortest_dist, shortest_path = tsp.tsp(list(range(len(cities))), distances)
        self.assertAlmostEqual(24.8313095581, shortest_dist)

    def test_tsp_5_stress_test(self):
        for t in range(5):
            cities = []
            for i in range(7):
                x = random.randint(1, 100)
                y = random.randint(1, 100)
                cities.append( (x, y) )
            
            distances = tsp.calculate_distances(cities)
            shortest_dist, shortest_path = tsp.tsp(list(range(len(cities))), distances)

            route, min_distance = lib.lib_tsp(cities)

            self.assertAlmostEqual(shortest_dist, min_distance)







            
if __name__ == '__main__':
    unittest.main()






    
            