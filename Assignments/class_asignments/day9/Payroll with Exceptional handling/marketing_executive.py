from employee import Employee
class MarketingExecutive(Employee):
    def __init__(self, ename, basic_salary, medical_allowance, distance_travelled = 0):
        super().__init__(ename, basic_salary, medical_allowance)
        self.phone_allowance = 1000
        self.travel_allowance = 5 * distance_travelled

    def calculate_gross(self):
        return super().calculate_gross() + self.phone_allowance + self.travel_allowance

me = MarketingExecutive("Piyush",700000,15000,12)
print(me)