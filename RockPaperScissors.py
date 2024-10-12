import random
playagain=True

while playagain:
  
  pc= int (input("Welcome to Rock-Paper-Scissors \n1- Rock \n2- Paper \n3- Scissors \nEnter your choice:"))
  cc = random.randint(1,3)

  #computer wins
  if pc ==1 and cc==2 or pc == 2 and cc ==3 or pc ==3 and cc == 1:
    print("The computer wins as \nPlayer chose {} and Computer chose{} ".format(pc, cc))

  #tie
  elif pc == cc:
    print("It's a tie as \nPlayer chose {} and Computer chose{} ".format(pc, cc))

  else:
    print("The player wins as \nPlayer chose {} and Computer chose{} ".format(pc, cc))

  playagain=int(input("Enter 1 to continue 0 to stop.")) 
if playagain==0:
  playagain=False
else:
  playagain=True
