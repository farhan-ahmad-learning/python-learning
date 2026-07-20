# FUNCTIONS
# Week 2 - Friday
# def = define, the keyword to create a function

# Basic function - no parameters
def greet():
    "This function prints a greeting."
    print("Hello! Welcome to Python Functions.")
    print("Functions help us reuse code!")
    
# Calling the function
greet()


# -----Functions with one parameter-------
def greet_person(name):
    "Greets a specific person by name."
    print(f"Hello {name}! Welcome to Python.")
greet_person("Farhan")
greet_person("Yusuf")


#----Function with multiple parameters------
# "Greets person with language and company"
def greet_full(name, language, company):
    print(f"Hello {name}! You speak {language} and work at {company}.")

greet_full("Farhan", "French", "Cognizant")
greet_full("Ahmed", "Arabic", "TCS")



# -----Functions with return values----
# return sends a value back to whoever called the function

def add(a, b):
    "Returns sum of 2 numbers"
    return a + b

def subtract(a, b):
    return a - b

def muliply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: cannot divide by 0"
    return a / b

# Store return values in variables
result1 = add(25,15)
result2 = subtract(50, 20)
result3 = muliply(6, 7)
result4 = divide(100, 4)
result5 = divide(10, 0)

print(f"25 + 15: {result1}")
print(f"50 - 20: {result2}")
print(f"6 * 7 : {result3}")
print(f"100 / 4: {result4}")
print(f"10 / 0: {result5}")


# Use return value directly
print(f"\nDouble of 15: {add(15, 15)}")
print(f"Square of 8: {muliply(8, 8)}")


# Multiple return values
def min_max_avg(numbers):
    "Returns min, max and avg of a list."
    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers) / len(numbers)
    return minimum, maximum, average     # returns a tuple

scores = [45, 82, 91, 67, 38, 55, 79, 93]
low, high, avg = min_max_avg(scores)        # unpack the tuple
print(f"\nScores: {scores}")
print(f"Min: {low} | Max: {high} | Average: {avg:.1f}")


# --Default parameters----
# Default value used when argument not provided

def greet_language(name, language="English"):
    "Greets in specified language - English by default"
    greetings = {
        "English": "Hello",
        "French": "Bonjour",
        "Arabic": "Marhaba",
        "Hindi": "Namaste",
        "Spanish": "Hola"
    }
    greeting = greetings.get(language, "Hello")
    print(f"{greeting} {name}!")

# Without language - uses default English
greet_language("Farhan")                # Hello Farhan!

# With language specified
greet_language("Farhan", "Arabic")      # Marhaba Farhan!
greet_language("Yusuf", "Hindi")        # Namaste Yusuf!
greet_language("Sara", "Spanish")       # Hola Sara!


#---Keyword arguments---
# Pass arguments by name - order doesn't matter

def create_profile(name, age, city, job):
    "Creates and displays a profile."
    print(f"\n===== PROFILE =====")
    print(f"Name    : {name}")
    print(f"City    : {city}")
    print(f"Age     : {age}")
    print(f"Job     : {job}")
    print(f"=====================")

# Positional - order matters
create_profile("Farhan", 35, "Delhi", "Localization")

# Keyword - order doesn't matter
create_profile(
    job="Localization",
    city="Delhi",
    name="Yusuf",
    age=3
)


# ---*args - variable number of arguments---
# Use when you don't know how many arguments will be passed
# *args collects all positional arguments into a TUPLE

def add_all(*numbers):
    "Adds any number of values."
    total = 0
    for num in numbers:
        total += num
    return total

print(f"\nadd_all(1, 2, 3)              = {add_all(1, 2, 3)}")
print(f"add_all(10, 20, 30, 40)         = {add_all(10, 20, 30, 40)}")
print(f"add_all(5)                      = {add_all(5)}")


def greet_all(*names):
    "Greets any number of people."
    print()
    for name in names:
        print(f"Hello {name}!")

greet_all("Farhan", "Yusuf", "Sara", "Rahul", "Priya")


# kwargs - keyword arguments
# Use when you don't know what key-value pairs will be passed
# **kwargs collects all keyword arguments into a DICT

def display_info(**details):
    "Display any information passed as keyword args."
    print(f"\n===== INFORMATION =====")
    for key, value in details.items():
        print(f"{key.title()}: {value}")
    print("==========================")

display_info(name="Farhan", age=37, city="Delhi", job="BA")
display_info(
    name="Yusuf",
    age=3,
    role="kid",
    language="child"
)


# Combining all parameter types
# Order must be: regular, *args, **kwargs

def full_function(greetings, *names, **options):
    "Demonstates all parameter types together."
    print(f"\nGreeting: {greetings}")
    print(f"Names: {names}")
    print(f"Options: {options}")

    for name in names:
        msg = f"{greetings} {name}!"
        if options.get("uppercase"):
            msg = msg.upper()
        print(msg)

full_function("Hello", "Farhan", "Yusuf", uppercase=True)
full_function("Bonjour", "Pierre", "Marie", uppercase=False)



#---DOCSTRINGS-----------------------
# Triples quotes inside function - explain what it does
# Access with function.__doc__

def calculate_bmi(weight, height_cm):
    """
    Calculate Body Mass Index (BMI).

    Args:
        weight: Weight in kilograms
        height_cm: Height in centimetres

    Returns:
        BMI value rounded to 2 decimal places
    """

    height_m=height_cm/100
    bmi=weight/(height_m**2)
    return round(bmi,2)

print(calculate_bmi(75, 175))
print(calculate_bmi.__doc__)        # prints the docstring



#----------VARIABLE SCOPE-----------
# Local - exists only inside the function
# Global - exists everywhere

global_name="Farhan"       # Global variable

def show_scope():
    local_name="Ahmad"      # local variable - only inside function
    print(f"Inside function - global name:{global_name}")
    print(f"Inside function - local name:{local_name}")

show_scope()
print(f"Outside function - global name:{global_name}")
# print(local_name)     # would cause NameError - local_name doesn't exist here


