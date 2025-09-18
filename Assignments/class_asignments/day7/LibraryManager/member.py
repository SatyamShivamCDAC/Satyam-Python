from book import Book

class Student:
    counter = 0

    def __init__(self,name):
        Student.counter += 1

        self.memberid = Student.counter
        self.name = name
        self.issued_books = []