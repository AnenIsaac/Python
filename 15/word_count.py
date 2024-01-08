def count_words(filename):
    """Count the approximate number of words in a file"""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "The file you've requested cannot be found"
        print(msg)
    else:
        #count the number of words in the file
        words = contents.split()
        num_words = len(words)
        print("the number of words in " + filename + "is " + str(num_words))

filename = 'alice.txt'
count_words(filename)
