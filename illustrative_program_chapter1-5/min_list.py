# Initialize an empty list
numbers = []
n = int(input("How many elements do you want in the list: "))

# Loop to get user input for the list
for _ in range(n):
    num = int(input("Enter the number: "))
    numbers.append(num)

# Print the list of numbers
print("The list is:", numbers)

# Initialize min to a very high value
min_value = float('inf')

# Loop to find the minimum value in the list
for i in numbers:
    if i < min_value:
        min_value = i

# Print the minimum value
print("The minimum value in the list is:", min_value)