from datetime import datetime, timedelta
from models import Checkout
from storage import Storage

class ReminderManager:
    def __init__(self, storage_file="checkouts.json"):
        self.storage = Storage(storage_file)
        self.checkouts = [Checkout.from_dict(checkout) for checkout in self.storage.load()]

    def send_reminders(self, days_before_due=3):
        today = datetime.now().date()
        reminders = []
        for checkout in self.checkouts:
            due_date = datetime.strptime(checkout.due_date, "%Y-%m-%d").date()
            if due_date - today <= timedelta(days=days_before_due):
                reminders.append(checkout)
        self._print_reminders(reminders)

    def _print_reminders(self, reminders):
        if not reminders:
            print("No reminders to send.")
        for reminder in reminders:
            print(f"Reminder: User ID {reminder.user_id}, Book ISBN {reminder.isbn} is due on {reminder.due_date}.")

# Example usage:
# reminder_manager = ReminderManager()
# reminder_manager.send_reminders()
