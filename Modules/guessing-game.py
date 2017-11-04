import random
print("Welcome to The Guessing Game.\n Guess a number between 0 to 100. Let the Computer find it.")
r=[]
for i in range(0,101):
	r.append(i)
while True:
	guess=random.randint(r[0],r[-1])
	print("Computer's guess is %d"%guess)
	x=input("Is Computer's Guess higher or lower or correct? ")
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

	else:
		print("Computer: I love wining the game.")
		playagain=input("Do you want to play again? ")
		if playagain=="no":
			break
