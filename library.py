# LIBRARY MANAGEMENT SYSTEM
# Week 3 - Saturday OOP Project

import os
import json

class Book:
    """Represents a book in the library."""
    
    def __init__(self, isbn, title, author, year):
        self.isbn       = isbn
        self.title      = title
        self.author     = author
        self.year       = year
        self.available  = True
        self.borrower   = None

    def borrow(self, member_name):
        "Marks book as borrowed."
        self.available = True
        self.borrower  = None

    def to_dict(self):
        """Converts book to dictionary for JSON saving."""
        return {
            "isbn"     : self.isbn,
            "title"    : self.title,
            "author"   : self.author,
            "year"     : self.year,
            "available": self.available,
            "borrower" : self.borrower
        }
    
    def __str__(self):
        status = "Available" if self.available else f"Borrowed by {self.borrower}"
        return f"'{self.title}' by '{self.author}' [{status}]"
    
#--Member class-------
class Member:
    """Represents a library member."""

    def __init__(self, member_id, name, email):
        self.member_id      = member_id
        self.name           = name
        self.email          = email
        self.borrowed_books = []
        self.history        = []

    def borrow_book(self, book):
        """Borrows a book if available."""
        if book.borrow(self.name):
            self.borrowed_books.append(book.isbn)
            self.history.append(book.title)
            print(f"{self.name} borrowed: {book.title}")
            return True
        else:
            print(f"Sorry - '{book.title}' is not available!")
            return False
        
    def return_book(self, book):
        """Returns a borrowed book."""
        if book.isbn in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book.isbn)
            print(f"{self.name} returned: {book.title}")
            return True
        else:
            print(f"{self.name} hasn't borrowed '{book.title}'")
            return False
    
    def display(self, library):
        """Displays member information."""
        print(f"\n===== Member: {self.name} =====")
        print(f"ID              : {self.member_id}")
        print(f"Email           : {self.email}")
        print(f"Books borrowed  : {len(self.borrowed_books)}")
        if self.borrowed_books:
            titles = [library.get_book(isbn).title
                      for isbn in self.borrowed_books]
            print(f"Currently has   : {', '.join(titles)}")
        if self.history:
            print(f"Full history    : {', '.join(self.history)}")

    def to_dict(self):
        """Converts member to dictionary for JSON saving."""
        return {
            "member_id"     : self.member_id,
            "name"          : self.name,
            "email"         : self.email,
            "borrowed_books": self.borrowed_books,
            "history"       : self.history
        }
    

#--Library class----
class Library:
    """Manager the entire Library System."""

    def __init__(self, name):
        self.name       = name
        self.books      = {}    # isbn: Book object
        self.members    = {}    # member_id: Member object

    def add_book(self, book):
        """Adds a book to the library."""
        self.books[book.isbn] = book

    def register_member(self, member):
        """Regsiters a new member."""
        self.members[member.member_id] = member

    def get_book(self, isbn):
        """Returns book by ISBN."""
        return self.books.get(isbn)
    
    def get_member(self, member_id):
        """Returns member by ID."""
        return self.members.get(member_id)
    
    def search(self, query):
        """Searches book by title or author."""
        query = query.lower()
        results = [
            book for book in self.books.values()
            if query in book.title.lower()
            or query in book.author.lower()
        ]
        return results
    
    def display_all_books(self):
        """Displays all books with status."""
        print(f"\n===== ALL BOOKS =====")
        print(f"{'ISBN':<12} {'Title':<25} {'Author':<20} Status")
        print(f"{'----':<12} {'-----':<25} {'------':<20} ------")
        for book in self.books.values():
            status = "Available" if book.available else "Borrowed"
            print(f"{book.isbn:<12} "
                  f"{book.title:<25} "
                  f"{book.author:<20} "
                  f"{status}")
            
    
    def display_search_results(self, query):
        """Displays search results."""
        results = self.search(query)
        print(f"\n==== SEARCH: {query} =====")
        if results:
            print(f"Found {len(results)} book(s):")
            for book in results:
                status = "Available" if book.available else "Borrowed"
                print(f"    {book.title} - {book.author} ({status})")
        else:
            print("No books found!")

    def save_to_json(self, filename):
        """Saves library data to JSON file."""
        data = {
            "library.name"  : self.name,
            "books"         : [b.to_dict() for b in self.books.values()],
            "members"       : [m.to_dict() for m in self.members.values()]
        }
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        print(f"\nLibrary data saved to {filename}")

    
    def get_stats(self):
        """Returns library statistics."""
        total       = len(self.books)
        available   = sum(1 for b in self.books.values() if b.available)
        borrowed    = total - available
        return {
            "total_books"   : total,
            "available"     : available,
            "borrowed"      : borrowed,
            "total_members" : len(self.members)
        }
    

#--Main Program----
print("===== LIBRARY MANAGEMENT SYSTEM =====")

# Create library
lib = Library("Cognizant Learning Library")

# Add books
books_data = [
    ("ISBN001", "Clean Code",               "Robert Martin",   2008),
    ("ISBN002", "Fluent Python",            "Luciano Ramalho", 2015),
    ("ISBN003", "Grokking Algorithms",      "Aditya Bhargava", 2016),
    ("ISBN004", "The Pragmatic Programmer", "Hunt and Thomas", 1999),
    ("ISBN005", "Python Crash Course",      "Eric Matthes",    2019),
]

for isbn, title, author, year in books_data:
    lib.add_book(Book(isbn, title, author, year))

print(f"\nBooks added: {len(lib.books)}")

# Register members
members_data = [
    ("MEM001", "Farhan Ahmad", "farhan@email.com"),
    ("MEM002", "Ahmed Khan",   "ahmed@email.com"),
    ("MEM003", "Sara Ali",     "sara@email.com"),
]

for mid, name, email in members_data:
    lib.register_member(Member(mid, name, email))

print(f"Members registered: {len(lib.members)}")


# Display all books
lib.display_all_books()


# Borrow books
farhan = lib.get_member("MEM001")
ahmed = lib.get_member("MEM002")

farhan.borrow_book(lib.get_book("ISBN001"))
farhan.borrow_book(lib.get_book("ISBN002"))
ahmed.borrow_book(lib.get_book("ISBN003"))

# Try borrowing already borrowed book
ahmed.borrow_book(lib.get_book("ISBN002"))

# Display updated books
lib.display_all_books()

# Display member info
farhan.display(lib)

# Return a book
farhan.return_book(lib.get_book("ISBN001"))

# Search
lib.display_search_results("python")
lib.display_search_results("Robert")

# Statistics
stats = lib.get_stats()
print(f"\n===== LIBRARY STATS =====")
for key, value in stats.items():
    print(f"{key.replace('_', ' ').title():<20}: {value}")


# Save to JSON
lib.save_to_json("library.json")

# Clean up
if os.path.exists("library.json"):
    os.remove("library.json")