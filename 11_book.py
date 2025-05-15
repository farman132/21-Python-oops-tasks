class Book:
    total_books = 0

    def __init__(self):
        Book.total_books += 1

    @classmethod
    def count(cls):
        print(f"Books: {cls.total_books}")

b1 = Book()
b2 = Book()
Book.count()

