class Book:
    def __init__(self, title: str, author: str, year: int) -> None:
        self.title = title
        self.author = author
        self.year = year

    def __str__(self) -> str:
        return "{} by {}, published in {}".format(self.title, self.author, self.year)

    def __repr__(self) -> str:
        return f"Book('{self.title}', '{self.author}', {self.year})"


def main():
    # Creating an instance of Book
    my_book = Book("1984", "George Orwell", 1949)

    # Demonstrating the __str__ method
    print(my_book)  # Expected to use __str__

    # Demonstrating the __repr__ method
    print(repr(my_book))  # Expected to use __repr__

    # Deleting a book instance to trigger __del__
    # del my_book


if __name__ == "__main__":
    main()
