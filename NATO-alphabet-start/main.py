import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}


# print(phonetic_dict)

def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        word_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetic()
    else:
        print(word_list)


generate_phonetic()
