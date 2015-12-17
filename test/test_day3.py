import unittest

from day3 import get_num_houses_visited, split_instructions, \
    get_total_houses_visited_with_robo_santa, INPUT_STRING

class Day3_numHousesVisitedTests(unittest.TestCase):

    def test_two_houses(self):
        input_string = ">"
        self.assertEqual(2, get_num_houses_visited(input_string))

    def test_square(self):
        input_string = "^>v<"
        self.assertEqual(4, get_num_houses_visited(input_string))

    def test_back_and_forth(self):
        input_string = "^v^v^v^v^v"
        self.assertEqual(2, get_num_houses_visited(input_string))

    def test_puzzle(self):
        self.assertEqual(2565, get_num_houses_visited(INPUT_STRING))

class Day3_splitInstructionsTests(unittest.TestCase):

    def test_1(self):
        input_string = "^v"
        santa, robo = split_instructions(input_string)
        self.assertEqual("^", santa)
        self.assertEqual("v", robo)

    def test_2(self):
        input_string = "^>v<"
        santa, robo = split_instructions(input_string)
        self.assertEqual("^v", santa)
        self.assertEqual("><", robo)

    def test_3(self):
        input_string = "^v^v^v^v^v"
        santa, robo = split_instructions(input_string)
        self.assertEqual("^^^^^", santa)
        self.assertEqual("vvvvv", robo)
    

class GetNumHousesVisitedWithRoboSantaTests(unittest.TestCase):
    def test_1(self):
        input_string = "^v"
        self.assertEqual(3, get_total_houses_visited_with_robo_santa(input_string))

    def test_2(self):
        input_string = "^>v<"
        self.assertEqual(3, get_total_houses_visited_with_robo_santa(input_string))

    def test_3(self):
        input_string = "^v^v^v^v^v"
        self.assertEqual(11, get_total_houses_visited_with_robo_santa(input_string))
    
    def test_puzzle(self):
        self.assertEqual(2639, get_total_houses_visited_with_robo_santa(INPUT_STRING))
