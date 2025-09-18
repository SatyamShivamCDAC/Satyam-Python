class Student:
    co = 1
    def __init__(self,name,marks):
        self.id = Student.co
        self.name = name
        self.marks = marks
        Student.co += 1
    def __str__(self):
        return f"{self.id} {self.name}"

    def cal_percent(self):
        total = 0
        for mark in self.marks.values():
            total += mark
        percentage = total/(len(self.marks) * 100) * 100
        return percentage



satyam = Student('Satyam', {"maths":92,"physics":91,"chemistry":90})
shivam = Student('Shivam', {"maths":90,"physics":11,"chemistry":10})
piyush = Student('Piyush', {"maths":80,"physics":51,"chemistry":81})
umang = Student('Umang', {"maths":70,"physics":61,"chemistry":90})



print(satyam.cal_percent())
print(shivam.cal_percent())

students = [satyam,shivam,piyush,umang]

max = 0
min = students[0].cal_percent()
print(min)
for student in students:
    if student.cal_percent()>max:
        max = student.cal_percent()
    if student.cal_percent()<min:
        min = student.cal_percent()

print("Max percent ",max)
print("Min percent ",min)