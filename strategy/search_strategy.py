
from abc import ABC, abstractmethod
from database.database import Database

class BookSearchStrategy(ABC):
    @abstractmethod
    def search(self, term):
        pass

class SearchByTitle(BookSearchStrategy):
    def search(self, title):
        db = Database()
        return db.execute('SELECT * FROM books WHERE name = %s', (title,))

class SearchByAuthor(BookSearchStrategy):
    def search(self, author):
        db = Database()
        return db.execute('SELECT * FROM books WHERE author = %s', (author,))

class SearchByCategory(BookSearchStrategy):
    def search(self, category):
        db = Database()
        return db.execute('SELECT * FROM books WHERE category = %s', (category,))
