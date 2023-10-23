# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp  # noqa
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp  # noqa
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp  # noqa

PLACEHOLDER = "[name]"

with open("Day 24/mail-merging/Input/Names/invited_names.txt") as f:
    name_list = f.readlines()

with open("Day 24/mail-merging/Input/Letters/starting_letter.txt") as f:
    letter = f.read()
    for name in name_list:
        stripped_name = name.strip()
        new_letter = letter.replace(PLACEHOLDER, stripped_name)
        with open(f"Day 24/mail-merging/Output/ReadyToSend/letter_for_{stripped_name}.txt", 'w') as completed_letter:  # noqa
            completed_letter.write(new_letter)
