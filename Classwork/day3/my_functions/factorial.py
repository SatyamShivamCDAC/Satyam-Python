def factorial(num):
    fac = 1
    for i in range(1,num+1):
        fac = fac*i
    return fac
print(factorial(4))