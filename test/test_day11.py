import unittest
import day11

class Day11_PasswordContainsStraight(unittest.TestCase):
    
    def test_contains_straight_at_beginning(self):
        self.assertTrue(day11.contains_straight("hijklmmn"))
        
    def test_contains_straight_at_end(self):
        self.assertTrue(day11.contains_straight("zzzabc"))
    
    def test_doesnt_contain_straight(self):
        self.assertFalse(day11.contains_straight("abbcegjk"))

class Day11_PasswordDoesntContainIOL(unittest.TestCase):
    
    def test_true(self):
        self.assertTrue(day11.contains_iol('foo'))
        self.assertTrue(day11.contains_iol('aaal'))
        self.assertTrue(day11.contains_iol('our'))
        
    def test_false(self):
        self.assertFalse(day11.contains_iol('abc'))
        self.assertFalse(day11.contains_iol('xyz'))

class Day11_ContainsTwoPairsTests(unittest.TestCase):
    
    def test_true(self):
        self.assertTrue(day11.contains_two_pairs('abbcdd'))
    
    def test_false(self):
        self.assertFalse(day11.contains_two_pairs('abbcded'))

import day11

class Day11_GenerateNextPasswordTests(unittest.TestCase):
    
    def test_1(self):
        self.assertEqual("abcdffaa", day11.generate_next_password("abcdefgh"))
        # self.assertEqual("ghjaabcc", day11.generate_next_password("ghijklmn"))

class Day11_IncrementStringTests(unittest.TestCase):
    
    def test_increment_string(self):
        self.assertEqual("abcxyzbc", day11.increment_string("abcxyzbb"))

    def test_increment_zzzzzzzz_wraps(self):
        self.assertEqual("aaaaaaaa", day11.increment_string("zzzzzzzz"))
        


# Day11
# import day11
# lp = "hxbxxyzz" # "hxbxwxba"
# print day11.generate_next_password(lp)
