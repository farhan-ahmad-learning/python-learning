# BUILT IN FUNCTIONS PRACTICE
# Week 2 - Thursday extra
# Practising all buit-in functions used in challenges


#---zip()-----------------------------
# Pairs 2 or more lists together
names = ["Farhan", "Ahmad", "Sara"]
scores = [85, 67, 92]
cities = ["Delhi", "Mumbai", "Chennai"]

# Basic zip - pairs 2 lists
paired = list(zip(names, scores))
print(f"zip(names, scores :{paired})")
# zip(names, scores :[('Farhan', 85), ('Ahmad', 67), ('Sara', 92)])

# zip with 3 lists
triple = list(zip(names, scores, cities))
print(f"zip(names, scores, cities :{triple})")
# zip(names, scores, cities :[('Farhan', 85, 'Delhi'), ('Ahmad', 67, 'Mumbai'), ('Sara', 92, 'Chennai')])

# loop through zipped lists
for name, score, city in zip(names, scores, cities):
    print(f" {name} from {city} scored {score}")
# Farhan from Delhi scored 85
# Ahmad from Mumbai scored 67
# Sara from Chennai scored 92


# zip to create dictionary
profile_keys = ["name", "age", "city", "job"]
profile_values = ["Farhan", "37", "Delhi", "Localization"]
profile = dict(zip(profile_keys, profile_values))
print(f"\nProfile: {profile}")

print()
#Profile: {'name': 'Farhan', 'age': '37', 'city': 'Delhi', 'job': 'Localization'}

#---round----------
# Rounds a number to given decimal places
pi = 3.14159265
print(f"round(pi, 0): {round(pi, 0)}")  # 3.0
print(f"round(pi, 1): {round(pi, 1)}")  # 3.1
print(f"round(pi, 2): {round(pi, 2)}")  # 3.14
print(f"round(pi, 3): {round(pi, 3)}")  # 3.142
print(f"round(pi, 4): {round(pi, 4)}")  # 3.1416

# Practical use - money calculations
price = 129.999
tax = price * 0.18
total = price + tax
print(f"\nPrice: Rs. {price}")
print(f"Tax: Rs. {round(tax, 2)}")
print(f"Total: Rs. {round(total, 2)}")
print()


#----sum(), min(), max()-----------
numbers = [45, 82, 91, 67, 38, 55, 79, 93]
print(f"Numbers: {numbers}")
print(f"Sum(): {sum(numbers)}")     # 550
print(f"Min(): {min(numbers)}")     # 38
print(f"Max(): {max(numbers)}")     # 93
print(f"len(): {len(numbers)}")     # 8
print(f"Average: {sum(numbers)/len(numbers):.1f}") # 68.8

#  With strings - min/max works alphabetically
names_list = ["Farhan", "Ahmed", "Sara", "Priya"]
print(f"\nmin(names): {min(names_list)}")   # Ahmed
print(f"max(names): {max(names_list)}")   # Sara
print()


#---abs-----------------
# Returns absolute value - removes negative sign
print({abs(-10)})       # 10
print({abs(10)})        # 10
print({abs(-3.14)})     # 3.14

# Practical use- temperature difference
temp_today = 38
temp_yesterday = 42
difference = abs(temp_today - temp_yesterday)
print(f"\nTemp diff: {difference} degrees") # 4 degrees

print()


# ----sorted-------------
# RETURNS a new sorted list - original is unchanged
numbers2 = [30, 10, 50, 20, 40]
sorted_asc = sorted(numbers2)                   # ascending
sorted_desc = sorted(numbers2, reverse=True)    #descending

print(f"Original        : {numbers2}")          # [30, 10, 50, 20, 40] - unchanged
print(f"Sorted asc      : {sorted_asc}")        # [10, 20, 30, 40, 50]
print(f"Sorted desc     : {sorted_desc}")       # [50, 40, 30, 20, 10]


# Sort strings alphabetically
langs = ["Python", "French", "English", "Arabic", "AWS"]
print(f"\nSorted languages : {sorted(langs)}")


# Sort by length of string
print(f"Sorted by length: {sorted(langs, key=len)}")
sort_length = sorted(langs, key=len)
print(f"Sorted by length: {sort_length}")

print()



# enumerate (deep practice)
# Gives INDEX and value together while looping
skills = ["Python", "AWS", "French", "Business Analysis"]

# Default - starts from 0
for i, skill in enumerate(skills):
    print(f"{i}. {skill}")

print()

# Custom start - starts from 1
for i, skill in enumerate(skills, 1):
    print(f"{i}. {skill}")

print()


# Enumerate with condition
print("Skills with more than 5 letters")
for i, skill in enumerate(skills, 1):
    if len(skill) > 5:
        print(f"{i}. {skill} ({len(skill)}) letters")

print()


# -dict()------------
# Converts other data types to dictionary

# From list of tuples
pairs = [("name", "Farhan"), ("age", 35), ("city", "Delhi")]
from_tuples = dict(pairs)
print(f"dict from tuples: {from_tuples}")  # {'name': 'Farhan', 'age': 35, 'city': 'Delhi'}

# From zip
keys = ["a", "b", "c"]
values = [1, 2, 3]
from_zip = dict(zip(keys, values))
print(f"dict from zip: {from_zip}")     # {'a': 1, 'b': 2, 'c': 3}

# Using keyword arguments
from_kwargs = dict(name="Farhan", age=37, city="Delhi")
print(f"dict from kwargs: {from_kwargs}")   # {'name': 'Farhan', 'age': 37, 'city': 'Delhi'}


# all() and any() - bonus!------
# all() — returns True if ALL items are True
# any() — returns True if ANY item is True
scores2 = [85, 72, 91, 65, 78]
print(f"All passed (>=60): {all(s >= 60 for s in scores2)}")        # True
print(f"Any distinction (>=90): {any(s >= 90 for s in scores2)}")   # True

scores3 = [85, 72, 45, 65, 78]
print(f"All passed (>=60): {all(s >= 60 for s in scores3)}")        # False
print(f"Any failes (<60): {any(s < 60 for s in scores3)}")          # True