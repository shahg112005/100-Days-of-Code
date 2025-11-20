from caesarcipherart import logo


# Description
# A simple program for practicing functions with parameters

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesarcipher(text, shift, encode_decode):
        output_text = '' # -> encrypted text or decrypted text

        if encode_decode == 'decode':
            shift *= -1

        for letter in text:
            if letter not in alphabets:
                output_text += letter
            else:
                i = alphabets.index(letter) + shift
                i %= len(alphabets)
                output_text += alphabets[i]
        print(output_text)

print(logo)

game_over = False

while not game_over:


    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    user_text = input("Type your message:\n").lower()
    user_shift = int(input("Type the shift number:\n"))

    caesarcipher(text=user_text, shift=user_shift, encode_decode= direction)

    y = input('Type whether go again or stop -> ')
    if y == 'stop':
        game_over = True