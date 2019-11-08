from random import randint
from gamefuctions import winlose, gameVars


def winorlose(status):
	print("You totally",status, "\n")
	print("You",status, "Wanna play again?")
	choice = input("Yah / Nah")

	if choice == "Yah":
		gameVars.player_lives = 2
		gameVars.computercomputer_lives = 2
		gameVars.player = False 
		gameVars.computer = gameVars.weapons[randint(0,2)]

	elif choice == "Nah":
		print("You quit. Quitter..")
		exit()
	else:
		print("Make a valid Choice Please")
		winorlose(status)