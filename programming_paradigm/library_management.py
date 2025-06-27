class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        self.__is_checked_out

class Library(Book):
    def __init__(self):
        self.__books = []
    def add_book(self, book):
        self.__books.append(book)
    def list_available_books(self):
        for b in self.__books:
            print(b)

    def check_out_book(self,title):
        if self.title in self.__books:
            self.__books.delete()
    def return_book(self):
        if self.title in self.__books:
            self.__books.append()

