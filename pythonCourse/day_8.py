alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
    if direction=="decode":
        shift = shift*-1
    final = ""
    for letter in range(0, len(text)):
        newIndex = (alphabet.index(text[letter])+shift)%len(alphabet)
        final+=alphabet[newIndex]
    print ("The text is", final)

from day_8_art import logo
print(logo)
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)