def add_n_numbers(*args):
    sum = 0
    for num in args:
        sum += num

    return sum

print("Sum of numbers : ",add_n_numbers( 1,2,3,4))
