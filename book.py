from models import Book
from storage import Storage
from datetime import datetime, timedelta

class BookManager:
    def __init__(self, storage_file="books.json"):
        self.storage = Storage(storage_file)
        self.books = [Book.from_dict(book) for book in self.storage.load()]

    def add_book(self, title, author, isbn):
        new_book = Book(title, author, isbn)
        self.books.append(new_book)
        self.save_books()
        print("Book added.")

    def update_book(self, isbn, title=None, author=None, due_date=None, late_fee=None):
        for book in self.books:
            if book.isbn == isbn:
                if title:
                    book.title = title
                if author:
                    book.author = author
                if due_date:
                    book.due_date = due_date
                if late_fee:
                    book.late_fee = late_fee
                self.save_books()
                print("Book updated.")
                return
        print("Book not found.")

    def delete_book(self, isbn):
        self.books = [book for book in self.books if book.isbn != isbn]
        self.save_books()
        print("Book deleted if existed.")

    def list_books(self):
        if not self.books:
            print("No books available.")
        for book in self.books:
            print(book)

    def search_books(self, **kwargs):
        results = self.books
        for key, value in kwargs.items():
            results = [book for book in results if getattr(book, key, None) == value]
        return results

    def save_books(self):
        self.storage.save([book.to_dict() for book in self.books])

    def calculate_late_fee(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.due_date and datetime.strptime(book.due_date, "%Y-%m-%d") < datetime.now():
                    overdue_days = (datetime.now() - datetime.strptime(book.due_date, "%Y-%m-%d")).days
                    return overdue_days * book.late_fee
        return 0
