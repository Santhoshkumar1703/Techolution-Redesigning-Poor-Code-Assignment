import json
from datetime import datetime, timedelta

class Item:
    def __init__(self, title, item_type):
        self.title = title
        self.item_type = item_type

    def to_dict(self):
        return {
            "title": self.title,
            "item_type": self.item_type
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["title"], data["item_type"])

class Book(Item):
    def __init__(self, title, author, isbn, due_date=None, late_fee=0):
        super().__init__(title, "Book")
        self.author = author
        self.isbn = isbn
        self.due_date = due_date
        self.late_fee = late_fee

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "author": self.author,
            "isbn": self.isbn,
            "due_date": self.due_date,
            "late_fee": self.late_fee
        })
        return data

    @classmethod
    def from_dict(cls, data):
        return cls(data["title"], data["author"], data["isbn"], data.get("due_date"), data.get("late_fee"))

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn}, Due Date: {self.due_date}, Late Fee: {self.late_fee})"

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def to_dict(self):
        return {
            "name": self.name,
            "user_id": self.user_id
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["user_id"])

    def __str__(self):
        return f"{self.name} (ID: {self.user_id})"

class Checkout:
    def __init__(self, user_id, isbn, due_date, returned=False):
        self.user_id = user_id
        self.isbn = isbn
        self.due_date = due_date
        self.returned = returned

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "isbn": self.isbn,
            "due_date": self.due_date,
            "returned": self.returned
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["user_id"], data["isbn"], data["due_date"], data["returned"])

    def __str__(self):
        return f"User ID: {self.user_id}, Book ISBN: {self.isbn}, Due Date: {self.due_date}, Returned: {self.returned}"
