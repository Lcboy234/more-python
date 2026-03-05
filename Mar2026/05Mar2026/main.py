PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:

    letter_contents = letter_file.read()

    for every_name in names:

        stripped_name = every_name.strip()
        latest_letter = letter_contents.replace(PLACEHOLDER, every_name)
        print(latest_letter)
        
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode = "w") as completed_letter:
            completed_letter.write(latest_letter)