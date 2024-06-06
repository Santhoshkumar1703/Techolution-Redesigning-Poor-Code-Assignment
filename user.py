from models import User
from storage import Storage

# Class to manage user-related operations
class UserManager:
    def __init__(self, storage_file="users.json"):
        self.storage = Storage(storage_file)  # Initialize the storage with the given storage file
        # Load user data from storage and create User instances
        self.users = [User.from_dict(user) for user in self.storage.load()]

    # Method to add a new user
    def add_user(self, name, user_id):
        new_user = User(name, user_id)  # Create a new User instance
        self.users.append(new_user)  # Add the new user to the list of users
        self.save_users()  # Save the updated user list to storage
        print("User added.")  # Print confirmation message

    # Method to update an existing user's information
    def update_user(self, user_id, name=None):
        for user in self.users:
            if user.user_id == user_id:
                if name:
                    user.name = name  # Update the user's name if provided
                self.save_users()  # Save the updated user list to storage
                print("User updated.")  # Print confirmation message
                return
        print("User not found.")  # Print message if the user is not found

    # Method to delete a user by user_id
    def delete_user(self, user_id):
        # Remove the user with the given user_id from the user list
        self.users = [user for user in self.users if user.user_id != user_id]
        self.save_users()  # Save the updated user list to storage
        print("User deleted if existed.")  # Print confirmation message

    # Method to list all users
    def list_users(self):
        if not self.users:
            print("No users available.")  # Print message if no users are available
        for user in self.users:
            print(user)  # Print each user

    # Method to search for users based on attributes
    def search_users(self, **kwargs):
        results = self.users
        # Filter users based on provided keyword arguments (e.g., name, user_id)
        for key, value in kwargs.items():
            results = [user for user in results if getattr(user, key, None) == value]
        return results  # Return the list of matching users

    # Method to save the current list of users to storage
    def save_users(self):
        self.storage.save([user.to_dict() for user in self.users])  # Save to storage
