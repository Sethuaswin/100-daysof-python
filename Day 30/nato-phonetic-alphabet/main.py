import pandas as pd


data = pd.read_csv("Day 30/nato-phonetic-alphabet/nato_phonetic_alphabet.csv")  # noqa
phonetic_dict = {row.letter: row.code for index, row in data.iterrows()}


def generate_phonetic():
    word = input("What is your Word?: ").upper()
    # Exception Handeling
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()
