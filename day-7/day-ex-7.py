import random

word_list = ["Javed", "Faham", "Bashkar"]

choose_word = random.choice(word_list)
word_length = len(choose_word)

print(f"Choosing word is: {choose_word}")

display = []
for _ in range(word_length):
    display += "_"

print(display)

guess = input("Please enter your guess letter: ").lower()


# for letter in choose_word:
#     if letter == guess:
#         print("Right")
#     else:
#         print("Wrong")

# Select position using range from 0 to total length of word.
for position in range(word_length):
    # create a variable "letter" and store choose_word position value in it.
    letter = choose_word[position]
    # Now compare letter value with guess word value`
    if letter == guess:
        # update display list value with selected position value.
        display[position] = letter
print(display)
