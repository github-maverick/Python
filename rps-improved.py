dict={1:"Rock", 2:"Paper", 3:"Scissors"}
dictr={"Rock":1, "Paper":2, "Scissors":3}
hwin=0
cwin=0
from random import randint
playagain="y"
def choice_to_number(choice):
    return dictr[choice]
def number_to_choice(number):
    return dict[number]
while playagain=="y":
  comp = randint(1,3)
  human=input("Rock, Paper or Scissors? ")
  if (human=="Rock" or human=="Paper" or human=="Scissors"):
    print("Computer Choice: %s"%dict[comp])
    if (choice_to_number(human)-comp)%3==1:
        print("You Won!")
        hwin+=1
    elif choice_to_number(human)==comp:
        print("Its a tie.")

    else:
        print("You Lose!")
        cwin+=1


  else:
      print("I'm sorry. I didn't get that.")

  print("Player Wins: %s"%hwin)
  print("Computer Wins: %s"%cwin)
  playagain=input("Play again (y/n)?")
