# 17. Swap Case

text = input('Text: ')
print(text.swapcase())

swapped_case = []
for char in text:
    if char.isalpha():
        if char.islower():
            swapped_case.append(char.upper())
        else:
            swapped_case.append(char.lower())
    else:
        swapped_case.append(char)

swapped_case = ''.join(swapped_case)
print(swapped_case)