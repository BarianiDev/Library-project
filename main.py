from book import Book
from user import User
from library import Library

library = Library()

book1 = Book("J K Rowling", "Harry Potter", 8877827025)
book2 = Book("R R Martin", "Game of Thrones", 1606238433)
book3 = Book("A A Martin", "Test", 5141651321)
library.register_book(book1)
library.register_book(book2)
library.register_book(book3)
print("-" * 50)

user1 = User("Pedro", 12345678910, 1)
user2 = User("Barbara", 523266563, 2)
user3 = User("Jose", 5161636556, 3)
library.register_user(user1)
library.register_user(user2)
library.register_user(user3)
print("-" * 50)

library.borrow_book(user1, book1)
library.borrow_book(user1, book2)
library.borrow_book(user3, book3)
print("-" * 50)

library.return_book(book1, user1)
library.borrow_book(user2, book1)
# library.return_book(book1, user2)
print("-" * 50)

library.return_book(book1, user2)
library.return_book(book2, user1)
library.return_book(book3, user3)
print("-" * 50)

# library.borrow_book(user1, book1)
# library.borrow_book(user1, book2)
# library.borrow_book(user1, book3)
