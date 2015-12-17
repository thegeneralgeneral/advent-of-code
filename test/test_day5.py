import unittest
from day5 import is_nice, is_nice_2, INPUT_STRING


class Day5Tests(unittest.TestCase):
    
    def test_nice_1(self):
        self.assertTrue(is_nice("ugknbfddgicrmopn"))
    def test_nice_2(self):
        self.assertTrue(is_nice("aaa"))
        
    def test_naughty_1(self):
        self.assertFalse(is_nice("jchzalrnumimnmhp"))
    def test_naughty_2(self):
        self.assertFalse(is_nice("haegwjzuvuyypxyu"))
    def test_naughty_3(self):
        self.assertFalse(is_nice("dvszwmarrgswjxmb"))
    
    def test_puzzle(self):
        inputs = INPUT_STRING.split('\n')
        num_nice = 0
        for i in inputs:
            if is_nice(i):
                num_nice += 1
        self.assertEqual(258, num_nice)


class Day5Part2Tests(unittest.TestCase):
    
    def test_1(self):
        self.assertTrue(is_nice_2("qjhvhtzxzqqjkmpb"))
     
    def test_2(self):
        self.assertTrue(is_nice_2("xxyxx"))

    def test_3(self):
        self.assertFalse(is_nice_2("uurcxstgmygtbstg"))
        
    def test_4(self):
        self.assertFalse(is_nice_2("ieodomkazucvgmuy"))
        
    def test_overlap_doesnt_count(self):
        self.assertFalse(is_nice_2("aaa"))

    def test_puzzle(self):
        inputs = INPUT_STRING.split('\n')
        num_nice = 0
        for s in inputs:
            if is_nice_2(s):
                num_nice += 1
        self.assertEqual(53, num_nice)
