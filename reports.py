from models import Checkout
from storage import Storage
from collections import Counter
from datetime import datetime

class ReportManager:
    def __init__(self, storage_file="checkouts.json"):
        self.storage = Storage(storage_file)
        self.checkouts = [Checkout.from_dict(checkout) for checkout in self.storage.load()]

    def generate_overdue_report(self):
        today = datetime.now().date()
        overdue_books = [checkout for checkout in self.checkouts if datetime.strptime(checkout.due_date, "%Y-%m-%d").date() < today]
        self._print_overdue_report(overdue_books)

    def generate_most_checked_out_report(self):
        isbn_counts = Counter(checkout.isbn for checkout in self.checkouts)
        most_checked_out = isbn_counts.most_common()
        self._print_most_checked_out_report(most_checked_out)

    def _print_overdue_report(self, overdue_books):
        if not overdue_books:
            print("No overdue books.")
        for book in overdue_books:
            print(f"Overdue: User ID {book.user_id}, Book ISBN {book.isbn}, Due Date {book.due_date}")

    def _print_most_checked_out_report(self, most_checked_out):
        if not most_checked_out:
            print("No checkouts recorded.")
        for isbn, count in most_checked_out:
            print(f"ISBN: {isbn}, Checkouts: {count}")

# Example usage:
# report_manager = ReportManager()
# report_manager.generate_overdue_report()
# report_manager.generate_most_checked_out_report()
