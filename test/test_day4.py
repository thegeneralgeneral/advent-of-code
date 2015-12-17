import unittest
from day4 import get_suffix_num_resulting_in_five_zeroes, get_suffix_num_resulting_in_six_zeroes

class Day4Tests(unittest.TestCase):

    def test_1(self):
        key = 'abcdef'
        result = get_suffix_num_resulting_in_five_zeroes(key)
        self.assertEqual(609043, result)
        
    def test_2(self):
        key = 'pqrstuv'
        result = get_suffix_num_resulting_in_five_zeroes(key)
        self.assertEqual(1048970, result)
    
    def test_puzzle_2(self):
        key = 'iwrupvqb'
        result = get_suffix_num_resulting_in_six_zeroes(key)
        self.assertEqual(9958218, result)