# TUPLES AND SETS
# Week 2 - Tuesday

# -- TUPLES - ordered, unchangeable-----
# Use tuples for data that should NOT change
coordinates = (28.6139, 77.2090)    # Delhi coordinates
rgb_red = (255, 0, 0)               # RGB colour - never changes
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

print(coordinates[0])   # 28.6139
print(coordinates[1])   # 77.2090
print(len(days))        # 7


# Tuple unpacking - very useful
latitude, longitude = coordinates
print(f"Latitude: {latitude}")
print(f"Longitude: {longitude}")

name, age, city = ("Farhan", 37, "Delhi")
print(f"{name} is {age} from {city}")

# Tuples are faster than lists
# Use when data is fixed - months, days, RGB values


# ----SETS - unordered, no duplicates-----
# Use sets when you need unique values only
fruits = {"mango", "banana", "apple", "mango", "banana"}
print(fruits)       # duplicates removed automatically!


languages = {"Python", "French", "English"}

# Set operations - very powerful
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print(set_a | set_b)        # Union - all items from both  {1, 2, 3, 4, 5, 6, 7, 8}
print(set_a & set_b)        # intersection - common items  {4, 5}
print(set_a-set_b)          # Difference - in A but not B  {1, 2, 3}

# Real use case - find unique words in a sentence
sentence = "the cat sat on the mat the cat"
words = sentence.split()
unique_words = set(words)
print(words)
print(f"Total words: {len(words)}")
print(f"Unique words: {len(unique_words)}")
print(f"Duplicate words removed: {unique_words}")