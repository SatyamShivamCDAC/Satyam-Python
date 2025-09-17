def swap(a,b):
    print(a, b)
    a, b = b, a
    print( "a : ",a," b : ", b)


num1 = int(input("a : "))
num2 = int(input("b : "))

swap(num1,num2)