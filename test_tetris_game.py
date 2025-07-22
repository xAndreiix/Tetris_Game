import unittest
from tetris_game import Piece, create_grid, convert_shape_format, valid_space, check_lost, shapes

class TestTetrisGame(unittest.TestCase):

    def setUp(self):
        self.locked_positions = {}
        self.grid = create_grid(self.locked_positions)
        self.piece = Piece(5, 0, shapes[0])  # S shape

    def test_create_grid_empty(self):
        self.assertEqual(len(self.grid), 20)
        self.assertEqual(len(self.grid[0]), 10)
        for row in self.grid:
            for cell in row:
                self.assertEqual(cell, (0, 0, 0))

    def test_convert_shape_format(self):
        positions = convert_shape_format(self.piece)
        self.assertTrue(all(isinstance(pos, tuple) for pos in positions))
        self.assertTrue(all(len(pos) == 2 for pos in positions))

    def test_valid_space_true(self):
        self.assertTrue(valid_space(self.piece, self.grid))

    def test_valid_space_false(self):
        self.piece = Piece(5, 5, shapes[0])
        positions = convert_shape_format(self.piece)
        locked = {positions[0]: (255, 255, 255)}

        grid = create_grid(locked)
        self.assertFalse(valid_space(self.piece, grid))

        grid = create_grid(locked)
        self.assertFalse(valid_space(self.piece, grid))

    def test_check_lost_false(self):
        self.assertFalse(check_lost(self.locked_positions))

    def test_check_lost_true(self):
        self.locked_positions[(5, 0)] = (255, 255, 255)
        self.assertTrue(check_lost(self.locked_positions))

if __name__ == "__main__":
    unittest.main()
