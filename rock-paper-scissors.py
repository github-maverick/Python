dict={1:"Rock", 2:"Paper", 3:"Scissors"}
uwin=0
cwin=0
from random import randint
pagain="y"
while pagain=="y":
  usr=raw_input("Rock, Paper or Scissors?")
  comp = randint(1,3)
  def out():
      return "Computer: %s"%dict[comp]
  if usr=="Rock":
      if comp==1:
          print out()
      elif comp==2:
          print out()
          cwin+=1
      else:
          print out()
          uwin+=1

  elif usr=="Paper":
          if comp==1:
              print out()
              uwin+=1
          elif comp==2:
              print out()
          else:
              print out()
              cwin+=1

  elif usr=="Scissors":
              if comp==1:
                  print out()
                  cwin+=1
              elif comp==2:
                  print out()
                  uwin+=1
              else:
                  print out()

  else:
      print "I'm sorry. I didn't get that. Please Try Again."

  print "Player Wins: %s"%uwin
  print "Computer Wins: %s"%cwin
  pagain=raw_input("Play again (y/n)?")
