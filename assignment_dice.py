try:
    first_number = int(input("Please enter the first number: "))
    second_number = int(input("Please enter the second number: "))

    answer = second_number/first_number
    print("The answer is {}". format(answer))

except ValueError:
    print("An invalid input has been given")
except ZeroDivisionError:
    print("You cannot divide by zero")
except TypeError:
    print("The input is of the wrong type")
except Exception as e:
    print("Error message: ", e)
