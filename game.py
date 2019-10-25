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
	else:
		print('NOT a tie, check other conditions')
		if player == "Rock":
			print("check to see what the computer is and win or lose")

	player = False
	computer=weapons[randint(0,2)]
