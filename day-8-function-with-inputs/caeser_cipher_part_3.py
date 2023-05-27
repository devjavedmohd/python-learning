alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caeser(direction, text, shift):
    new_position = ''
    new_letter = ''
    if direction == "decode":
        shift *= -1
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            # if direction == "encode":
            #     new_position = (position + shift) % len(alphabet)
            # elif direction == "decode":
            #     new_position = (position - shift) % len(alphabet)
            new_position = (position + shift) % len(alphabet)
            new_letter += alphabet[new_position]
        else:
            new_letter += letter
    print(f"You select {direction}d and result is : {new_letter}")



should_continue = False

while not should_continue:

    enter_direction = input("Type 'encode' to encode a message type and type 'decode' to decode a message: ")
    enter_text = input("Enter plan text here: ").lower()
    enter_shift = int(input("Enter shift number: "))

    caeser(direction=enter_direction, text=enter_text, shift=enter_shift)

    result = input("Please type 'Yes' to continue or 'No' for disconnect.\n").lower()

    if result == "no":
        should_continue = True
        print('GoodBye!')
    # else:
    #     should_continue
