from book import BookManager
from user import UserManager
from check import CheckoutManager
from reservation import ReservationManager
from reminder import ReminderManager
from advanced_search import AdvancedSearchManager
from reports import ReportManager

def main_menu():
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. List Books")
    print("3. Update Book")
    print("4. Delete Book")
    print("5. Search Books")
    print("6. Add User")
    print("7. List Users")
    print("8. Update User")
    print("9. Delete User")
    print("10. Search Users")
    print("11. Checkout Book")
    print("12. Checkin Book")
    print("13. Calculate Late Fee")
    print("14. Reserve Book")
    print("15. List Reservations")
    print("16. Send Reminders")
    print("17. Advanced Search Books")
    print("18. Generate Overdue Report")
    print("19. Generate Most Checked Out Report")
    print("20. Exit")
    choice = input("Enter choice: ")
    return choice

def main():
    book_manager = BookManager()
    user_manager = UserManager()
    checkout_manager = CheckoutManager()
    reservation_manager = ReservationManager()
    reminder_manager = ReminderManager()
    search_manager = AdvancedSearchManager()
    report_manager = ReportManager()

    while True:
        choice = main_menu()
        if choice == '1':
            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            book_manager.add_book(title, author, isbn)
        elif choice == '2':
            book_manager.list_books()
        elif choice == '3':
            isbn = input("Enter ISBN of the book to update: ")
            title = input("Enter new title (or leave blank to keep current): ")
            author = input("Enter new author (or leave blank to keep current): ")
            due_date = input("Enter new due date (YYYY-MM-DD) (or leave blank to keep current): ")
            late_fee = input("Enter new late fee (or leave blank to keep current): ")
            book_manager.update_book(isbn, title or None, author or None, due_date or None, float(late_fee) if late_fee else None)
        elif choice == '4':
            isbn = input("Enter ISBN of the book to delete: ")
            book_manager.delete_book(isbn)
        elif choice == '5':
            title = input("Enter title (or leave blank): ")
            author = input("Enter author (or leave blank): ")
            isbn = input("Enter ISBN (or leave blank): ")
            results = search_manager.search_books(title=title or None, author=author or None, isbn=isbn or None)
            for book in results:
                print(book)
        elif choice == '6':
            name = input("Enter user name: ")
            user_id = input("Enter user ID: ")
            user_manager.add_user(name, user_id)
        elif choice == '7':
            user_manager.list_users()
        elif choice == '8':
            user_id = input("Enter user ID of the user to update: ")
            name = input("Enter new name (or leave blank to keep current): ")
            user_manager.update_user(user_id, name or None)
        elif choice == '9':
            user_id = input("Enter user ID of the user to delete: ")
            user_manager.delete_user(user_id)
        elif choice == '10':
            name = input("Enter name (or leave blank): ")
            user_id = input("Enter user ID (or leave blank): ")
            results = user_manager.search_users(name=name or None, user_id=user_id or None)
            for user in results:
                print(user)
        elif choice == '11':
            user_id = input("Enter user ID: ")
            isbn = input("Enter ISBN of the book to checkout: ")
            days = input("Enter number of days for checkout (default is 14): ")
            checkout_manager.checkout_book(user_id, isbn, int(days) if days else 14)
        elif choice == '12':
            user_id = input("Enter user ID: ")
            isbn = input("Enter ISBN of the book to checkin: ")
            checkout_manager.checkin_book(user_id, isbn)
        elif choice == '13':
            isbn = input("Enter ISBN of the book to calculate late fee: ")
            late_fee = book_manager.calculate_late_fee(isbn)
            print(f"Late fee for book with ISBN {isbn}: {late_fee}")
        elif choice == '14':
            user_id = input("Enter user ID: ")
            isbn = input("Enter ISBN of the book to reserve: ")
            reservation_manager.reserve_book(user_id, isbn)
        elif choice == '15':
            reservation_manager.list_reservations()
        elif choice == '16':
            reminder_manager.send_reminders()
        elif choice == '17':
            title = input("Enter title (or leave blank): ")
            author = input("Enter author (or leave blank): ")
            isbn = input("Enter ISBN (or leave blank): ")
            results = search_manager.search_books(title=title or None, author=author or None, isbn=isbn or None)
            for book in results:
                print(book)
        elif choice == '18':
            report_manager.generate_overdue_report()
        elif choice == '19':
            report_manager.generate_most_checked_out_report()
        elif choice == '20':
            print("Exiting.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
