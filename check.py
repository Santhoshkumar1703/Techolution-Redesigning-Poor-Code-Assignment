from models import Checkout
from storage import Storage
from datetime import datetime, timedelta

class CheckoutManager:
    def __init__(self, storage_file="checkouts.json"):
        self.storage = Storage(storage_file)
        self.checkouts = [Checkout.from_dict(checkout) for checkout in self.storage.load()]

    def checkout_book(self, user_id, isbn, days=14):
        due_date = (datetime.now() + timedelta(days=days)).strftime("%Y-%m-%d")
        new_checkout = Checkout(user_id, isbn, due_date)
        self.checkouts.append(new_checkout)
        self.save_checkouts()
        print("Book checked out.")

    def list_checkouts(self):
        if not self.checkouts:
            print("No checkouts available.")
        for checkout in self.checkouts:
            print(checkout)

    def checkin_book(self, user_id, isbn):
        for checkout in self.checkouts:
            if checkout.user_id == user_id and checkout.isbn == isbn and not checkout.returned:
                checkout.returned = True
                self.save_checkouts()
                print("Book checked in.")
                return
        print("Checkout record not found or already returned.")

    def save_checkouts(self):
        self.storage.save([checkout.to_dict() for checkout in self.checkouts])
