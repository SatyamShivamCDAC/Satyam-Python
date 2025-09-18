class Calculator:
    def add(self,*args):
        sum = 0
        for i in args:
            sum += i
        return sum

    def sub(self,*args):
        result = 2*args[0]
        for i in args:
            result =  result - i
        return result

    def mul(self,*args):
        result  = 1
        for i in args:
            result *= i
        return result

    def div(self,a,b):
        return a/b






