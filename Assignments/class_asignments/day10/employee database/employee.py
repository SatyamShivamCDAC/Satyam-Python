from databas_ops import MySqlOps

class Employee:
    e_count= 0
    def __init__(self,eid,ename,esalary):
        Employee.e_count += 1
        self.empid = Employee.e_count
        self.ename = ename
        self.esalary = esalary

    def add_to_database(self):
        MySqlOps.add_record(self)

    def delete_from_database(self):
        MySqlOps.delete(self.empid)

    def update_instance(self):
        pass