# LISTS
# Week 2 - Monday

# ------Creating Lists-----------
fruits = ["mango", "apple", "banana", "guava", "orange"]
numbers = [10, 20, 30, 40, 50]
mixed = ["farhan", 35, True, 3.14]      # lists can mix types
empty = []                              # empty list

print(fruits)
print(numbers)
print(mixed)


#--------- Indexing - accessing items ---------
print(fruits[0])        # mango - first item
print(fruits[1])        # apple - second item
print(fruits[-1])       # orange - last item           
print(fruits[-2])       # guava - second from last


#---------- Slicing - getting multiple items ---------
print(fruits[0:3])      # ['mango', 'apple', 'banana']
print(fruits[2:])       # from index 2 to end ['banana', 'guava', 'orange']
print(fruits[:3])       # from start to index 2 ['mango', 'apple', 'banana']
print(fruits[::2])      # every second item
print(fruits[::-1])     # reverse


# --------- List info -------------
print(len(fruits))          # 5 - number of items
print("mango" in fruits)    # True
print("grapes" in fruits)   # False


# LIST METHODS
skills = ["Python", "French", "English"]

# Adding items
skills.append("AWS")        # add to end
skills.insert(0, "Excel")   # add to start position
print (skills)

# Removing items
skills.remove("Excel")      # remove by value
popped = skills.pop()       # remove and return last item
print(f"Removed: {popped}") # AWS
print (skills)

# Other useful methods
numbers = [30, 10, 50, 20, 40]
numbers.sort()          # sort ascending
print(numbers)

numbers.sort(reverse=True)  # sort descending
print(numbers)

numbers.reverse()           # reverse order
print(numbers)

print(numbers.count(30))    # count occurences
print(numbers.index(10))    # find position

# Copy a list
original = [1, 2, 3]
copy = original.copy()      # proper way to copy
print(copy)
copy.append(4)
print(original)             # [1, 2, 3] - unchanged
print(copy)                 # [1, 2, 3, 4]



# LOOPING THROUGH LISTS
languages = ["Python", "French", "English", "Arabic"]

# Basic loop
for lang in languages:
    print(f"I speak {lang}")

# Loop with index
for i, lang in enumerate(languages, 1):
    print(f"{i}. {lang}")

# Loop and modify
scores = [45, 82, 91, 67, 55]
passed = []
failed = []

for score in scores:
    if score >= 60:
        passed.append(score)
    else:
        failed.append(score)

print(f"Passed: {passed}")
print(f"Failed: {failed}")
print(f"Pass rate: {len(passed)}/{len(scores)}")