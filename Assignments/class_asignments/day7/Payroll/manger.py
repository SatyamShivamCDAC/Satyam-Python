from employee import Employee

class Manager(Employee):

    def __init__(self,ename,basic_salary,medical_allowance):
        super().__init__(ename,basic_salary,medical_allowance)
        self.manager_allowance = 0.08 * basic_salary
        self.food_allowance = 0.1 * basic_salary
        self.other_allowance = 0.03 * basic_salary

    def calculate_gross(self):
        gross = super().calculate_gross() + self.medical_allowance + self.food_allowance + self.other_allowance
        return gross

manganger1 = Manager("Arbab",2000000,50000)

print(manganger1)