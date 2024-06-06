# Techolution-Redesigning-Poor-Code-Assignment
# 📚 Library Management System

Welcome to the Library Management System! This project is designed to manage library operations, including book management, user management, book checkouts, reservations, reminders, and generating reports.

## Features 🚀

- **Book Management** 📚
  - Add, update, delete, and list books
  - Search books by title, author, and ISBN
  - Calculate late fees for overdue books

- **User Management** 👤
  - Add, update, delete, and list users
  - Search users by name and user ID

- **Checkout Management** 📅
  - Checkout books to users
  - Checkin returned books
  - List all checkouts

- **Book Reservations** 🔖
  - Reserve books for users
  - List all reservations

- **Reminders** ⏰
  - Send reminders for due dates

- **Advanced Search** 🔍
  - Perform advanced search for books by title, author, and ISBN

- **Reports** 📊
  - Generate overdue books report
  - Generate most checked-out books report

## Installation 🛠️

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/library-management-system.git
   ```

2. Navigate to the project directory:
   ```bash
   cd library-management-system
   ```

3. Install the required dependencies (if any):
   ```bash
   pip install -r requirements.txt
   ```

## Usage 📖

Run the `main.py` file to start the Library Management System:
```bash
python main.py
```

Follow the on-screen menu to perform various library operations.

## File Structure 📁

- `models.py`: Contains the classes for `Item`, `Book`, `User`, and `Checkout`.
- `book.py`: Manages book-related operations.
- `user.py`: Manages user-related operations.
- `check.py`: Manages book checkouts and returns.
- `reservation.py`: Manages book reservations.
- `reminder.py`: Manages sending reminders for due dates.
- `reports.py`: Manages generating reports for the library.
- `storage.py`: Handles file-based storage operations.
- `advanced_search.py`: Manages advanced searching of books.
- `main.py`: The main entry point of the application.

## Example Data 📄

Example book data can be found in `books.json`:
```json
[
    {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "isbn": "9780743273565"
    }
]
```

## Contributions 🤝

Contributions are welcome! Feel free to submit a pull request or open an issue.

## License 📜

This project is licensed under the MIT License.

## Contact ✉️

For any questions or suggestions, please contact us at [pangoth20102@iiitnr.edu.in].

---

Happy Reading! 📖✨
