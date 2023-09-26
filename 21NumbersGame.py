import random
next_num = 1
previous_num = 0 
multiple_of_4 = [x for x in range(1,22) if x%4==0]
num_entered = None
count = 0

def header():
	print("\n\t\tWelcome to the 21 Numbers game.\n")
	print("\n*Rules: \n\t1.You can enter upto 3 numbers in a single try if you want.\n")
	print("\t2.The player that reaches the number 21 at their turn will lose the game")


def start():
	while True:
		user_input = str(input("\nStart the game  ==> (y/n) : \n"))
		user_input = user_input.lower()
	
	
		if user_input == 'y':
			
			while True:
				user_input = str(input("Would you like to go first? ==> (y/n) : \n"))

				if user_input == 'y':
					print("Your turn:")
					player_number_input()
					game_continue_com()
					break
					

				elif user_input == 'n':
					print("Computer's turn:\n")
					computer_turn()
					print(f"Numbers player2(com) wants to enter : {computer_turn()}")
					com_number_input()

					game_continue_player()
					break
	
				else:
					print("Please enter 'y' or 'n' only.")
					continue
			break		

		elif user_input == 'n':
			print("Goodbye!")
			break
		

		else:
			print("Please enter 'y' or 'n' only.")
			continue


		
def player_number_input():
	i = 1
	global next_num
	global previous_num
	while True:
		num_entered = int(input("How many numbers do you want to input?\nEnter num : "))
		if num_entered > 3 or num_entered < 1:
			print("Not valid.\nYou can enter Min : 1, and \nMax : 3 numbers at a try.")
			continue
		else:
			while i <= num_entered:
				num = int(input(f"\tEnter number {i} : ")) 
				if num == next_num:
					i+= 1
					previous_num = num
				else:
					print("Entered number is not continuous.\nEnter next number in the series.")
					continue
				next_num += 1

			break



def com_number_input():
	i = 1
	global next_num
	global previous_num
	global num_entered	
	while i <= num_entered:
		print(f"\n\tEntered number {i} : {next_num}")
		i+=1
		previous_num = next_num
		next_num += 1
		  



def computer_turn():
	global previous_num
	global multiple_of_4
	global num_entered
	
	if previous_num + 1 in multiple_of_4:
		num_entered = 1 
	elif previous_num + 2 in multiple_of_4:
		num_entered = 2
	elif previous_num + 3 in multiple_of_4:
		num_entered = 3
	else:
		num_entered = random.choice(range(1,4))

	return num_entered


def game_continue_player():
	global count
	global next_num

	while next_num != 21:
		player_number_input()
		count = previous_num
		if next_num ==21:
			print("Congratulations. You Won!!")
			break
		print("\nComputer's turn:\n")
		computer_turn()
		print(f"Numbers player2(com) wants to enter : {computer_turn()}")
		com_number_input()
		count = previous_num
		if next_num ==21:
			print("\nYou Lose.")
			break
		continue
	next_num = 1


def game_continue_com():
	global count
	global next_num

	while next_num != 21:
		print("\nComputer's turn:\n")
		computer_turn()
		print(f"Numbers player2(com) wants to enter : {computer_turn()}")
		com_number_input()
		if next_num ==21:
			print("\nYou Lose.")
			break
		count = previous_num
		player_number_input()
		if next_num ==21:
			print("Congratulations. You Won!!")
			break
		count = previous_num
		continue
	next_num = 1


# Running header().
header()

# Running start(). Strating the game.
while True:

	start()
	play_input = str(input("Play Again? (y/n)"))
	if play_input=="n":
		break
	elif play_input=="y":
		continue
	else:
		print("Please enter y or n only.")
		break




"""
#Asking for another play at the game.
while True:	

	play_again = str(input("Try Again? (y/n) : "))
	play_again = play_again.lower()

	if play_again == 'y':
		
		start()
		game_continue()
		continue
	elif play_again == 'n':
		print("Goodbye!")
		break
	else:
		print("Please input 'y' or 'n' only.")
		continue
		

"""