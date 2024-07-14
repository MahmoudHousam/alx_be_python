class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        # self._is_checked_out


class Library:
    def __init__(self):
        self._books = []
        self._authors = []

    def add_book(self, Book):
        self._books.append(Book.title)
        self._authors.append(Book.author)

    def list_available_books(self):
        for book, author in zip(self._books, self._authors):
            print(f"{book} by {author}")

    def check_out_book(self, book):
        if book in self._books:
            self._books.remove(book)

    def return_book(self, book):
        if book not in self._books:
            self._books.append(book)
