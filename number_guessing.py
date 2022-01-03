from random import randint
#activate user input
user_number = input("please enter a number between 1 and 6: ") 
user_number = int(user_number)
random_number = randint(1,6)

list_of_numbers = [1,2,3,4,5,6]

#check if user input is valid
if user_number in list_of_numbers:
    print("thank you!")
    print(f"the number the computer chose is {random_number}")
    #check if the user guessed correctly
    while user_number != random_number:
        print("try again")
        user_number = input("please enter a number between 1 and 6: ")
        user_number = int(user_number)
        continue
    print("congratulation!")
