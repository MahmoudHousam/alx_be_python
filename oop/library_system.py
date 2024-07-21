class Book:
    def __init__(self, title, author) -> None:
        self.title = title
        self.author = author

    def __str__(self) -> str:
        return "Book: {} by {}".format(self.title, self.author)


class EBook(Book):
    def __init__(self, title, author, file_size) -> None:
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self) -> str:
        return "EBook: {} by {}, File Size: {}KB".format(
            self.title, self.author, self.file_size
        )


class PrintBook(Book):
    def __init__(self, title, author, page_count) -> None:
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self) -> str:
        return "PrintBook: {} by {}, Page Count: {}".format(
            self.title, self.author, self.page_count
        )


class Library:
    def __init__(self, book) -> None:
        self.book = book
        self.book_title
