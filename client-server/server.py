import socket
from messages import Message
import os
import logging
import random
import game

if __name__ == '__main__':

    if os.path.isfile("server.log"):
        os.remove("server.log")
    logging.basicConfig(filename="server.log", level=logging.INFO)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 50001)
    print("Starting at %s port %s " % server_address)
    logging.info("Starting at %s port %s " % server_address)
    sock.bind(server_address)
    sock.listen(1)

    while True:
        connection, client_address = sock.accept()
        print("Connected client {}".format(client_address))
        logging.info("Connected client {}" .format(client_address))
        break

    try:
        while True:
            message = Message(1,"1. Number guessing\n2. Tic Tac Toe\n3. Quit")
            message = message.encoding()
            connection.send(message)
            rec = connection.recv(1024)
            response = Message.decoding(rec)
            logging.info("Client chose {}".format(response.message))
            choice = response.message
            try:
                choice = int(choice)
            except ValueError:
                msg = Message(99, "Input is not a number. Quit.")
                logging.info("Client chose not a number. Closing connection.")
                msg = msg.encoding()
                connection.send(msg)
                connection.close()
                print("Connection closed")
                exit()
            if choice == 1:     ## NUMBER GUESSING
                number = random.randint(20, 50)
                msg = Message(9, "Guess number between 20 - 50").encoding()
                attempts = -1
                while True:
                    if attempts < 10:
                        connection.send(msg)
                        recv = connection.recv(1024)
                        recv = Message.decoding(recv)
                        guess = recv.message
                        try:
                            guess = int(guess)
                        except ValueError:
                            msg = Message(9, "You've chosen not a number.").encoding()
                        finally:
                            attempts += 1
                            if number == guess:
                                msg = Message(7, "Good guess. You win.").encoding()
                                connection.send(msg)
                            if guess < number:
                                msg = Message(9, "Try higher number.").encoding()
                            else:
                                msg = Message(9, "Try lower number.").encoding()
            elif choice == 2:       ## TIC TAC TOE
                board_size = 5
                msg = Message(11, "Starting game Tic Tac Toe").encoding()
                connection.send(msg)

                tic_tac_toe = game.Game(board_size)
                board = str(game.MakeBoardStrig.print_board(tic_tac_toe))
                msg = Message(11, board).encoding()
                connection.send(msg)
                while True:
                    if tic_tac_toe.computer_turn():
                        x = random.randint(0, board_size - 1)
                        y = random.randint(0, board_size - 1)
                    else:
                        while True:
                            msg = Message(5, "").encoding()
                            connection.send(msg)
                            rec = connection.recv(1024)
                            print("recv to coords", rec)    # no rec message for input coords
                            #x = random.randint(0, board_size - 1)
                            #y = random.randint(0, board_size - 1)
                            #break
                            move = Message.decoding(rec)
                            try:
                                x = int(move.message[0])
                                y = int(move.message[1])
                                break
                            except ValueError:
                                msg = Message(11, "Coords have to be integers").encoding()
                                connection.send(msg)
                                x = board_size - 1
                                y = board_size - 1
                                break
                    if not tic_tac_toe.choose_square(x, y):
                        msg = Message(11, "Repeat your move").encoding()
                        connection.send(msg)
                    is_over = tic_tac_toe.game_over()
                    if tic_tac_toe.game_over() == game.CheckGameResult.PLAYING:
                        tic_tac_toe.switch_player()
                        if not tic_tac_toe.computer_turn():
                            board = str(game.MakeBoardStrig.print_board(tic_tac_toe))
                            msg = Message(11, board).encoding()
                            connection.send(msg)
                    else:
                        board = str(game.MakeBoardStrig.print_board(tic_tac_toe))
                        msg = Message(11, board).encoding()
                        connection.send(msg)
                        if is_over == game.CheckGameResult.CROSS:
                            msg = Message(11, "\nThe winner is cross").encoding()
                            connection.send(msg)
                        if is_over == game.CheckGameResult.CIRCLE:
                            msg = Message(11, "\nThe winner is circle").encoding()
                            connection.send(msg)
                        if is_over == game.CheckGameResult.DRAW:
                            msg = Message(11, "\nNo winner").encoding()
                            connection.send(msg)
                        msg = Message(7, "\n").encoding()
                        connection.send(msg)
                        break

            elif choice ==3:        ## QUIT
                logging.info("Client chose to quit game. Closing connection")
                msg = Message(99, "Quiting the game").encoding()
                connection.send(msg)
            else:
                msg = Message(99, "Wrong choice. Quit")
                logging.info("Client chose wrong number. Closing connection.")
                msg.encoding()
                connection.send(msg)
            connection.close()
            print("Connection closed")
            exit()
    except (ConnectionAbortedError, ConnectionResetError ):
        connection.close()
        print("Connection closed")
        exit()

