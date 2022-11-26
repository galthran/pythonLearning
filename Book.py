class Book:

    def __init__(self, isbn, title, author, publisher, pages, price, copies):
        self._isbn = isbn
        self._title = title
        self._author = author
        self._publisher = publisher
        self._pages = pages
        self.price = price
        self._copies = copies

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, val):
        if 50 < val < 1000:
            self._price = val
        else:
            raise ValueError('Price must be between 50 and 1000')

    def display(self):
        print(f'isbn: {self._isbn}, title: {self._title}, price: {self._price}, copies: {self._copies}')

    def in_stock(self):
        return True if self._copies > 0 else False
        # if self._copies > 0:
        #     return True
        # else:
        #     return False

    def sell(self):
        if self.in_stock():
            self._copies -= 1
        else:
            print("The book is out of stock")

        # if self._copies < 1:
        #     print("The book is out of stock")
        # else:
        #     self._copies -= 1


if __name__ == '__main__':
    book1 = Book('957-4-36-547417-1', 'Learn Physics', 'Stephen', 'CBC', 350, 200, 2)
    book2 = Book('652-6-86-748413-3', 'Learn Chemistry', 'Jack', 'CBC', 400, 220, 20)
    book3 = Book('957-7-39-347216-2', 'Learn Maths', 'John', 'XYZ', 500, 300, 5)
    book4 = Book('957-7-39-347216-2', 'Learn Biology', 'Jack', 'XYZ', 400, 200, 6)

    books = [book1, book2, book3, book4]
    # jackBooks = []

    for book in books:
        book.display()
        # if book.author == "Jack":
        #     jackBooks.insert(len(jackBooks), book)

    jack_books = [book.title for book in books if book.author == 'Jack']
    print(jack_books)
