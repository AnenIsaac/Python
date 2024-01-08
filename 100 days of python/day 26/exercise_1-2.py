# Squaring numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 13, 21, 34, 55]
squared_numbers = [num**2 for num in numbers]

print(squared_numbers)

# Even numbers only
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 13, 21, 34, 55]
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)

# Exercise 3
with open("file1.txt") as file1:
    file_1_data = file1.readlines()

with open("file2.txt") as file2:
    file_2_data = file2.readlines()

result = [int(num) for num in file_1_data if num in file_2_data]
