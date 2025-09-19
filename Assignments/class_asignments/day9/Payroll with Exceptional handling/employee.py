from medicalallowance_exception import MedicalAllowanceException

class Employee:
    emp_count = 0
    def __init__(self,ename,basic_salary,medical_allowance):
        Employee.emp_count += 1

        self.empid = Employee.emp_count
        self.ename = ename
        self.basic_salary = basic_salary
        self.pf = 0.12*basic_salary
        self.pt = 200
        self.hra = 0.5*basic_salary
        if(medical_allowance >= 2000):
            raise MedicalAllowanceException("minimum of Rs. 2000 is allowed ..please write the employee detail again")
        self.medical_allowance = medical_allowance


    def calculate_gross(self):
        gross = self.basic_salary + self.hra + self.medical_allowance
        return gross

    def calculate_net(self):
        net = self.calculate_gross()-self.pf-self.pt
        return net

    def salary_info(self):
        print(f'pf = {self.pf} pt = {self.pt} hra = {self.hra} \n Gross Salary = {self.calculate_gross()}  Net Salary = {self.calculate_net()}')

    def __str__(self):
        return f'{self.empid}. {self.ename} salary -> {self.calculate_net()}'

