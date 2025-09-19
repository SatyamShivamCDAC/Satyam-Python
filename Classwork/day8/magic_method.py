class Employee:
    def __init__(self,empid,ename,esalary):
        self.empid = empid
        self.ename = ename
        self.esalary = esalary

    def displayInfo(self):
        print(f'empid : {self.empid} \n ename : {self.ename} \n esalary : {self.esalary}')

    def __repr__(self):
        represent = {"empid" : self.empid , "ename" : self.ename , "esalary" : self.esalary}
        return str(represent)

    def __str__(self):
        represent = {"empid": self.empid, "ename": self.ename, "esalary": self.esalary}
        return str(represent)

    def __eq__(self, other):
        return self.empid == other.empid

    def __lt__(self, other):
        return self.empid < other.empid

    def __gt__(self,other):
        return self.empid > other.empid



e1 = Employee(101,"Satyam",6000000)
e2 = Employee(102,"Shivam",1200000)
e3 = Employee(103,"Umang",3000000)
e4 = Employee(101,"Satyam",6000000)

l = [e1,e2,e3,e4]
print(e1)
l.sort()


print(e1==e4)

