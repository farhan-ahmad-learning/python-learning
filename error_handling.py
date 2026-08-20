# ERROR HANDLING
# Week 4 - Monday
# Errors are inevitable — handle them gracefully

# ── Without error handling — program crashes ──────
# int("hello")       # ValueError — crashes!
# 10 / 0             # ZeroDivisionError — crashes!
# open("missing.txt") # FileNotFoundError — crashes!

# ── Basic try/except ──────────────────────────────
try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print(f"100 / {number} = {result}")
except ValueError:
    print("Error: Please enter a valid number!")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")


# ---Multiple exceptions-------
def safe_divide(a, b):
    """Safely divides two numbers."""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Division by zero!"
    except TypeError:
        return "Error: Both values must be numbers!"
    
print(safe_divide(10,2))        # 2.0
print(safe_divide(10,0))        # Error: Division by zero!
print(safe_divide(10,"two"))    # Error: Both values must be numbers!


# ---Catching all exceptions-------
def risky_operation(value):
    try:
        result = 100 / int(value)
        return result
    except (ValueError, ZeroDivisionError) as e:
        return f"Error caught: {e}"
    except Exception as e:
        return f"Unexpected error: {e}"
    
print (risky_operation("5"))        # 20
print (risky_operation("0"))        # Error caught: division by zero
print (risky_operation("hello"))    # Error caught: invalid literal for int() with base 10: 'hello'


# ----else -- runs if NO exception occured---------
# ----finally - ALWAYS runs, exception or not------

def read_file(filename):
    """Reads a file with full error handling."""
    try:
        file = open(filename, "r")
        content = file.read()
    except FileNotFoundError:
        print(f"Error: '{filename}' not found!")
        content = None
    except PermissionError:
        print(f"Error: No permission to read: '{filename}'")
        content = None
    else:
        # Only runs if no exception
        print(f"File read successfully - {len(content)} characters")
    finally:
        # Always run, good for cleanup
        print(f"Attempted to read: {filename}")

    return content

read_file("error_handling.py")      # exists - works
read_file("missing.txt")            # doesn't exist - error


#--- try/except/else/finally pattern ----
def connect_to_service(service_name):
    """Simulates connecting to a service."""
    try:
        if service_name == "":
            raise ValueError("Service name cannot be empty!")
        print(f"Connecting to {service_name}...")
        # simulate access
        connected = True
    except ValueError as e:
        print(f"Connection failed: {e}")
        connected = False
    else:
        print(f"Successfully connected to {service_name}!")
    finally:
        print(f"Connection attempt complete.\n")

    return connected

connect_to_service("AWS")
connect_to_service("GitHub")
connect_to_service(".")



# -- CUSTOM EXCEPTIONS -----
# Create your own exception classes

class ValidationError(Exception):
    """Raised when data validation fails."""
    pass

class AgeError(ValidationError):
    """Raised when age is invalid."""
    def __init__(self, age, message="Invalid age"):
        self.age        = age
        self.message    = message
        super().__init__(f"{message}: {age}")

class SalaryError(ValidationError):
    """Raised when salary is invalid."""
    def __init__(self, salary):
        self.salary = salary
        super().__init__(f"Invalid salary: {salary}")

# --Using custom exceptions----------
def create_employee(name, age, salary):
    """Created employee with validation."""
    # Validate name
    if not name or not name.strip():
        raise ValidationError("Name cannot be empty!")
    
    #Validate age
    if age < 18:
        raise AgeError(age, "Employee must be 18 or older")
    if age > 65:
        raise AgeError(age, "Age cannot exceed 65")
    
    # Validate salary
    if salary < 0:
        raise SalaryError(salary)
    if salary < 15000:
        raise SalaryError(f"{salary} - minimum salary is Rs.15,000")
    
    return {
        "name"  : name,
        "age"   : age,
        "salary": salary
    }


# Test with various inputs
test_cases = [
    ("Farhan Ahmad", 35, 60000),   # valid
    ("",             25, 50000),   # empty name
    ("Ahmed Khan",   16, 50000),   # too young
    ("Sara Ali",     30, -1000),   # negative salary
    ("Rahul",        30, 10000),   # salary too low
]

for name, age, salary in test_cases:
    try:
        emp = create_employee(name, age, salary)
        print(f"✓ Created: {emp['name']} - Rs.{emp['salary']:,}")
    except AgeError as e:
        print(f"x Age Error     : {e}")
    except SalaryError as e:
        print(f"x Salary Error  : {e}")
    except ValidationError as e:
        print(f"x Validation    : {e}")




# ---raise - manually trigger an exception-------
def set_age(age):
    """Sets age with validation."""
    if not isinstance(age, int):
        raise TypeError(f"Age must be integer, got {type(age).__name__}")
    if age < 0  or age > 150:
        raise ValueError(f"Age {age} is out of valid range (0-150)")
    return age

try:
    print(set_age(35))      # valid
    print(set_age(-5))      # raises value error
except ValueError as e:
    print(f"ValueError: {e}")

try:
    print(set_age("old"))   # raises type error
except TypeError as e:
    print(f"TypeError: {e}")


# assert - check conditions during development
def calculate_percentage(score, total):
    """Calculates percentage."""
    assert total > 0, "Total must be greater than zero!"
    assert 0 <= score <= total, f"Score {score} must be between 0 and {total}"
    return round((score / total) * 100, 1)

print(f"\n{calculate_percentage(85, 100)}%")     # 85.0%
print(f"\n{calculate_percentage(45, 60)}%")      # 75.0%

try:
    calculate_percentage(85, 0)         # AssertionError
except AssertionError as e:
    print(f"AssertionError: {e}")