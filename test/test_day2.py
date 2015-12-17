import unittest
import day2

class Day2_Tests(unittest.TestCase):
    
    def setUp(self):
        inputs = day2.INPUT_STRING.split()
        self.lwh_tuples = [tuple([int(n) for n in l.split('x')]) for l in inputs]
    
    def test_get_paper(self):
        total = sum([day2.get_paper_area(l, w, h) for l, w, h in self.lwh_tuples])
        self.assertEqual(1588178, total)

    def test_get_ribbon(self):
        self.assertEqual(34, day2.get_ribbon_length(2, 3, 4))
        self.assertEqual(14, day2.get_ribbon_length(1, 1, 10))
        total = sum([day2.get_ribbon_length(l, w, h) for l, w, h in self.lwh_tuples])
        self.assertEqual(3783758, total)