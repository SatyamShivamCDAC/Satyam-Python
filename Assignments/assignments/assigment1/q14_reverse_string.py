# 14. Reverse a string

text = input('Text: ')
reversedText = []

for i in range(-1, -len(text) - 1, -1):
    reversedText.append(text[i])

reversedText = ''.join(reversedText)

print(reversedText)

print(text[::-1])