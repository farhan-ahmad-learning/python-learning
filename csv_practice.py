# CSV FILES
# Week 3 - Friday
# CSV = Comma Separated Values
# Used everywhere — Excel, databases, data exchange

import csv
import os

# ----Writing csv files--------
students = [
    ["Name",         "Age", "Course",              "Score"],
    ["Farhan Ahmad", 35,    "Python + AWS",        85],
    ["Ahmed Khan",   28,    "Python",              67],
    ["Sara Ali",     31,    "Business Analysis",   92],
    ["Rahul Sharma", 25,    "AWS",                 45],
    ["Priya Gupta",  29,    "Python + BA",         78],
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students)

print("students.csv created!")


# ---Reading csv-----------------
print(f"\n==== READING CSV ====")
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# ---Reading csv as dictionary------
print(f"\n==== CSV as DICTIONARY ====")
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"{row['Name']:<15} Score: {row['Score']}")

# ---Writing csv from dictionary---
student_dicts = [
    {"Name": "Farhan", "Score": 85, "Grade": "B"},
    {"Name": "Ahmed",  "Score": 45, "Grade": "D"},
    {"Name": "Sara",   "Score": 92, "Grade": "A"},
]

with open("grades.csv", "w", newline="") as file:
    fieldnames = ["Name", "Score", "Grade"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()            # writes column names
    writer.writerows(student_dicts)
print("\ngrades.csv created!")


# ---Practical - analyze csv data---
def analyze_csv(filename):
    """Reads CSV and returns statistics."""
    scores = []
    names = []

    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            names.append(row["Name"])
            scores.append(int(row["Score"]))

    return {
        "total"  : len(scores),
        "average": round(sum(scores)/len(scores),1),
        "highest": max(scores),
        "lowest" : min(scores),
        "top"    : names[scores.index(max(scores))]
    }

stats  = analyze_csv("students.csv")
print(f"\n==== CSV Analysis ====")
for key, value in stats.items():
    print(f"{key.title():<10} : {value}")


# Cleanup
for f in ["students.csv", "grades.csv"]:
    if os.path.exists(f):
        os.remove(f)