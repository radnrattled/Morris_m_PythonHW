from random import randint
from gamefuctions import winlose, gameVars
# figure out what to pass into the fuction -- what are you comparing 

def compared(player,computer):
	if player == gameVars.computer:
		print("tie, no one wins, like in life")
	elif player == "quit":
		print("Youre a quitter")
		exit()

	elif player == "rock":
		if gameVars.computer == "paper":
			print("You LOSE", gameVars.computer,"covers", gameVars.player,"\n")
			gameVars.player_lives = gameVars.player_lives -1
		else:
			print("YOU WON", player, "smashes", gameVars.computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives -1
	elif player == "paper":
		if gameVars.computer == "scissors":
			print("You LOSE", gameVars.computer,"cuts", player,"\n")
			gameVars.player_lives = gameVars.player_lives -1
		else:
			print("YOU WON", player, "covers", gameVars.computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives -1
	elif player == "scissors":
		if gameVars.computer == "rock":
			print("You LOSE", gameVars.computer,"smashes", player,"\n")
			gameVars.player_lives = gameVars.player_lives -1
		else:
			print("YOU WON", player, "cuts", gameVars.computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives -1

	