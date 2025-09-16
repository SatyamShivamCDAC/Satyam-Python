# 6. Prime

number = abs(int(input('Number: ')))

if number == 0 or number == 1:
    print(f'{number} is not Prime.')
    exit()

for i in range(2, (number // 2) + 1):
    if number % i == 0:
        print(f'{number} is not Prime.')
        break
else:
    print(f'{number} is Prime')