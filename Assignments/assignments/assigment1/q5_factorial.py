# 5. Factorial of a number

number = int(input('Number: '))

factorial = 1
for i in range(2, number + 1):
    factorial *= i

print(f'Factorial of {number} is {factorial}.')