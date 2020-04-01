from string import ascii_lowercase


LETTERS = {letter: int(index) for index, letter in enumerate(ascii_lowercase, start=1)} 

def alphabet_position(text):
    text = text.lower()

    numbers = [LETTERS[character] for character in text if character in LETTERS]

    return ' '.join(numbers)

word = input()
a = [char for char in word]
s = 0 
for i in a:
    O = LETTERS[i]
    s = s+O

print(s)
