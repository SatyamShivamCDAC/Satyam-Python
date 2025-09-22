from employee import Employee
class MarketingExecutive(Employee):
    def __init__(self, ename, basic_salary, medical_allowance, distance_travelled):
        super().__init__(ename, basic_salary, medical_allowance)
        self.phone_allowance = 1000
        self.travel_allowance = 5 * distance_travelled
        self.add_to_database()

    def add_to_database(self):
        cursor = Employee.conn.cursor()
        cursor.execute(f'insert ignore into employee_payroll (empid,ename,basic_salary,gross_salary,net_salary,medical_allowance,travel_allowance,phone_allowance) values ({self.empid},"{self.ename}",{self.basic_salary} ,{self.calculate_gross()},{self.calculate_net()},{self.medical_allowance},{self.travel_allowance},{self.phone_allowance})')
        cursor.close()



    def calculate_gross(self):
        return super().calculate_gross() + self.phone_allowance + self.travel_allowance

me = MarketingExecutive("Piyush",700000,15000,12)
