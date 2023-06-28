# Розробіть клас Library для представлення бібліотеки.
# А також класс Book для представлення книги. Класс Library повинен мати атрибут books зі списком книжок.
# Кожна книга в бібліотеці має атрибути, такі як назва, автор і рік видання.
# Додайте метод add_book, який додає нову книгу до бібліотеки. Реалізуйте метод __str__,
# який виводить список книг у бібліотеці.
# Створіть об'єкт Library і додайте кілька книг. Виведіть список книг у бібліотеці.
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author}, {self.year}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def __str__(self):
        if not self.books:
            return "No books in the library."
        return "\n".join(str(book) for book in self.books)


library = Library()

book1 = Book("Компютерные сети", "В. Олифер, Н. Олифер", 2016)
book2 = Book("Посібник користувача windows 8.1", "microsoft", 2015)
book3 = Book("Name book", "name author", 2023)

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print(library)
