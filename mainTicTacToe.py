import game
import random

if __name__=='__main__':
    board_size = 5
    tic_tac_toe = game.Game(board_size)
    game.MakeAndPrintBoard.print_board(tic_tac_toe)
