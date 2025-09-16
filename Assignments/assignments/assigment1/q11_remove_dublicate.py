# 11. Remove duplicates from list

numbers = [1, 2, 3, 2, 1, 3, 3]
uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)

print(uniques)