#rolling two fair dice
from random import randint

#getting user details
username = input("input your name: ")

#gtting user permission to play or not to play
permmision = input(f"do you want to play the dice roll game or not? \n.if yes indictate YES! \n. if no indicate NO!.: ")
if permmision == "N":
    print("please end game")
elif permmision == "YES":
    print("please proceed")
else: print("you have put an invalid statement.\n. The game will now exit ")

