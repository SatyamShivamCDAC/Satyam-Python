from manger import Manager
from marketing_executive import MarketingExecutive

try:
    emp1 = Manager("Satyam",12000000,300)
except:
    print("medical Allowance Exception")

print(emp1.basic_salary)