def sum_of_digit(num):
    num1 = num
    sum = 0
    while(num1):
        sum += num1%10
        num1 = num1//10
    return sum