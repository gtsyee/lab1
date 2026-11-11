class Book:
    def __init__(self, title, author, year):
        self.id = None 
        self.title = title
        self.author = author
        self.year = year
        self.is_available = True
class Reader:
    def __init__(self, name):
        self.id = None
        self.name = name
        self.borrowed_book_ids = [] #id взятых книг