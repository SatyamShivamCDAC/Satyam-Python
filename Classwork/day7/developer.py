from Classwork.day6.oopDemo import Employee

class Developer(Employee):
    def __init__(self,eid,ename,esalary):
        super().__init__(eid,ename,esalary)
    pass


e = Employee(1,'abc',7000)
d1 = Developer(e.eid,e.ename,e.esalary)

d2 = Developer(2,'xyz',5000)

e.hello()
d1.hello()
d2.hello()