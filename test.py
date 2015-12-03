import unittest
from day3 import get_num_houses_visited

class Day3Tests(unittest.TestCase):
    
    def test_two_houses(self):
        input_string = ">"
        print "Calculating result for input string %r" % input_string
        self.assertEqual(2, get_num_houses_visited(input_string))
