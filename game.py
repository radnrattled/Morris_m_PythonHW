from random import randint

weapons=["rock", "paper", "scissors"]

# adding lives 
player_lives = 1
computer_lives = 1

computer=weapons[randint(0,2)]

player = False

def winorlose(status):
	print("called win or lose",status)
	print("You",status, "Wanna play again?")
	choice = input("Yah / Nah")

	if choice == "Yah":
		global player_lives
		global computer_lives
		global player
		global computer
		player_lives = 5
		computer_lives = 5
		player = False 
		computer = choice[randint(0,2)]

	elif choice == "Nah":
		print("You quit. Quitter..")
		exit()
	else:
		print("Make a valid Choice Please")


while player is False:
	print("==================================")
	print("ComputerLives", computer_lives, "/5\n")
	print("PlayerLives", player_lives, "/5\n")
	print("==================================")
	print("Choose your Weapon!\n")
	player=input("choose rock, paper, or scissors: \n")
	#print("computer: ", computer, "player: ", player)

	if player == computer:
		print("tie, no one wins, like in life")
	elif player == "quit":
		print("Youre a quitter")
		exit()

	elif player == "rock":
		if computer == "paper":
			print("You LOSE", computer,"covers", player,"\n")
			player_lives = player_lives -1
		else:
			print("YOU WON", player, "smashes", computer, "\n")
			computer_lives = computer_lives -1
	elif player == "paper":
		if computer == "scissors":
			print("You LOSE", computer,"cuts", player,"\n")
			player_lives = player_lives -1
		else:
			print("YOU WON", player, "covers", computer, "\n")
			computer_lives = computer_lives -1
	elif player == "scissors":
		if computer == "rock":
			print("You LOSE", computer,"smashes", player,"\n")
			player_lives = player_lives -1
		else:
			print("YOU WON", player, "cuts", computer, "\n")
			computer_lives = computer_lives -1

	if player_lives is 0:
		winorlose("lost")
		#print("Youre a loser. Do you wanna LOSE again?")
		#choice = input("Yah / Nah")

		#if choice == "Yah":
		#	player_lives = 5
		#	computer_lives = 5
		#	player = False 
		#	computer = choice[randint(0,2)]

		#elif choice == "Nah":
		#	print("You quit. Quitter..")
		#else:
		#	print("Make a valid Choice Please")
	elif computer_lives is 0:
		winorlose("won")
		#print("You are a king of kings at RPS, wanna win again?")
		#choice = input("Yah / Nah")

		#if choice == "Yah":
		#	player_lives = 5
		#	computer_lives = 5
		#	player = False 
		#	computer = choice[randint(0,2)]
		#elif choice == "Nah":
		#	print("You quit. Quitter..")
		#	exit()
		#else:
		#	print("Make a valid Choice Please")


	player = False
	computer=weapons[randint(0,2)]
