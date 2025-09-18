class Book:
    counter = 0
    def __init__(self,title,author):
        Book.counter += 1

        self.bookid = Book.counter
        self.title = title
        self.is_available = True

