class Calculator:
    def add(self,*args):
        sum = 0
        for i in args:
            sum += i
        return sum

    def sub(self,*args):
        result = 0
        for i in args:
            result -= i
        return result

    def mul(self,*args):
        result  = 1
        for i in args:
            result *= i
        return result

    def div(self,a,b):
        return a/b



cal = Calculator()

print(cal.add(1,2,3,4,5))


