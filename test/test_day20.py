import unittest

from day20 import get_num_presents, get_presents_by_elf_for_house, get_first_house_with_n_presents

class GetNumPresentsByElfXTests(unittest.TestCase):
    
    def test_elf_1(self):
        # Should deliver a present to every house.
        for i in range(50):
            self.assertEqual(10, get_presents_by_elf_for_house(1, i))
        
    def test_elf_2(self):
        # Should deliver a present to every *other* house.
        self.assertEqual(0, get_presents_by_elf_for_house(2, 1))
        self.assertEqual(20, get_presents_by_elf_for_house(2, 2))
        self.assertEqual(0, get_presents_by_elf_for_house(2, 3))
        self.assertEqual(20, get_presents_by_elf_for_house(2, 4))
    
    def test_elf_3(self):
        self.assertEqual(0, get_presents_by_elf_for_house(3, 1))
        self.assertEqual(0, get_presents_by_elf_for_house(3, 2))
        self.assertEqual(30, get_presents_by_elf_for_house(3, 3))
        self.assertEqual(0, get_presents_by_elf_for_house(3, 4))


class GetNumPresentsTests(unittest.TestCase):
    
    def test_house_1(self):
        self.assertEqual(10, get_num_presents(1))

    def test_house_2(self):
        self.assertEqual(30, get_num_presents(2))

    def test_house_7(self):
        self.assertEqual(80, get_num_presents(7))

class GetFirstHouseWithNPresents(unittest.TestCase):
    
    def test_example(self):
        self.assertEqual(4, get_first_house_with_n_presents(70))
        
    def test_puzzle(self):
        a, b = 500000, 505000 
        # Checked:
        # 50k - 65k
        # 90k - 91k
        # 150k - 152k
        # 500k - 501k
        
        m = a
        
        # binary search?
        
        print get_first_house_with_n_presents(34000000, a, b)