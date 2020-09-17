'''You will design a program that prints all the odd integers between a range. You will ask a user to input the lower and the upper limits of the range and print the odd numbers in the range.'''

#Make the list of numbers with range
range = list(range(int(input("Enter the starting number of the range: ")), int(input("Enter the last number of the range: "))))

print("The list is: ", range)

#going through each number in the list and finding all odd numbers and assigning it to a variable
rangeodd = [num for num in range if num % 2 == 1]

#Print the odd numbers
print("The odd numbers in the list are: ", rangeodd)
