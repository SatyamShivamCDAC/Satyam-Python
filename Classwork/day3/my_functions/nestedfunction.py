def a():
    print('this is a funtion')
    for i in range(1,3):
        b()

def b():
    for  i in range(1,6):
        print('welcome : ',i)

a()