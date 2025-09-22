import pymysql as p

class Employee:
    conn = p.connect(host = "localhost",user= "root",passwd="root",database="satyam",autocommit=True)

    emp_count = 0
    def __init__(self,ename,basic_salary,medical_allowance):
        Employee.emp_count += 1

        self.empid = Employee.emp_count
        self.ename = ename
        self.basic_salary = basic_salary
        self.pf = 0.12*basic_salary
        self.pt = 200
        self.hra = 0.5*basic_salary
        self.medical_allowance = medical_allowance
        cursor = Employee.conn.cursor()
        print(f'insert into employee_payroll (empid,ename,basic_salary,gross_salary,net_salary,medical_allowance) values ({self.empid},"{self.ename}",{self.basic_salary},{self.calculate_gross()},{self.calculate_net()},{self.medical_allowance})')

        cursor.execute(f'create table if not exists employee_payroll (empid int primary key,ename varchar(50),basic_salary int,net_salary int,gross_salary int,medical_allowance int,food_allowance int, other_allowance int,travel_allowance int,phone_allowance int)')
        print(f'insert into employee_payroll (empid,ename,basic_salary,gross_salary,net_salary,medical_allowance) values ({self.empid},"{self.ename}",{self.basic_salary},{self.calculate_gross()},{self.calculate_net()},{self.medical_allowance})')
        # self.add_to_database()
        cursor.close()


    def update_database(self,column,item):
        cursor = Employee.conn.cursor()
        cursor.execute(f'update employee_payroll set {column} = {item} where id = {self.id}')
        cursor.close()

    def delete_from_database(self):
        cursor = Employee.conn.cursor()
        cursor.execute(f'delete from employee_payroll where id = {self.id}')
        cursor.close()

    def add_to_database(self):
        cursor = Employee.conn.cursor()
        cursor.execute(f'insert ignore into employee_payroll (empid,ename,basic_salary,gross_salary,net_salary,medical_allowance) values ({self.empid},"{self.ename}",{self.basic_salary} ,{self.calculate_gross()},{self.calculate_net()},{self.medical_allowance})')
        cursor.close()

    @staticmethod
    def display_all():
        cursor = Employee.conn.cursor()
        cursor.execute(f'select empid,ename,basic_salary,gross_salary,net_salary from employee_payroll')
        data = cursor.fetchall()
        print(data)
        cursor.close()

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



Employee.display_all()
