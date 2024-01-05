import pandas

data = pandas.read_csv(r"NATO-Phonetic-Alphabet\nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

def generate_phonetic():
    word = input("Enter a word: ").upper()

    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("All character in the word must be letters. Try again")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()