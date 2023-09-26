from IPython.display import clear_output


# Global lists which are used as game board.
row1 = ["1","2","3"]
row2 = ["4","5","6"]
row3 = ["7","8","9"]



def print_board():
    global row1,row2,row3

    for item in row1:
        print(item,end = " ")
    print(" ")
    for item in row2:
        print(item, end = " ")
    print(" ")
    for item in row3:
        print(item, end = " ")
    print(" ")





def row_selection_input():
    choice = "wrong"

    while choice not in ['0','1','2']: 

        choice = input("Enter the row num : ")

        if choice not in ['0','1','2']:
            clear_output()
            print("Enter a valid digit only.")

        
    if choice in ["0"]:
        return row1
    elif choice in ["1"]:
        return row2
    else:
        return row3

def row_column_selection():
	choice = "wrong"

	while choice not in ["0","1","2"]:
		
		choice = input("Enter the column num : ")

		if choice not in ["0","1","2"]:
			print("Enter a valid digit only.")

	

	if choice in ["0"]:
		return int(choice)
	elif choice in ["1"]:
		return int(choice)
	else:
		return int(choice)


# Global Variables which are used in functions.

row = None
row_column = None
player1_sign = 1
player2_sign = 2



def player1_box_selection():
	global row,row_column
	row = row_selection_input()
	row_column = row_column_selection()
	row[row_column] = player1_sign
	return row


def player1_turn():
	print(player1_box_selection())	
	print_board()







def player2_box_selection():
	global row,row_column
	row = row_selection_input()
	row_column = row_column_selection()
	row[row_column] = player2_sign
	return row

def player2_turn():
	print(player2_box_selection())
	print_board()





def check_game_end():

    global row1,row2,row3

    return ((row1[0] == 1 and row2[0] == 1 and row3[0] == 1) or
        (row1[1] == row2[1] == row3[1]) or
        (row1[2] == row2[2] == row3[2]) or
        (row1[0] == row1[1] == row1[2]) or
        (row2[0] == row2[1] == row2[2]) or
        (row3[0] == row3[1] == row3[2]) or
        (row1[0] == row2[1] == row3[2]) or
        (row1[2] == row2[1] == row3[0]))


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
 	print_board()


 	while game_on:
 		while game_continue:
 		
 			#Player1 turn.
 			player1_turn()

 			#Chech for game end.
 			check_game_end()

 			#Player2 turn.
 			player2_turn()

 			#Check again for game end.
 			check_game_end()

 		game_choice()

 	print("Goodbye.")


# Running the game.
game_start()

