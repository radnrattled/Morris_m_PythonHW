from random import randint

weapons=["rock", "paper", "scissors"]

computer=weapons[randint(0,2)]

player = False

while player is False:
	player=input("choose rock, paper, or scissors: \n")
	print("computer: ", computer, "player: ", player)

	if player == computer:
		print("tie, no one wins, like in life")
	elif player == "quit":
		print("Youre a quitter")
		exit()

	elif player == "rock":
		if computer == "paper":
			print("You LOSE", computer,"covers", player,"\n")
		else:
			print("YOU WON", player, "smashes", computer, "\n")
	elif player == "paper":
		if computer == "scissors":
			print("You LOSE", computer,"cuts", player,"\n")
		else:
			print("YOU WON", player, "covers", computer, "\n")
	elif player == "scissors":
		if computer == "rock":
			print("You LOSE", computer,"smashes", player,"\n")
		else:
			print("YOU WON", player, "cuts", computer, "\n")

	player = False
	computer=weapons[randint(0,2)]
