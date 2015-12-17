

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
