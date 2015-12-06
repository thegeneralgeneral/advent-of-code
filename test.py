import unittest
from day3 import get_num_houses_visited, split_instructions, get_total_houses_visited_with_robo_santa
from day4 import get_suffix_num_resulting_in_five_zeroes, get_suffix_num_resulting_in_six_zeroes
from day5 import is_nice, is_nice_2, INPUT_STRING

class Day3_numHousesVisitedTests(unittest.TestCase):

    def test_two_houses(self):
        input_string = ">"
        self.assertEqual(2, get_num_houses_visited(input_string))

    def test_square(self):
        input_string = "^>v<"
        self.assertEqual(4, get_num_houses_visited(input_string))

    def test_back_and_forth(self):
        input_string = "^v^v^v^v^v"
        self.assertEqual(2, get_num_houses_visited(input_string))

class Day3_splitDirectionsTests(unittest.TestCase):

    def test_1(self):
        input_string = "^v"
        santa, robo = split_instructions(input_string)
        self.assertEqual("^", santa)
        self.assertEqual("v", robo)

    def test_2(self):
        input_string = "^>v<"
        santa, robo = split_instructions(input_string)
        self.assertEqual("^v", santa)
        self.assertEqual("><", robo)

    def test_3(self):
        input_string = "^v^v^v^v^v"
        santa, robo = split_instructions(input_string)
        self.assertEqual("^^^^^", santa)
        self.assertEqual("vvvvv", robo)

class GetNumHousesVisitedWithRoboSantaTests(unittest.TestCase):
    def test_1(self):
        input_string = "^v"
        self.assertEqual(3, get_total_houses_visited_with_robo_santa(input_string))

    def test_2(self):
        input_string = "^>v<"
        self.assertEqual(3, get_total_houses_visited_with_robo_santa(input_string))

    def test_3(self):
        input_string = "^v^v^v^v^v"
        self.assertEqual(11, get_total_houses_visited_with_robo_santa(input_string))

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


from day6 import convert_instruction_string, apply_action_to_value, apply_instruction_to_grid, apply_instruction_string_to_grid, get_1000_by_1000_grid, get_num_lights_on

class Day6_convertInstructionStringTests(unittest.TestCase):
    
    def test_convert_instruction_turn_off(self):
        example = "turn off 387,19 through 720,700"
        expected = "turn off", (387, 19), (720, 700)
        self.assertEqual(expected, convert_instruction_string(example))

    def test_convert_instruction_turn_on(self):
        example = "turn on 952,417 through 954,845"
        expected = "turn on", (952,417), (954,845)
        self.assertEqual(expected, convert_instruction_string(example))

    def test_convert_instruction_toggle(self):
        example = "toggle 347,482 through 959,482"
        expected = "toggle", (347,482), (959,482)
        self.assertEqual(expected, convert_instruction_string(example))

class Day6_applyActionToValueTests(unittest.TestCase):
    
    def test_turn_on(self):
        result = apply_action_to_value("turn on", 0)
        print result
        self.assertEqual(1, apply_action_to_value("turn on", 0))
        self.assertEqual(1, apply_action_to_value("turn on", 1))
    
    def test_turn_off(self):
        self.assertEqual(0, apply_action_to_value("turn off", 0))
        self.assertEqual(0, apply_action_to_value("turn off", 1))
    
    def test_toggle(self):
        self.assertEqual(1, apply_action_to_value("toggle", 0))
        self.assertEqual(0, apply_action_to_value("toggle", 1))
        

class Day6_applyInstructionToGridTests(unittest.TestCase):
    
    def test_turn_on(self):
        grid = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        instruction = "turn on", (0, 0), (3, 2)
        expected = [
            [1, 1, 1, 1, 0],
            [1, 1, 1, 1, 0],
            [1, 1, 1, 1, 0]
        ]
        result = apply_instruction_to_grid(grid, instruction)
        self.assertEqual(expected, result)

    def test_turn_off(self):
        grid = [
            [0, 0, 1, 1, 0],
            [0, 0, 1, 1, 0],
            [0, 0, 1, 1, 0]
        ]
        instruction = "turn off", (2, 0), (3, 1)
        expected = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 1, 1, 0]
        ]
        result = apply_instruction_to_grid(grid, instruction)
        self.assertEqual(expected, result)

class Day6_GetNumLightsOn(unittest.TestCase):
    def test_all_zeroes(self):
        grid = get_1000_by_1000_grid()
        self.assertEqual(0, get_num_lights_on(grid))
    
    def test_example(self):
        grid = [
            [1, 0, 0, 1, 1],
            [0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1]]
        self.assertEqual(9, get_num_lights_on(grid))

    def test_example_full(self):
        grid = [[1 for _ in xrange(1000)] for _ in xrange(1000)]
        self.assertEqual(1000000, get_num_lights_on(grid))