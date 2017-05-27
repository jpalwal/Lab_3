import unittest
import game


class TestGame(unittest.TestCase):

    def test_if_game_in_progress_gives_correct_status(self):
        board_size = 5
        tic_tac_toe = game.Game(board_size, 0)
        self.assertEqual(tic_tac_toe.game_over(), game.CheckGameResult.PLAYING)

    def test_if_after_input_coords_draw_in_correct_square_and_end_game_when_there_is_a_winner_horizontally(self):
        board_size = 4
        tic_tac_toe = game.Game(board_size, 0)
        tic_tac_toe.choose_square(0,1)
        tic_tac_toe.choose_square(0,0)
        tic_tac_toe.choose_square(0,2)
        tic_tac_toe.choose_square(0,3)
        self.assertEqual(game.CheckGameResult.CROSS,tic_tac_toe.game_over())

    def test_if_after_input_coords_draw_in_correct_square_and_end_game_when_there_is_a_winner_vertically(self):
        board_size = 4
        tic_tac_toe = game.Game(board_size, 0)
        tic_tac_toe.choose_square(0,1)
        tic_tac_toe.choose_square(1,1)
        tic_tac_toe.choose_square(2,1)
        tic_tac_toe.choose_square(3,1)
        self.assertEqual(game.CheckGameResult.CROSS,tic_tac_toe.game_over())

    def test_shoud_not_overwrite_coords_if_ocupated(self):
        board_size = 4
        tic_tac_toe = game.Game(board_size, 0)
        tic_tac_toe.choose_square(1,2)
        self.assertEqual(tic_tac_toe.choose_square(1,2), False)

    def test_if_board_is_empty_after_init_a_game(self):
        board_size = 3
        tic_tac_toe = game.Game(board_size, 0)
        for i in range(board_size):
            for j in range(board_size):
                self.assertEqual(tic_tac_toe.board[i][j], game.MarkSquare.FREE)


if __name__=='__main__':
    unittest.main()