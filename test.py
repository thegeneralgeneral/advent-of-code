import unittest
from day3 import get_num_houses_visited, split_instructions, get_total_houses_visited_with_robo_santa
from day4 import get_suffix_num_resulting_in_five_zeroes, get_suffix_num_resulting_in_six_zeroes

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

class Day3_splitDirectionsTests(unittest.TestCase):

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

class Day4Tests(unittest.TestCase):

    def test_1(self):
        print 'test_1'
        key = 'abcdef'
        result = get_suffix_num_resulting_in_five_zeroes(key)
        self.assertEqual(609043, result)
        print result
        
    def test_2(self):
        print 'test_2'
        key = 'pqrstuv'
        result = get_suffix_num_resulting_in_five_zeroes(key)
        self.assertEqual(1048970, result)
        print result
    
    def test_puzzle_2(self):
        print 'final'
        key = 'iwrupvqb'
        result = get_suffix_num_resulting_in_six_zeroes(key)
        self.assertEqual(9958218, result)
        print result
        