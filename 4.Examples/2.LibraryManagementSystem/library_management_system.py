from typing import Dict
from book import Book
from member import Member

class LibraryManagementSystem():
    _instance = None
    def __init__(self):
        if LibraryManagementSystem._instance is not None:
            raise Exception(f"This is a singleton class!")
        else:
            LibraryManagementSystem._instance = self
            self.catalog = {}
            self.members = {}
            self.LOAN_DURATION_DAYS = 14
            self.MAX_BOOKS_PER_MEMBER = 5

    @staticmethod
    def get_instance():
        if LibraryManagementSystem._instance is None:
            LibraryManagementSystem()
        return LibraryManagementSystem._instance
    

    def add_book(self, book : Book):
        self.catalog[book.isbn] = book

    def get_book(self, isbn : str):
        self.catalog[isbn]

    def remove_book(self, isbn : str):
        self.catalog.pop(isbn, None)
    
    def register_a_member(self, member : Member):
        self.members[member.member_id] = member
    
    def de_register_a_member(self, member : Member):
        self.members.pop(member.id, None)

    def borrow_book(self, member_id: int, isbn:str):
        member : Member = self.members[member_id]
        book : Book = self.catalog[isbn]
        if member and book and book.available:
            if len(member._borrowed_books) < self.MAX_BOOKS_PER_MEMBER:
                member.borrow_book(book)
                book.available = False
            else:
                print(f"We couldn't borrow you {book.name} as you've reached you're limit !!")
        else:
            print(f"We couldn't borrow you {book.name} now, sorry !!")
    
    def return_book(self, member_id, isbn):
        member : Member = self.members[member_id]
        book : Book = self.catalog[isbn]
        if member and book:
                member.return_book(book)
                book.available = True
        else:
            print(f"We couldn't borrow you {book.name} now, sorry !!")



