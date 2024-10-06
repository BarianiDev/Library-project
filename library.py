import json

class Library:
    def __init__(self, books_file="books.json", users_file="users.json"):
        self.books_file = books_file
        self.users_file = users_file
        self.books = self.load_data(self.books_file)
        self.users = self.load_data(self.users_file)

    def save_data(self, file, data):
        try:
            with open(file, "w") as f:
                json.dump(data, f, indent=4)
        except IOError as e:
            print("Error saving data.")
        
    def load_data(self, file):
        try:
            with open(file, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"File {file} not found, creating a new file.")
            return []
        except json.JSONDecodeError:
            print(f"Error decoding file {file}. Please check the format.")
            return []

    def register_book(self, book):
        try:
            for b in self.books:
                if b["ISBN"] == book.isbn:
                    print(f"The book '{book.title}' is already registered.")
                    return
                
            self.books.append(book.to_dict())
            self.save_data(self.books_file, self.books)
            print(f"Book: '{book.title}' registered successfully.")
        except AttributeError as e:
            print(f"Error registering book: {e}")

    def register_user(self, user):
        try:
            for u in self.users:
                if u["CPF"] == user.get_cpf():
                    print(f"The holder of CPF: {user.get_cpf()} is already registered.")
                    return
                
            self.users.append(user.to_dict())
            self.save_data(self.users_file, self.users)
            print(f"User: {user.get_name()}, holder of CPF: {user.get_cpf()} registered successfully.")
        except AttributeError as e:
            print(f"Error registering user: {e}")

    def borrow_book(self, user, book):
        try:
            # Check if the book has already been borrowed by the user
            for b in user.borrowed_books:
                if b["ISBN"] == book.isbn:
                    print(f"The book '{book.title}' has already been borrowed by the holder of CPF: {user.get_cpf()}.")
                    return

            # Check if the book is available in the catalog
            for b in self.books:
                if b["ISBN"] == book.isbn:
                    print(f'Book {book.title} borrowed by user {user.get_id()}.')

                    # Remove the book from the catalog and add it to the user's borrowed books
                    self.books.remove(b)
                    user.borrowed_books.append(book.to_dict())

                    # Update the user in the users file
                    for u in self.users:
                        if u["ID"] == user.get_id():
                            u["borrowed_books"] = user.borrowed_books

                    # Save the changes to the JSON files
                    self.save_data(self.books_file, self.books)
                    self.save_data(self.users_file, self.users)
                    return

            # If the book is not found in the catalog
            print(f'The book {book.title} is not available for borrowing.')

        except KeyError as e:
            print(f"ERROR: key {e} not found.")
        except TypeError:
            print("Provided data is incorrect.")
        except AttributeError as e:
            print(f"Error accessing book or user data: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def return_book(self, book, user):
        try:
            for b in user.borrowed_books:
                if b["ISBN"] == book.isbn:
                    print(f'Book {book.title} returned to the library by {user.get_id()}.')

                    user.borrowed_books.remove(b)

                    self.books.append(b) 

                    self.save_data(self.books_file, self.books)
                    self.save_data(self.users_file, self.users)
                    return
                
            print(f"The book '{book.title}' was not found in the user's borrowed list.")
    
        except KeyError as e:
            print(f"ERROR: key {e} not found.")   
        except TypeError:
            print("Provided data is incorrect.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
