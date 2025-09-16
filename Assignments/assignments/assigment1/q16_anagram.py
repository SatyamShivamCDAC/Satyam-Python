# 16. Anagram

text = input('Text: ')

if text == text[::-1]:
    print(f'{text} is Anagram.')
else:
    print(f'{text} is not Anagram.')