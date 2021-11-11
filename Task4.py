class Book:
    count = 0

    def __init__(self, pages, price):
        self.pages = pages
        self.price = price
        Book.count += 1

    def getPrice(self):
        return self.price

    def getPages(self):
        return self.pages

    def weight(self):
        return self.pages * 1.5 + 200  # вес книги в граммах

    @staticmethod
    def byn_to_usd(price_byn):
        return price_byn // 2.45

    @classmethod
    def count_book(cls):
        print('Количество книг:', cls.count)


book1 = Book(365, 15)
book2 = Book(128, 25)
print('book1.weight:', book1.weight())
print('book2.weight:', book2.weight())
Book.count_book()


class ForeignBook(Book):
    def __init__(self, pages, price, language):
        Book.__init__(self, pages, price)
        self.language = language


englishBook = ForeignBook(320, 45, 'English')
