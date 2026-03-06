# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     print(key)
#     print(value)

# import pandas
# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     print(index)
#     print(row)
#     #Access row.student or row.score
#     print(row.student)
#     print(row.score)

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")

#TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter anything: ").upper()

# loop through each word in the input for example: K A I for loop check this will automatically tell phonetic_dict to check phonetic_dict[K] which output is Kilo
# for loop will check everything and output them all
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)