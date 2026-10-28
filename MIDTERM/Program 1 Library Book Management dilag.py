class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"Book: {self.title} | Author: {self.author}\nPrice: PHP {self.price:.2f}"

class EBook(Book):
    def __init__(self, title, author, price, file_size_mb):
        super().__init__(title, author, price)
        self.file_size_mb = file_size_mb

    def __str__(self):
        return f"EBook: {self.title} | Author: {self.author}\nPrice: PHP {self.price:.2f} | File size: {self.file_size_mb} MB"

book1 = Book("Python Basics", "Maria Santos", 450.00)
ebook1 = EBook("Learning OOP", "Ana Cruz", 300.00, 5)
ebook2 = EBook("Advanced Python", "Marceal Dilag", 550.00, 12)


print(book1)
print()
print(ebook1)
print()
print(ebook2)
