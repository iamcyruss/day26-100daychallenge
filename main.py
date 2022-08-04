student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
phonetic = pandas.read_csv("/home/rnicosia/PycharmProjects/day-26/NATO-alphabet-start/NATO-alphabet-start/nato_phonetic_alphabet.csv")
# usper important for dictionary comprehension especially from pandas
phonetic_dict = {row.letter: row.code for (index, row) in phonetic.iterrows()}
print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("What's your name? ").upper()
phonetic_name_list = [l for l in user_input]
print(phonetic_name_list)
phonetic_name = [phonetic_dict[letter] for letter in user_input]
print(phonetic_name)
""" 
The above is how to do it. I over complicated it. phonetic_dict[letter] says to itter through just the letters for the letters in uner_input() and give me the results
which is just the code and not letter and code? why just the code name? if I wanted both values returned.. how'd i do that?
my attempts below were unsuccessful
"""
# new_dict = {new_key:new_value for item in list if test}
# new_dict = {new_key:new_value for item in list}
#phonetic_name = [letter for letter in user_input if letter in phonetic_dict.items()]
#phonetic_name2 = {letter: code for (letter, code) in phonetic_name_list if letter in phonetic_dict.items()}
