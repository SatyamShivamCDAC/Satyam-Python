def div(a,b):
    if(b==0):
        return "denomerator cant be zero"
    return a/b

while(True):
    a = int(input('Numerator : '))
    b = int(input('Denomerator : '))

    print(div(a,b))

    c = int(input('Press 1 to continue and 0 to exit'))
    if(c == 0):
        break
