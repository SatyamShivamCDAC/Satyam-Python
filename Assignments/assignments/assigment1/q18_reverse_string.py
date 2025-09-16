sentence = input('Sentence: ')
words = sentence.split(' ')

# reversedSentence = []
# for word in words:
#     reversedSentence.append(word[::-1])

reversedSentence = []
for word in words:
    revered_word = []
    for i in range(-1, -len(word) - 1, -1):
        revered_word.append(word[i])
    revered_word = ''.join(revered_word)
    reversedSentence.append(revered_word)

reversedSentence = ' '.join(reversedSentence)

print(reversedSentence)