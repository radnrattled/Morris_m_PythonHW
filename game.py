from random import randint
from gamefuctions import winlose, gameVars, compare


while gameVars.player is False:
	print("==================================")
	print("ComputerLives", gameVars.computer_lives, "/", gameVars.total_lives)
	print("PlayerLives", gameVars.player_lives, "/", gameVars.total_lives)
	print("==================================")
	print("Choose your Weapon!\n")
	player=input("choose rock, paper, or scissors: \n")
	
#this is where you need to call the fuction

compare.compared(player,computer)

elif player == "quit":
		print("Youre a quitter")
		exit()

if gameVars.player_lives is 0:
	winlose.winorlose("lost")
		
elif gameVars.computer_lives is 0:
	winlose.winorlose("won")	

else:
	player = False
	gameVars.computer=gameVars.weapons[randint(0,2)]
