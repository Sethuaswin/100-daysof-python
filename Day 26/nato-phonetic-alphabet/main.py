import pandas as pd

# TODO 1. Create a dictionary in this format:
data = pd.read_csv("Day 26/nato-phonetic-alphabet/nato_phonetic_alphabet.csv")  # noqa
phonetic_dict = {row.letter: row.code for index, row in data.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.  # noqa
word = input("What is your Word?: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)
