import random
r=[x for x in range(1,101)]
print("Welcome to The Guessing Game.\nGuess a number between 0 to 100.\nLet the Computer find it.\n")
while True:
	guess=random.randint(r[0],r[-1])
	print("Computer's guess is %d"%guess)
	x=input("\nIs Computer's Guess higher or lower or correct? ")
	if x=="lower":
		counter=r[0]
		while True:
			if counter>guess:
				break
			r.remove(counter)
			counter+=1
	elif x=="higher":
		counter=r[-1]
		while True:
			if counter<guess:
				break
			r.remove(counter)
			counter-=1
	elif x=="correct":
		print("\nComputer: I love wining the game.")
		break
	else:
		print("\nI'm sorry I didn't get that.")
