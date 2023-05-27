alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encode a message type and type 'decode' to decode a message: ")
print(direction)

enter_text = input("Enter plan text here: ").lower()
enter_shift = int(input("Enter shift number: "))


def encrypt(message_text, shift_text):
    caesar_message = ''
    for letter in message_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift_text) % len(alphabet)
            new_letter = alphabet[new_position]
            caesar_message += new_letter
        else:
            caesar_message += letter
    print(caesar_message)


encrypt(enter_text, enter_shift)

