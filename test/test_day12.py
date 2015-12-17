import unittest
import day12

class Day12_GetTotalTests(unittest.TestCase):
    
    def test_base(self):
        input_dict = {
            'a': [1, 2],
            'b': {'f': [3, 2, 1]},
            'c': {'d': 3, 'e': 2}
        }
        expect = 14
        actual = day12.get_total(input_dict)
        self.assertEqual(expect, actual)

# day 12
# import day12
# import json
# print day12.get_total(json.loads(day12.INPUT_STRING))
