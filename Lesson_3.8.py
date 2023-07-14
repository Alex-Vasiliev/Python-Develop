# Створіть клас Book який має такі атрибути як рік видання, назву, автор та кількість сторінок.
# Створіть статік метод який буде приймати список книжок та рік,
# та повертати кількість книжок з цього списку які були опубліковані у цьому році.

class Book:
    books = []

    def __init__(self, title, author, year, pages):
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages
        Book.books.append(self)

    @staticmethod
    def numbers_book(year):
        count = 0
        for book in Book.books:
            if book.year == year:
                count += 1
        return count


book1 = Book("Компютерные сети", "В. Олифер, Н. Олифер", 2016, 200)
book2 = Book("Посібник користувача windows 8.1", "microsoft", 2015, 500)
book3 = Book("Name book", "name author", 2023, 250)
book4 = Book("Name book", "Name author", 2016, 200)

print(Book.numbers_book(2016))
