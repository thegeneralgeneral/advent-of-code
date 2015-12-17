import unittest

from day6 import convert_instruction_string, apply_action_to_value, apply_instruction_to_grid, apply_instruction_string_to_grid, get_1000_by_1000_grid, get_num_lights_on, get_brightness


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
        self.assertEqual(1, apply_action_to_value("turn on", 0))
        self.assertEqual(2, apply_action_to_value("turn on", 1))
    
    def test_turn_off(self):
        self.assertEqual(0, apply_action_to_value("turn off", 0))
        self.assertEqual(0, apply_action_to_value("turn off", 1))
        self.assertEqual(4, apply_action_to_value("turn off", 5))
    
    def test_toggle(self):
        self.assertEqual(2, apply_action_to_value("toggle", 0))
        self.assertEqual(3, apply_action_to_value("toggle", 1))
        

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

class Day6_getBrightnessTests(unittest.TestCase):
    def test_brightness(self):
        example = [
            [1, 2, 3, 0, 0],
            [3, 3, 3, 3, 0],
            [0, 0, 0, 0, 1]]
        expected = 19
        result = get_brightness(example)
        self.assertEqual(expected, result)
