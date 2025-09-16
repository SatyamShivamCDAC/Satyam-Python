#list of word with 2 or more vowels

texts = ['Apple', 'Elephant', 'Mango', 'Orange', 'Cat']

vowels = ('a', 'e', 'i', 'o', 'u')

texts_vowels = []

for word in texts:
    vowelCount = 0
    for char in word:
        if char.lower() in vowels:
            vowelCount += 1

    if vowelCount >= 2:
        texts_vowels.append(word)


print(texts_vowels)