#writting a code that iteratesthrough every number the list to seperate odd and even numbers from the list
my_list = [1,2,3,4,5,6,7,21,33,32,2,4] 
even_numbers = []
odd_numbers = []
#going through the list to seperate even numbers fromodd numbers
for numbers in my_list:
    if numbers %2 == 0:
        even_numbers.append(numbers)
    else:
        odd_numbers.append(numbers)

#print
print(f'even numbers{even_numbers}')
print(f'odd numbers{odd_numbers}')
