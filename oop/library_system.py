class Book:
    def __init__(self, title, author) -> None:
        self.title = title
        self.author = author

    def __str__(self) -> str:
        return "Book: {} by {}".format(self.title, self.author)

    def book_details(self):
        return [f"{self.title}", f"{self.author}"]


class EBook(Book):
    def __init__(self, title, author, file_size) -> None:
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self) -> str:
        return "EBook: {} by {}, File Size: {}KB".format(
            self.title, self.author, self.file_size
        )

    def book_details(self):
        return [f"{self.title}", f"{self.author}", f"{self.file_size}"]


class PrintBook(Book):
    def __init__(self, title, author, page_count) -> None:
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self) -> str:
        return "PrintBook: {} by {}, Page Count: {}".format(
            self.title, self.author, self.page_count
        )

    def book_details(self):
        return [f"{self.title}", f"{self.author}", f"{self.page_count}"]


class Library:
    def __init__(self) -> None:
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            if isinstance(book, EBook):
                print(
                    f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB"
                )
            elif isinstance(book, PrintBook):
                print(
                    f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}"
                )
            else:
                print(f"Book: {book.title} by {book.author}")


def main():
    # Create a Library instance
    my_library = Library()

    # Create instances of each type of book
    classic_book = Book("Pride and Prejudice", "Jane Austen")
    digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
    paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    # Add books to the library
    my_library.add_book(classic_book)
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)

    # List all books in the library
    my_library.list_books()


if __name__ == "__main__":
    main()
