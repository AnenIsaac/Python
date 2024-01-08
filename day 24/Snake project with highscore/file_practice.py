with open("my_file.txt") as file_object:
    contents = file_object.read()
    print(contents)

with open("my_file.txt", "a") as file:
    file.write("\nHere is the new line!")

with open("new_file.txt", "w") as file:
    file.write("here is the new document")
