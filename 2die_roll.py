#rolling two fair dice
from random import randint

#getting user details
username = input("input your name: ")
print("welcome ",username)

#gtting user permission to play or not to play
permmision = input(f"do you want to play the dice roll game or not? \n If yes indictate YES! \n If no indicate NO!.: ")
if permmision == "NO":
    print("please end game")
elif permmision == "YES":
    print("please proceed")
else: print("you have put an invalid statement.\n. The game will now exit ")

