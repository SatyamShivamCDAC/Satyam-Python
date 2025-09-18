from book import Book
from member import Student

class Library:

    def __init__(self,list_of_books):
        self.books = list_of_books

    def addBook(self,book):
        self.books.append(book)
        print(book.name, " add to library")

    def issue_book(self,member,book):
        if book in self.books :
            i = self.books.index(book)
            if self.books[i].is_available:
                member.issued_books.append(book)
                self.books[i].is_available = False
                print("Book issued")
            else:
                print("Book already issued")
        else:
            print("Bok not available")

    def return_book(self, member, book):
        if book in self.books:
            i = self.books.index(book)
            if not self.books[i].is_available:
                member.issued_books.remove(book)
                self.books[i].is_available = True
                print("Book returned")
            else:
                print("Book not issued")

        else:
            print("Bok not available")


book1 = Book("hella","helen")
book2 = Book("abc","ABC")
book3 = Book("pqr","PQR")
book4 = Book("xyz","XYZ")

library = Library([book1,book2,book3,book4])

student1 = Student("Satyam",)

