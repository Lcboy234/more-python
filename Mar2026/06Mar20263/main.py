# List Comprehension

# numbers = [1, 2, 3]
# new_numbers = [n + 1 for n in numbers]

# print(new_numbers)

# name = "Kai"
# new_list = [letter for letter in name]

# print(new_list)

# new_list = [n * 2 for n in range(1, 5)]
# print(new_list)

names = ["dasdad", "fsdf", "gjndri", "dsead", "fwerfw", "dfased"]
new_names = [name.upper() for name in names if len(name) > 5]
print(new_names)