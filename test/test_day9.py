
import unittest
import day9
        
class Day9_MapDistances_Tests(unittest.TestCase):

    def test_convert_input_to_lookup_table(self):
        input_string = """A to B = 3
A to C = 2
A to B = 3
B to C = 5
B to D = 4
C to D = 3"""
        expect = {
            'A': {'B': 3, 'C': 2},
            'B': {'A': 3, 'C': 5, 'D': 4},
            'C': {'A': 2, 'B': 5, 'D': 3},
            'D': {'B': 4, 'C': 3}
        }
        result = day9.map_distances(input_string)
        self.assertEqual(expect, result)
    
    def test_example_map_distances(self):
        i = """London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141"""
        expect = {
            'London': {'Dublin': 464, 'Belfast': 518},
            'Belfast': {'London': 518, 'Dublin': 141},
            'Dublin': {'Belfast': 141, 'London': 464}}
        self.assertEqual(expect, day9.map_distances(i))


class Day9_GetAllPathsFromAToB_Tests(unittest.TestCase):
    
    def test_get_all_paths_from_single_node(self):
        input_string = """A to B = 3
A to C = 2
A to B = 3
B to C = 5
B to D = 4
C to D = 3"""
        graph = day9.map_distances(input_string)
        expected_paths = [['C', 'A', 'B'], ['C', 'B'], ['C', 'D', 'B']]
        self.assertEqual(expected_paths, day9.get_all_paths_from_a_to_b('C', 'B', graph))
    
    def test_get_all_paths_through_multiple_nodes(self):
        input_string = """A to B = 3
A to C = 2
A to B = 3
B to C = 5
B to D = 4
C to D = 3"""
        graph = day9.map_distances(input_string)
        expected_paths = [['A', 'B', 'C', 'D'], ['A', 'C', 'B', 'D'], ['A', 'B', 'D'], ['A', 'C', 'D']]
        results = day9.get_all_paths_from_a_to_b('A', 'D', graph)
        self.assertTrue(all([expect in results for expect in expected_paths]))
        self.assertTrue(all([result in expected_paths for result in results]))

class Day9_GetLengthOfPath_Tests(unittest.TestCase):
    
    def setUp(self):
        super(Day9_GetLengthOfPath_Tests, self).setUp()
        input_string = """A to B = 3
A to C = 2
A to B = 3
B to C = 5
B to D = 4
C to D = 3"""
        self.graph = day9.map_distances(input_string)
    
    def test_get_length_between_connected_nodes(self):
        result = day9.get_length_of_path(['A', 'B'], self.graph)
        self.assertEqual(3, result)
    
    def test_get_length_of_longer_path(self):
        result = day9.get_length_of_path(['A', 'C', 'B', 'D'], self.graph)
        self.assertEqual(2+5+4, result)

import mock
class Day9_GetShortestPathTests(unittest.TestCase):
    
    def setUp(self):
        input_string = """A to B = 3
A to C = 2
A to B = 3
B to C = 5
B to D = 4
C to D = 3"""
        self.graph = day9.map_distances(input_string)

    def test_gets_shortest_path(self):
        result_path, result_dist = day9.get_shortest_complete_path(self.graph)
        self.assertEqual(8, result_dist)
    
    def test_advent_puzzle(self):
        advent_graph = day9.map_distances(day9.INPUT_STRING)
        result_path, result_dist = day9.get_shortest_complete_path(advent_graph)
        print result_path
        print result_dist
    
    def test_advent_puzzle_part_2_longest_path(self):
        advent_graph = day9.map_distances(day9.INPUT_STRING)
        result_path, result_dist = day9.get_longest_complete_path(advent_graph)
        print result_path
        print result_dist


# Day 9
# result = my_func(day9.INPUT_STRING)