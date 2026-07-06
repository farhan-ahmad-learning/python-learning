# VARIABLES AND DATA TYPES
# Week1 - Wednesday

name = "Farhan"             # String - text always in quotes
age = 35                    # Integer - whole number, no quotes
salary = 55000.50           # Float - decimal number
is_employed = True          # Boolean - only True or False (capital T/F)

# Check the type of each variable
print(type(name))           # <class 'str'>
print(type(age))            # <class 'int'>
print(type(salary))         # <class 'float'>
print(type(is_employed))    # <class 'bool'>

# Print them with labels
print(f"Name : {name}")
print(f"Age : {age}")
print(f"Salary : {salary}")
print(f"Is Employed : {is_employed}")


#STRING METHODS
# These are very relevant to your translation work

language = "french"

print(language.upper())            #FRENCH
print(language.lower())            #french
print(language.capitalize())       #French
print(len(language))               #6 - counts characters


# Replace text - very useful in localization
text = "Bonjour le monde"
print(text.replace("Bonjour", "Hello"))    #Hello le monde

# Strip removed extra spaces - useful when cleaning text
messy = "      hello world   "
print(messy.strip())        # hello world
print(messy.lstrip())       # hello world
print(messy.rstrip())       #     hello world


#Check with text contains something
sentence = "I love Python programming"
print(sentence.startswith("I"))     #True
print(sentence.endswith("ing"))     #True
print("Python" in sentence)         #True
print("Java" in sentence)           #False



# F-STRINGS - the most important formatting tool in Python
name = "Farhan"
age = 35
city = "New Delhi"
salary = 55000.50

# Basic f-string
print(f"My name is {name} and I am {age} years old")

#Math inside f-srtings
print(f"In 5 years I will be {age + 5}")
print(f"My daily salary is {salary/30:.2f}")

#Method inside f-strings
print(f"Name in upper case : {name.upper()}")
print(f"Name has {len(name)} letters")

#Multiple variables
print(f"{name} lives in {city} and earns rupees {salary:,} per year")
# The :, adds comma separators to numbers -  55,500.50
# The :.2f rounds to 2 decimal places






