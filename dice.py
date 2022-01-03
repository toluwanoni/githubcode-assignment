#dice roll programme
import random 
number = [1,3,6]
user_roll = random.choice(number)
print(user_roll)
if user_roll== 6:
    print("move to the next step")
elif  user_roll == 3:
    print("roll again")
else :
    user_roll ==1
    print("drop the dice")
