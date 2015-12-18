import unittest
from day18 import Light, Grid, convert_string_to_grid, OFF, ON, INPUT_STRING

class ConvertStringToGridTests(unittest.TestCase):
    
    def test_convert_example_string(self):
        example = """.#.#.#
...##.
#....#
..#...
#.#..#
####.."""
        grid =  convert_string_to_grid(example)
        self.assertEqual(example, str(grid))

class GetNeighboursTests(unittest.TestCase):
    
    def setUp(self):
        self.w = 6
        self.h = 6
        self.grid = Grid(self.w, self.h, [])
    
    def test_get_corner_neighbours(self):
        result = set([l.coords for l in self.grid.get_neighbours(0, 0)])
        expect = {(1, 0), (0, 1), (1, 1)}
        self.assertEqual(expect, result)
    
    def test_get_far_corner_neighbours(self):
        result = set([l.coords for l in self.grid.get_neighbours(5, 5)])
        expect = {(4, 4), (5, 4), (4, 5)}
        self.assertEqual(expect, result)
    
    def test_get_middle_neighbours(self):
        result = set([l.coords for l in self.grid.get_neighbours(3, 3)])
        expect = {(2, 2), (2, 3), (2, 4), (3, 2), (3, 4), (4, 2), (4, 3), (4, 4)}
        self.assertEqual(expect, result)


class GetNextStateTests(unittest.TestCase):

    def setUp(self):
        example = \
""".#.#.#
...##.
#....#
..#...
#.#..#
####.."""
        self.grid = convert_string_to_grid(example)
    
    def test_on_stays_on(self):
        # 2 or 3
        next_state = self.grid.get_next_cell_state(self.grid.lights[3][1])
        self.assertEqual(ON, next_state)
        next_state = self.grid.get_next_cell_state(self.grid.lights[0][5])
        self.assertEqual(ON, next_state)

    def test_on_turns_off(self):
        next_state = self.grid.get_next_cell_state(self.grid.lights[1][0])
        self.assertEqual(OFF, next_state)
        next_state = self.grid.get_next_cell_state(self.grid.lights[0][2])
        self.assertEqual(OFF, next_state)
    
    def test_off_stays_off(self):
        next_state = self.grid.get_next_cell_state(self.grid.lights[0][0])
        self.assertEqual(OFF, next_state)
        next_state = self.grid.get_next_cell_state(self.grid.lights[1][4])
        self.assertEqual(OFF, next_state)
    
    def test_off_turns_on(self):
        next_state = self.grid.get_next_cell_state(self.grid.lights[2][1])
        self.assertEqual(ON, next_state)
        next_state = self.grid.get_next_cell_state(self.grid.lights[5][1])
        self.assertEqual(ON, next_state)

class GridStepTests(unittest.TestCase):

    def setUp(self):
        example = \
""".#.#.#
...##.
#....#
..#...
#.#..#
####.."""
        self.grid = convert_string_to_grid(example)

    def test_step_1(self):
        expect = """..##..
..##.#
...##.
......
#.....
#.##.."""
        print self.grid
        print
        self.grid.step()
        print self.grid
        self.assertEqual(expect, str(self.grid))
        
    
    def test_step_4(self):
        expect = """......
......
..##..
..##..
......
......"""
        print self.grid
        print
        for _ in range(4):
            self.grid.step()
        print self.grid
        print self.grid.get_num_lights()
        self.assertEqual(expect, str(self.grid))
    
    def test_puzzle(self):
        grid = convert_string_to_grid(INPUT_STRING)
        for _ in range(100):
            grid.step()
        print grid.get_num_lights()
    
    def test_example_2(self):
        grid = convert_string_to_grid("""##.#.#
...##.
#....#
..#...
#.#..#
####.#""")
        expect = """##.###
.##..#
.##...
.##...
#.#...
##...#"""
        print grid
        for _ in range(5):
            grid.step_with_stuck_lights()
        print 
        print grid
        self.assertEqual(expect, str(grid))
        
    def test_puzzle_2(self):
        grid = convert_string_to_grid(INPUT_STRING)
        for _ in range(100):
            grid.step_with_stuck_lights()
        print grid.get_num_lights()