# 15. Pangram

text = input('Text: ')
letters = set()

for char in text:
    if char.isalpha():
        letters.add(char.lower())

if len(letters) == 26:
    print('Given text is pangram.')
else:
    print('Given text is not pangram.')