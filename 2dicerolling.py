#rolling two fair dice
from random import randint

#getting user details
username = input("input your name: ")

#gtting user permission to play or not to play
permmision = input(f"do you want to play the dice roll game or not?\nPlease indicate if YES/NO: ")
if permmision == "no":
    print("please end game")
elif permmision == "yes":
    print("please proceed")
else: print("you have put an invalid statement.\n.The game will now exit ")

#die rolling game starts
#instructions before game starts

dieroll_1 = randint(1,6)
dieroll_2 = randint(1,6)
print("To start the game you will need double six." )
print("die rolling...")
user_roll = (dieroll_1 and dieroll_2)
user_roll = input("roll number: ")
print(user_roll)

#die rollingg outcome

if dieroll_1 and dieroll_2 == 6:
    print(f"{username} you can now proceed")
elif dieroll_1 and dieroll_2 !=6:
    print("please try again")
else: print("please exit.")





