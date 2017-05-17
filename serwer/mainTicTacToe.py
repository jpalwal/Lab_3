import game
import random
from echoClient import MyEchoClient

if __name__=='__main__':

    client = MyEchoClient('localhost', 50001, 1024)
    size = client.sock.recv(client.data_size).decode()
    msg = input()
    client.sock.send(msg.encode())
    board_size = 5

    while True:
        print(client.sock.recv(client.data_size).decode())
        msg = input()
        client.sock.send(msg.encode())

    #tic_tac_toe = game.Game(board_size, server)
    #game.MakeAndPrintBoard.print_board(tic_tac_toe)

    #while True:
     #   if tic_tac_toe.computer_turn():
      #      x = random.randint(0,board_size-1)
       #     y = random.randint(0,board_size-1)
        #else:
         #   print('Enter x value: 0 - ', board_size-1)
          #  x = int(input())
           # print('Enter y value: 0 - ', board_size - 1)
            #y = int(input())
        #if not tic_tac_toe.choose_square(x,y):
         #   print("Repeat move")
        #is_over = tic_tac_toe.game_over()
        #if tic_tac_toe.game_over() == game.CheckGameResult.PLAYING:
        #    tic_tac_toe.switch_player()
        #    if not tic_tac_toe.computer_turn():
        #        game.MakeAndPrintBoard.print_board(tic_tac_toe)
        #else:
        #    game.MakeAndPrintBoard.print_board(tic_tac_toe)
        #    if is_over == game.CheckGameResult.CROSS:
        #        print('\n\nThe winner is cross')
        #    if is_over == game.CheckGameResult.CIRCLE:
        #        print('\n\nThe winner is circle')
        #    if is_over == game.CheckGameResult.DRAW:
        #        print('\n\nNo winner')
        #   break
