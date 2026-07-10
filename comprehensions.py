# LIST COMPREHENSIONS
# Week 2 - Thursday
# Shorter, faster, more Pythonic way to create lists

# ---The old way - using for loop------
squares_loop = []
for i in range(1, 6):
    squares_loop.append(i ** 2)
print(f"Old way: {squares_loop}")       # [1, 4, 9, 16, 25]


# ---The new way - list comprehension----
# Syntax: [expression for item in iterable]
squares = [i ** 2 for i in range(1, 6)]
print(f"New way: {squares}")            # [1, 4, 9, 16, 25]

# More examples
numbers = [i for i in range(1, 6)]
print(f"Numbers: {numbers}")            # [1, 2, 3, 4, 5]

doubled = [i * 2 for i in range(1, 6)]
print(f"Doubled: {doubled}")            # [2, 4, 6, 8, 10]

cube = [i ** 3 for i in range(1, 6)]
print(f"Cube: {cube}")



# --- with condition---
# Syntax - [expression for item in iterable if condition]

# Even numbers only
even = [i for i in range(1, 21) if i % 2 == 0]
print(f"Even numbers: {even}")      # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Odd numbers only
odd = [i for i in range(1, 21) if i % 2 != 0]
print(f"Odd numbers: {odd}")        # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# scores above 60 only
all_scores = [45, 82, 91, 67, 38, 55, 79, 93, 41, 88]
all_scores.sort()
passed = [score for score in all_scores if score >= 60]
failed = [score for score in all_scores if score < 60]
print(f"Passed: {passed}")      # [82, 91, 67, 79, 93, 88]
print(f"Failed: {failed}")      # [45, 38, 55, 41]
print(f"Pass count: {len(passed)} | Fail count: {len(failed)}") # Pass count: 6 | Fail count: 4

print(all_scores)               # [38, 41, 45, 55, 67, 79, 82, 88, 91, 93]

# Multiples of 3
multiples_3 = [i for i in range(1, 31) if i % 3 == 0]
print(f"Mutiples of 3: {multiples_3}")      # [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]



#--- String operations with comprehension----
languages = ["Python", "French", "English", "Arabic"]

# Convert all to uppercase/ lowercase / capitalised
upper = [lang.upper() for lang in languages]
print(f"Uppercase: {upper}")

lower = [lang.lower() for lang in languages]
print(f"Lowercase: {lower}")

capitalised = [lang.capitalize() for lang in languages]
print(f"Capitalised: {capitalised}")

# only languages with more than 6 letters
lang6 = [lang for lang in languages if len(lang) > 6]
print(f"Long languages: {lang6}")

# Get length of each language name
length = [len(lang) for lang in languages]
print(f"Lengths: {length}")     # [6, 6, 7, 6]


# --- Real world localization use case ----
# Filter out empty translation segments
segments = ["Hello World!", "   ", "Bonjour", "  ", "Good morning", "    ", "Au revoir"]
print(segments)
clean = [seg.strip() for seg in segments if seg.strip()]
print(f"Clean segments: {clean}")  # ['Hello World!', 'Bonjour', 'Good morning', 'Au revoir']

# Count words in each segment
WC = [len(seg.split()) for seg in clean]
print(f"Word count: {WC}")      # [2, 1, 2, 2]



# --- DICTIONARY COMPREHENSION ---
# Syntax : {key: value for item in iterable}

# Basic dictionary comprehension
names = ["Farhan", "Ahmad", "Sara", "Rahul", "Priya"]
name_lengths = {name: len(name) for name in names}
print(f"Name lengths: {name_lengths}")   #{'Farhan': 6, 'Ahmad': 5, 'Sara': 4, 'Rahul': 5, 'Priya': 5}

# Squares dictionary
squares_dict = {i: i**2 for i in range(1, 6)}
print(f"Squares: {squares_dict}")   # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# With condition - only even squares
even_squares = {i: i**2 for i in range(1, 11) if i % 2 == 0}
print(f"Even squares: {even_squares}")  # {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

# Convert list of scores to pass/fail dict
scores = {"Farhan": 85, "Ahmed": 45, "Sara": 92, "Rahul": 55, "Priya": 78}
results = {name: "Pass" if score >= 60 else "Fail"
           for name, score in scores.items()}
print(f"Results: {results}")
#{'Farhan': 'Pass', 'Ahmed': 'Fail', 'Sara': 'Pass', 'Rahul': 'Fail', 'Priya': 'Pass'}