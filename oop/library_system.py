class Book:
    """Represents a general book with a title and an author.
    
    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
    
    Methods:
        __repr__: Returns a string representation of the book.
    """
    def __init__(self, title: str, author: str) -> None:
        self.title = title
        self.author = author  

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}: {self.title} by {self.author}'

class EBook(Book):
    """Represents an electronic book (EBook), a subclass of Book.
    
    In addition to title and author, requires the file size in kilobytes (KB).
    
    Attributes:
        file_size (int): The size of the eBook file in KB.
    
    Methods:
        __repr__: Returns a string representation of the eBook, including file size.
    """
    def __init__(self, title: str, author: str, file_size: int) -> None:
        super().__init__(title, author)
        self.file_size = file_size   

    def __repr__(self) -> str:
        return f'{super().__repr__()}, File Size: {self.file_size}KB'
    
class PrintBook(Book):
    """Represents a printed book, a subclass of Book.
    
    In addition to title and author, requires the page count.
    
    Attributes:
        page_count (int): The number of pages in the book.
    
    Methods:
        __repr__: Returns a string representation of the printed book, including page count.
    """
    def __init__(self, title: str, author: str, page_count: int) -> None:
        super().__init__(title, author)
        self.page_count = page_count
    
    def __repr__(self) -> str:
        return f'{super().__repr__()}, Page Count: {self.page_count}'

class Library:
    """Represents a library that can store a collection of books.
    
    Class Attributes:
        books (list): A list to store book instances.
    
    Instance Attributes:
        name (str): The name of the library.
    
    Methods:
        add_book: Adds a book to the library if it is not already present.
        list_books: Lists all the books in the library.
    """
    books = []

    def __init__(self, name_of_library: str = "") -> None:
        self.name = name_of_library

    def add_book(self, book):
        """Adds a book to the library collection if it is not already present.
        
        Args:
            book (Book): The book to add to the library.
        """
        if book not in Library.books:
            Library.books.append(book)

    def list_books(self):
        """Prints all the books currently in the library collection."""
        for item in Library.books:
            print(item)
