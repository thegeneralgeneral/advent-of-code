import unittest
from life import generate_next_cell_state, DEAD, ALIVE, count_alive_neighbours, generate_next_state


class GenerateNextCellStateTests(unittest.TestCase):

    def test_live_with_fewer_than_2_neighbours_dies(self):
        self.assertEqual(DEAD, generate_next_cell_state(ALIVE, 0))
        self.assertEqual(DEAD, generate_next_cell_state(ALIVE, 1))

    def test_dead_with_fewer_than_2_neighbours_still_dead(self):
        self.assertEqual(DEAD, generate_next_cell_state(DEAD, 0))
        self.assertEqual(DEAD, generate_next_cell_state(DEAD, 1))

    def test_live_cell_with_two_neighbours_lives(self):
        self.assertEqual(ALIVE, generate_next_cell_state(ALIVE, 2))

    def test_live_cell_with_three_neighbours_lives(self):
        self.assertEqual(ALIVE, generate_next_cell_state(ALIVE, 3))

    def test_live_cell_with_more_than_three_neighbours_dies(self):
        for i in range(4, 9):
            self.assertEqual(DEAD, generate_next_cell_state(ALIVE, i))

    def test_dead_cell_with_exactly_three_neighbours_lives(self):
        for i in range(9):
            if i == 3:
                self.assertEqual(ALIVE, generate_next_cell_state(DEAD, 3))
            else:
                self.assertEqual(DEAD, generate_next_cell_state(DEAD, i))

class CountNeighboursTests(unittest.TestCase):

    def test_count_neighbours_returns_0(self):
        blank_grid = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        result = count_alive_neighbours(blank_grid, 1, 1)
        self.assertEqual(0, result)

    def test_one_neighbour(self):
        grid = [
            [1, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        result = count_alive_neighbours(grid, 1, 1)
        self.assertEqual(1, result)

    def test_eight_neighbours_of_dead_cell(self):
        grid = [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
        ]
        result = count_alive_neighbours(grid, 1, 1)
        self.assertEqual(8, result)

    def test_eight_neighbours_of_live_cell(self):
        grid = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ]
        result = count_alive_neighbours(grid, 1, 1)
        self.assertEqual(8, result)

    def test_eight_neighbours_of_live_cell_larger_grid(self):
        grid = [
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1]
        ]
        result = count_alive_neighbours(grid, 1, 1)
        self.assertEqual(8, result)

    def test_lots_of_cells(self):
        grid = [
            [1, 0, 1, 1, 0],
            [1, 1, 1, 1, 0],
            [1, 1, 1, 0, 1],
            [1, 0, 1, 1, 0],
            [1, 1, 1, 1, 0]
        ]
        result = count_alive_neighbours(grid, 1, 2)
        self.assertEqual(7, result)

    def test_corner(self):
        grid = [
            [1, 0, 1, 1, 0],
            [1, 1, 1, 1, 0],
            [1, 1, 1, 0, 1],
            [1, 0, 1, 1, 0],
            [1, 1, 1, 1, 0]
        ]
        result = count_alive_neighbours(grid, 0, 0)
        self.assertEqual(4, result)  # toroidal

    def test_left_border(self):
        grid = [
            [1, 0, 1, 1, 0],
            [1, 1, 1, 1, 0],
            [1, 1, 1, 0, 1],
            [1, 0, 1, 1, 0],
            [1, 1, 1, 1, 0]
        ]
        result = count_alive_neighbours(grid, 0, 3)
        self.assertEqual(5, result)

    def test_bottom_border(self):
        grid = [
            [1, 0, 1, 1, 0],
            [1, 1, 1, 1, 0],
            [1, 1, 1, 0, 1],
            [1, 0, 1, 1, 0],
            [1, 1, 1, 1, 0]
        ]
        result = count_alive_neighbours(grid, 3, 5)
        self.assertEqual(6, result)

    def test_two_rows(self):
        grid = [
            [1, 0, 1, 1, 0],
            [1, 1, 1, 1, 0],
        ]
        result = count_alive_neighbours(grid, 2, 2)
        self.assertEqual(6, result)



class GenerateNextStateTests(unittest.TestCase):

    #
    # Still Lifes
    #

    def test_block(self):
        state = [
            [0, 0, 0, 0],
            [0, 1, 1, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 0]
        ]
        self.assertEqual(state, generate_next_state(state))

    def test_beehive(self):
        state = [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 0, 0],
            [0, 1, 0, 0, 1, 0],
            [0, 0, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ]
        self.assertEqual(state, generate_next_state(state))

    def test_loaf(self):
        state = [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 0, 0],
            [0, 1, 0, 0, 1, 0],
            [0, 0, 1, 0, 1, 0],
            [0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0],
        ]
        self.assertEqual(state, generate_next_state(state))

    def test_boat(self):
        state = [
            [0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0],
            [0, 1, 0, 1, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        self.assertEqual(state, generate_next_state(state))

    def test_blinker(self):
        initial_state = [
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        expected_state = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        self.assertEqual(expected_state, generate_next_state(initial_state))

