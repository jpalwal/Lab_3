import unittest
import game


class TestGame(unittest.TestCase):
    def test_if_after_input_coords_draw_in_correct_square_and_end_game_when_there_is_a_winner(self):
        board_size = 4
        tic_tac_toe = game.Game(board_size)
        tic_tac_toe.choose_square(0,1)
        tic_tac_toe.choose_square(0,0)
        tic_tac_toe.choose_square(0,2)
        tic_tac_toe.choose_square(0,3)
        self.assertEqual(game.CheckGameResult(),tic_tac_toe.game_over())

    def test_shoud_not_overrite_coords_if_ocupated(self):
        board_size = 4
        tic_tac_toe = game.Game(board_size)
        tic_tac_toe.choose_square(1,2)
        tic_tac_toe.switch_player()
        tic_tac_toe.choose_square(1,2)
        self.assertEqual(tic_tac_toe[1,2],game.MarkSquare.CROSS)


if __name__=='__main__':
    unittest.main()
