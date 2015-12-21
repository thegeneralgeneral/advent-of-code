import unittest

from day19 import parse_input, generate_possible_steps, get_num_combinations, \
    INPUT_MOLECULE, INPUT_TRANSFORMATION_STRING, \
    get_path_to_molecule

class ParseInputTests(unittest.TestCase):
    
    def test_example(self):
        test_input = """H => HO
H => OH
O => HH"""
        expected = {
            'H': ['HO', 'OH'],
            'O': ['HH']
        }
        self.assertEqual(expected, parse_input(test_input))
    
class GenerateAllTransformationsTests(unittest.TestCase):
    
    def test_example(self):
        trans_dict = {
            'H': ['HO', 'OH'],
            'O': ['HH']
        }
        result = set([item for item in generate_possible_steps('HOH', trans_dict)])
        expect = set(['HOOH', 'HOHO', 'OHOH', 'HHHH'])
        self.assertEqual(expect, result)

class GetNumCombinationsTests(unittest.TestCase):
    def test_example(self):
        trans_dict = {
            'H': ['HO', 'OH'],
            'O': ['HH']
        }
        start = 'HOH'
        expect = 4
        # after 1 step:
        self.assertEqual(expect, get_num_combinations(start, trans_dict))
    
    def test_puzzle(self):
        trans_dict = parse_input(INPUT_TRANSFORMATION_STRING)
        result = get_num_combinations(INPUT_MOLECULE, trans_dict)
        print result

class GetPathToMoleculeTests(unittest.TestCase):

    def setUp(self):
        self.d = parse_input("""e => H
e => O
H => HO
H => OH
O => HH""")
        self.starting_path = ['e']
        
        
    def test_base_case(self):
        path = get_path_to_molecule(self.starting_path, 'H', self.d)
        self.assertEqual(['e', 'H'], path)
    
    def test_base_case_2(self):
        path = get_path_to_molecule(self.starting_path, 'O', self.d)
        self.assertEqual(['e', 'O'], path)
    
    def test_example(self):
        
        path = get_path_to_molecule(self.starting_path, 'HH', self.d)
        expect = ['e' ,'O', 'HH']
        self.assertEqual(expect, path)