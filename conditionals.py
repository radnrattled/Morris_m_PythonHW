# check a temerature and output a result 
# 
temperature = input("input a number between 0 and 100")

if temperature <= 4:
	print("water is a solid. She frozen")

if temperature < 100:
	print("water is a liquid")

if temperature >= 100:
	print("water is a gas")