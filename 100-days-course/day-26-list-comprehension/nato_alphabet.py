import pandas as pd
import os
import sys

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

student_data_frame = pd.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

print("Working dir:", os.getcwd())
file_path = os.path.join(sys.path[0], "nato_phonetic_alphabet.csv")
print(file_path)
# TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
nato_data = pd.read_csv(file_path)
phonetic_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}
print(phonetic_dict)


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
phonetic_word = [(letter, phonetic_dict[letter]) for letter in word]
print(phonetic_word)
