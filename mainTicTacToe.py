import game
import random

if __name__=='__main__':
    board_size = 5
    tic_tac_toe = game.Game(board_size)
    game.MakeAndPrintBoard.print_board(tic_tac_toe)


    while 1==1:
        if tic_tac_toe.computer_turn():
            x = random.randint(0,board_size-1)
            y = random.randint(0,board_size-1)
        else:
            print('Enter x value: 0 - ', board_size-1)
            x = int(input())
            print('Enter y value: 0 - ', board_size - 1)
            y = int(input())
        if tic_tac_toe.game_over():
            game.MakeAndPrintBoard.print_board(tic_tac_toe)
            if tic_tac_toe.game_over() == 'x':
                print('The winner is cross')
            if tic_tac_toe.game_over() == 'o':
                print('The winner is circle')
            if tic_tac_toe.game_over() == 'r':
                print('No winner')
            break
        tic_tac_toe.switch_player()
        if not tic_tac_toe.computer_turn():
            game.MakeAndPrintBoard.print_board(tic_tac_toe)
