numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers]
print(new_list)

name = "Anen Isaac"
new_list = [letter for letter in name]
print(new_list)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
long_names = [name.upper() for name in names if len(name) > 5]
print(new_list)
