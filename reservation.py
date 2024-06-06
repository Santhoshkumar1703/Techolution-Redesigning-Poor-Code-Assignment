from models import Checkout
from storage import Storage
from datetime import datetime

class ReservationManager:
    def __init__(self, storage_file="reservations.json"):
        self.storage = Storage(storage_file)
        self.reservations = [Checkout.from_dict(reservation) for reservation in self.storage.load()]

    def reserve_book(self, user_id, isbn):
        new_reservation = Checkout(user_id, isbn, (datetime.now()).strftime("%Y-%m-%d"))
        self.reservations.append(new_reservation)
        self.save_reservations()
        print("Book reserved.")

    def list_reservations(self):
        if not self.reservations:
            print("No reservations available.")
        for reservation in self.reservations:
            print(reservation)

    def save_reservations(self):
        self.storage.save([reservation.to_dict() for reservation in self.reservations])
