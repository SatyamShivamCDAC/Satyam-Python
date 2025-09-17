# 17. Swap Case of each Vowel

text = input('Text: ')

vowels = ('a', 'e', 'i', 'o', 'u')

swapped_case = []
for char in text:
    if char.lower() in vowels:
        if char.islower():
            swapped_case.append(char.upper())
        else:
            swapped_case.append(char.lower())
    else:
        swapped_case.append(char)

swapped_case = ''.join(swapped_case)
print(swapped_case)