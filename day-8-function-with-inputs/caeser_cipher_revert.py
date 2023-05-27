alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encode a message type and type 'decode' to decode a message: ")
print(direction)

enter_text = input("Enter plan text here: ").lower()
enter_shift = int(input("Enter un-shift number: "))


def decrypt(text, shift_number):
    new_letter = ''
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position - shift_number) % len(alphabet)
            letter = alphabet[new_position]
            new_letter += letter
        else:
            new_letter += letter
    print(new_letter)


decrypt(text=enter_text, shift_number=enter_shift)


# mdyhg