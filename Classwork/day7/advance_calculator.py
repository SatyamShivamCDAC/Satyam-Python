from Classwork.day6.calculator import Calculator

class AdvCalculator(Calculator):
    def div(self,a,b,c):
        return b/a/c

calc1 = Calculator()
calc2 = AdvCalculator()

print(calc1.div(10,5))
print(calc2.div(10,5,2))
