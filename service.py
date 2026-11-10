from data_layer import Book, Reader
from repository_layer import Repository
def check_text(text, field):
    if not isinstance(text, str):
        raise TypeError(f"{field} должно быть строкой")
    if not text.strip():
        raise ValueError(f"{field} не должно быть пустым")
class LibraryService:
    def __init__(self, books: Repository, readers: Repository):
        self.books = books
        self.readers = readers
    def register_reader(self, name):
        check_text(name, "имя читателя")
        return self.readers.add(Reader(name.strip()))
    def get_readers(self):
        return self.readers.get_all()
    def add_book(self, title, author, year):
        check_text(title, "название книги")
        check_text(author, "имя автора")
        return self.books.add(Book(title.strip(), author.strip(), year))
    def get_books(self):
        return self.books.get_all()
    def give_book(self, book_id, reader_id):
        book = self.books.get(book_id)
        reader = self.readers.get(reader_id)
        if not book.is_available:
            raise ValueError("эта книга уже выдана кому-то другому")  
        book.is_available = False
        reader.borrowed_book_ids.append(book.id)
        self.books.update(book)
        self.readers.update(reader)
    def return_book(self, book_id, reader_id):
        book = self.books.get(book_id)
        reader = self.readers.get(reader_id)
        if book.id not in reader.borrowed_book_ids:
            raise ValueError("у этого читателя нет такой книги")
        book.is_available = True
        reader.borrowed_book_ids.remove(book.id)
        self.books.update(book)
        self.readers.update(reader)