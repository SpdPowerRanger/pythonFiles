def print_the_board(lst):
	print(lst[7] + "|" + lst[8] + "|" + lst[9])
	print("-+-+-")
	print(lst[4] + "|" + lst[5] + "|" + lst[6])
	print("-+-+-")
	print(lst[1] + "|" + lst[2] + "|" + lst[3])
	print(" ")

#board_lst = [str(x) for x in range (0,10)]
board_lst = [" " for x in range(0,10)]

def player_input(mark,lst):
	num = ' '
	while num not in range(1,10): 
		num = int(input("Enter a number between 1 to 9 :  "))

	lst[num] = mark

	return lst


def empty_space_check(board):
	for x in range(1,10):
		if board[x] == " ":
			return True 

def game_end_check(board,mark):
	"""
	if board[7]==board[8] and board[7]==board[9]:
		return False
	elif board[7]==board[4] and board[7]==board[1]:
		return False
	elif board[7]==board[5] and board[7]==board[3]:
		return False
	elif board[3]==board[2] and board[3]==board[1]:
		return False
	elif board[3]==board[6] and board[3]==board[9]:
		return False
	elif board[9]==board[5] and board[9]==board[1]:
		return False
	elif board[8]==board[5] and board[8]==board[2]:
		return False
	elif board[9]==board[6] and board[9]==board[3]:
		return False
	elif board[4]==board[5] and board[4]==board[6]:
		return False
	else:
		return True
	"""
	return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

def game_continue_check(board):
	if empty_space_check(board) == False and game_end_check(board) == False:
		return True
	elif empty_space_check(board) == True and game_end_check(board) == False:
		return True
	elif empty_space_check(board) == True and game_end_check(board) == True:
		return True
	else:
		return False
	


		




def start():
	
	while True:

		print_the_board(board_lst)
		mark = "X"
		player_input(mark,board_lst)
		
		print_the_board(board_lst)

#		if game_end_check(board_lst) == False:
#			break

		if empty_space_check(board_lst) == False and game_end_check(board_lst,"X") == True:
			break
		elif empty_space_check(board_lst) == True and game_end_check(board_lst,"X") == True:
			break
		elif empty_space_check(board_lst) == True and game_end_check(board_lst,"X") == False:
			pass
		else:
			pass

		mark = "O"
		player_input(mark,board_lst)
		
		print_the_board(board_lst)

#		if game_end_check(board_lst) == False:
#			break
		if empty_space_check(board_lst) == False and game_end_check(board_lst,"O") == True:
			break
		elif empty_space_check(board_lst) == True and game_end_check(board_lst,"O") == True:
			break
		elif empty_space_check(board_lst) == True and game_end_check(board_lst,"O") == False:
			pass
		else:
			pass







start()