def even_odd(number):
    if number % 2 == 0:
        print(number, 'is Even.')
    else:
        print(number, 'is Odd.')

numb = int(input("Number : "))
even_odd(numb)