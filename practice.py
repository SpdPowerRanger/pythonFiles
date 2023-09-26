from IPython.display import clear_output

def game_board(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


# Global lists which are used as game board.
single_board = ['#',"1","2","3","4","5","6","7","8","9"]


def box_selection_input():
    choice = "wrong"

    while choice not in ['0','1','2','3',"4","5","6","7","8","9"]: 

        choice = input("Enter the row num : ")

        if choice not in ['0','1','2','3',"4","5","6","7","8","9"]:
            clear_output()
            print("Enter a valid digit only.")

        
    if choice in ["0","1","2","3","4","5","6","7","8","9"]:
        return int(choice)
player1_mark = "X"
def player1_choice(board):
    position = box_selection_input()
    board[position] = "X"
    return board[position]

player2_mark = "O"
def player2_choice(board):
    position = box_selection_input()
    board[position] = "O"
    return board[position]




def check_game_end(board,mark):

 return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal


def game_choice():
    choice = "wrong"

    while choice not in ["y","n"]:

        choice = input("play again? : (y/n)").lower()

        if choice not in ["y","n"]:
            print("Choose between (y/n) only.")

    if choice in ["y"]:
        return True
    else:
        return False




def game_start():

    game_on = True
    game_continue = True
    # First print the empty board
    game_board(single_board)


    while game_on:
        while game_continue:
        
            #Player1 turn.
            player1_choice(single_board)

            #Chech for game end.
            check_game_end(single_board,player1_mark)

            #Player2 turn.
            player2_choice(single_board)

            #Check again for game end.
            check_game_end(single_board,player2_mark)

        game_choice()

    print("Goodbye.")


# Running the game.
game_start()

