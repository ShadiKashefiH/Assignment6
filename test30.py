import pyfiglet

def show():
    for row in game_board:
        for cell in row:
            print(cell, "", end="")
        print()

def check_game():
    if game_board[0][0] == "X" and game_board [0][1] == "X" and game_board[0][2] == "X":
        print ("Player1 wins!!!")
    else:
        if game_board[1][0] == "X" and game_board [1][1] == "X" and game_board[1][2] == "X":
            print ("Player1 wins!!!")
        else:
            if game_board[2][0] == "X" and game_board [2][1] == "X" and game_board[2][2] == "X":
                print ("Player1 wins!!!")
            else:
    
                if game_board[0][0] == "X" and game_board [1][0] == "X" and game_board[2][0] == "X":
                    print ("Player1 wins!!!")
                else:
                    if game_board[0][1] == "X" and game_board [1][1] == "X" and game_board[2][1] == "X":
                        print ("Player1 wins!!!")
                    else:
                        if game_board[0][2] == "X" and game_board [1][2] == "X" and game_board[2][2] == "X":
                            print ("Player1 wins!!!")
                        else:
    
                            if game_board[0][0] == "X" and game_board [1][1] == "X" and game_board[2][2] == "X":
                                print ("Player1 wins!!!")
                            else:
                                if game_board[2][0] == "X" and game_board [1][1] == "X" and game_board[0][2] == "X":
                                    print ("Player1 wins!!!")
                                else:

                                    if game_board[0][0] == "O" and game_board [0][1] == "O" and game_board[0][2] == "O":
                                        print ("Player2 wins!!!")
                                    else:
                                        if game_board[1][0] == "O" and game_board [1][1] == "O" and game_board[1][2] == "O":
                                            print ("Player2 wins!!!")
                                        else:
                                            if game_board[2][0] == "O" and game_board [2][1] == "O" and game_board[2][2] == "O":
                                                print ("Player2 wins!!!")
                                            else:
    
                                                if game_board[0][0] == "O" and game_board [1][0] == "O" and game_board[2][0] == "O":
                                                    print ("Player2 wins!!!")
                                                else:
                                                    if game_board[0][1] == "O" and game_board [1][1] == "O" and game_board[2][1] == "O":
                                                        print ("Player2 wins!!!")
                                                    else:
                                                        if game_board[0][2] == "O" and game_board [1][2] == "O" and game_board[2][2] == "O":
                                                            print ("Player2 wins!!!")
                                                        else:
    
                                                            if game_board[0][0] == "O" and game_board [1][1] == "O" and game_board[2][2] == "O":
                                                                print ("Player2 wins!!!")
                                                            else:
                                                                if game_board[2][0] == "O" and game_board [1][1] == "O" and game_board[0][2] == "O":
                                                                    print ("Player2 wins!!!")
                                                                else:
                                                                    print("Draw!!!")
    
title = pyfiglet.figlet_format("Tic Tac Toe", font="slant")
print(title)

game_board = [["- ","- ","- ",],
                ["- ","- ","- "],
                ["- ","- ","- "]]
show()



while True:
    #Player1
    print("Player1")
    while True:
        row = int(input("Please enter the row number:"))
        col = int(input("Please enter the column number:"))
        if 0 <= row <= 2 and 0<= col <=2:
            if game_board[row][col] == "-":
                game_board[row][col] = "X"
                show()
                check_game ()
                break
            else:
                print("Choose another cell!")
        else:
            print("choose a number between 0-2!")

    #Player2
    print("Player2")
    while True:
        row = int(input("Please enter the row number:"))
        col = int(input("Please enter the column number:"))
        if 0 <= row <= 2 and 0<= col <=2:
            if game_board[row][col] == "-":
                game_board[row][col] = "X"
                show()
                check_game ()
                break
            else:
                print("Choose another cell!")
        else:
            print("choose a number between 0-2!")           