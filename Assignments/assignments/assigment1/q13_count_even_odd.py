# 13. Count prime and odd numbers in tuple

numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

number_of_odds = 0
number_of_primes = 0

for number in numbers:
    if number % 2 != 0:
        number_of_odds += 1

    if number == 0 or number == 1:
        continue

    for i in range(2, (number // 2) + 1):
        if number % i == 0:
            break
    else:
        number_of_primes += 1

print(f'Number of Odds: {number_of_odds}')
print(f'Number of Primes: {number_of_primes}')