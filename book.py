class Book:
    def __init__(self, author, title, isbn):
        self.author = author
        self.title = title
        self.isbn = isbn

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "ISBN": self.isbn
        }
