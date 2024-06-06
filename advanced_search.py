from models import Book
from storage import Storage

class AdvancedSearchManager:
    def __init__(self, storage_file="books.json"):
        self.storage = Storage(storage_file)
        self.books = [Book.from_dict(book) for book in self.storage.load()]

    def search_books(self, title=None, author=None, isbn=None):
        results = self.books
        if title:
            results = [book for book in results if title.lower() in book.title.lower()]
        if author:
            results = [book for book in results if author.lower() in book.author.lower()]
        if isbn:
            results = [book for book in results if isbn.lower() in book.isbn.lower()]
        return results

# Example usage:
# search_manager = AdvancedSearchManager()
# results = search_manager.search_books(title="Some Title", author="Some Author")
# for book in results:
#     print(book)
