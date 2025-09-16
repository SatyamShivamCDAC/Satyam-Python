# 10. List of prime numbers from 2 to 100

primes = []

for number in range(2, 101):
    for i in range(2, (number // 2) + 1):
        if number % i == 0:
            break
    else:
        primes.append(number)

print(primes)