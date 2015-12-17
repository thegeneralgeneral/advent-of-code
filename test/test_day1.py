import unittest
import day1

class Day1_Tests(unittest.TestCase):
    
    def test_test(self):
        self.assertEqual(74, day1.calculate_floor(day1.INPUT_STRING))
        self.assertEqual(1795, day1.calculate_basement_step(day1.INPUT_STRING))
