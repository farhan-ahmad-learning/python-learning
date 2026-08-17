# FILE I/O — Reading and Writing Files
# Week 3 - Thursday

import os 

#---Writing to a file-----
# "w" = write mode - created file or overwrites existing
# "a" = append mode - adds to existing file
# "r" = read mode - reads existing file


# Write mode
with open("test.txt", "w") as file:
    file.write("Hello World\n")
    file.write("This is my first file\n")
    file.write("Python file I/O is powerful!\n")

print("File written successfully!")


# Append mode - adds to existing content
with open("test.txt", "a") as file:
    file.write("This line was appended.\n")
    file.write("And this one too!\n")

print("Content appended successfully!")


# Write multiple lines at once
lines = [
    "Line 1 - Python\n"
    "Line 2 - French\n"
    "Line 3 - AWS\n"
    "Line 4 - Business Analysis\n"
]

with open("skills.txt", "w") as file:
    file.writelines(lines)

print("Skills file created!")



#----Reading from a file---------

# Read entire file as one string
with open("test.txt", "r") as file:
    #content = file.read()
    print("====Full File Content====")
    print(file.read())

# Read line by line
with open("test.txt", "r") as file:
    print("====Line by Line====")
    for line in file:
        print(line.strip())     # strip() removes \n

# Read all lines into a list
with open("test.txt", "r") as file:
    lines = file.readlines()
    print(f"\nTotal lines: {len(lines)}")
    print(f"First line: {lines[0].strip()}")
    print(f"Last line: {lines[-1].strip()}")

# Read one line at a time
with open("test.txt", "r") as file:
    first = file.readline()
    second = file.readline()
    print(f"\nFirst: {first.strip()}")
    print(f"Second: {second.strip()}")


# Error handling with files----
# Always handle FileNotFoundError

def read_file_safe(filename):
    """Safely reads a file with error handling."""
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        return f"Error: File '{filename}' not found!"
    except PermissionError:
        return f"Error: No permission to read '{filename}'"
    
print(read_file_safe("test.txt"))
print(read_file_safe("missing.txt"))


# Check if file exists before opening
def file_exists(filename):
    """Checks if a file exists."""
    return os.path.exists(filename)

print(f"\ntest.txt exists   : {file_exists('test.txt')}")
print(f"missing.txt exists   : {file_exists('missing.txt')}")


# Write student data to file
def save_student_data(students, filename):
    """Saves student data to a text file."""
    with open(filename, "w") as file:
        file.write("==== STUDENT DATA ====\n")
        for name, data in students.items():
            file.write(f"Name   : {name}\n")
            file.write(f"Average: {data['average']}\n")
            file.write(f"Grade  : {data['grade']}\n")
            file.write("-" * 25 + "\n")
    print(f"Student data saved to {filename}")


def load_and_display(filename):
    """Loads and displays file content."""
    content = read_file_safe(filename)
    print(f"\n==== {filename.upper()} ====")
    print(f"\n{content}")

# Test with sample data
students = {
    "Farhan Ahmad": {"average": 85.0, "grade": "B"},
    "Ahmed Khan":   {"average": 72.7, "grade": "C"},
    "Sara Ali":     {"average": 91.3, "grade": "A"}
}

save_student_data(students, "students.txt")
load_and_display("students.txt")

#--clean up - delete test files---
for f in ["test.txt", "skills.txt", "students.txt"]:
    if file_exists(f):
        os.remove(f)
        print(f"Deleted: {f}")

