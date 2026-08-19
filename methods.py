# Attributes and Methods
# Week 3 - Tuesday

class Book:
    """Represents a book in a library."""

    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        self.is_read = False        # default value

    # Special methods (dunder methods)------
    # These start and end with double underscores __

    def __str__(self):
        """Returns string representation - used by print()"""
        return f"'{self.title}' by {self.author}"
    
    def __repr__(self):
        """Returns detailed representation - for debugging"""
        return f"Book(title='{self.title}', author='{self.author}', pages={self.pages})"
    
    def __len__(self):
        """Returns length - used by len()"""
        return self.pages
    
    def __eq__(self, other):
        """Checks equality - used by =="""
        return self.title == other.title and self.author == other.author
    
    def __lt__(self, other):
        """Less than - used for sorting"""
        return self.price < other.price
    

    # Regualar methods----------
    def mark_as_read(self):
        """Marks book as read."""
        self.is_read = True
        print(f"You have finished reading {self.title}!")

    def apply_discount(self, percent):
        """Applies discount to price."""
        discount = self.price * (percent / 100)
        self.price -= discount
        print (f"Discount applied! New price: Rs.{self.price:.2f}")

    def get_info(self):
        """Returns formatted book information."""
        status = "Read" if self.is_read else "Not read"
        return {
            "title" :   self.title,
            "author":   self.author,
            "pages" :   self.pages,
            "price" :   f"Rs.{self.price:.2f}",
            "status":   status
        }

# Create books
book1 = Book("Clean Code",        "Robert Martin",   431, 599)
book2 = Book("Fluent Python",     "Luciano Ramalho",  792, 799)
book3 = Book("Grokking Algorithms","Aditya Bhargava", 256, 499)
book4 = Book("Clean Code",        "Robert Martin",   431, 599)

# Test special methods
print(book1)
print(repr(book2))
print(f"Pages: {len(book1)}")
print(f"Same book: {book1 == book4}")
print(f"Same book: {book1 == book2}")

# Sort books by price using __lt__
books = [book1, book2, book3]
sorted_books = sorted(books)
print(f"\nBooks sorted by price:")
for book in sorted_books:
    print(f"    {book} - Rs.{book.price}")

# Test regular methods
book1.mark_as_read()
book2.apply_discount(10)

# Get info
info = book1.get_info()
print(f"\n==== BOOK INFO =====")
for key, value in info.items():
    print(f"{key.title():<8}: {value}")




# Class methods and Static methods--------
class Temperature:
    """Demonstrates class and static methods."""

    # Class variable
    unit = "Celsius"

    def __init__(self, value):
        self.value = value

    # Instance method - works on one object, needs self
    def display(self):
        print(f"Temperature: {self.value}°{Temperature.unit[0]}")

    # Class method - works on class itself, needs cls
    # Used to change class variables or create objects differently
    @classmethod
    def set_unit(cls, unit):
        """Changes the temperature unit for all objects."""
        cls.unit = unit
        print(f"Unit changed to {unit}")
    
    @classmethod
    def from_fahrenheit(cls, fahrenheit):
        """Creates Temperature object from Fahrenheit value."""
        celsius = (fahrenheit - 32) * 5/9
        return cls(round(celsius, 1))
    
    # Static method - doesn't need cls or self
    # Justify a utility function that belongs to the class

    @staticmethod
    def is_freezing(value):
        """Checks if temperature is at or below freezing."""
        return value <= 0
    
    @staticmethod
    def convert_to_fahrenheit(celsius):
        """Converts Celsius to Fahrenheit."""
        return round((celsius * 9/5) +32, 1)
    
# Instance method
t1 = Temperature(25)
t1.display()

# Class method - change unit for ALL objects
Temperature.set_unit("Fahrenheit")
t1.display()
Temperature.set_unit("Celsius")

# Class method - alternative constructor
t2 = Temperature.from_fahrenheit(98.6)
print(f"98.6°F = {t2.value}°C")

# Static methods - no object needed
print(f"\nIs 0°C freezing? {Temperature.is_freezing(0)}")
print(f"Is 25°C freezing? {Temperature.is_freezing(25)}")
print(f"25°C in Fahrenheit: {Temperature.convert_to_fahrenheit(25)}")


# Getters and Setters — @property
class Student:
    def __init__(self, name, age):
        self._age = age    # _ means "private"

    @property
    def age(self):         # getter — read the value
        return self._age

    @age.setter
    def age(self, value):  # setter — set with validation
        if value < 0:
            raise ValueError("Age cannot be negative!")
        self._age = value

s = Student("Farhan", 35)
print(s.age)        # calls getter → 35
s.age = 36          # calls setter → validates then sets
s.age = -1          # raises ValueError!