try:
    fruits = ["Apple", "Pear", "Orange"]

    def make_pie(index):
        fruit = fruits[index]
        print(fruit + " pie")
        
    make_pie(4)
except IndexError as error_message:
    print(error_message)