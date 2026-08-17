# JSON FILES
# Week 3 - Friday
# JSON = JavaScript Object Notation
# Standard format for APIs and web data

import json
import os

# ---Writing json------
student_data = {
    "school": "Cognizant Academy",
    "year"  : 2026,
    "students": [
        {
            "name"  : "Farhan Ahmad",
            "age"   : 35,
            "scores": [85, 92, 78],
            "active": True
        },
        {
            "name"  : "Ahmed Khan",
            "age"   : 28,
            "scores": [67, 71, 80],
            "active": True
        },
        {
            "name"  : "Sara Ali",
            "age"   : 31,
            "scores": [91, 95, 88],
            "active": False
        }
    ]
}

# Write to JSON file
# indent=4 makes it human readable
with open("students.json", "w") as file:
    json.dump(student_data, file, indent=4)

print("students.json created!")


# ----Reading JSON------
with open("students.json", "r") as file:
    loaded_data = json.load(file)

print(f"\nSchool    : {loaded_data['school']}")
print(f"Year        : {loaded_data['year']}")
print(f"Total       : {len(loaded_data['students'])} students")

print(f"\n==== STUDENTS ====")
for student in loaded_data["students"]:
    avg = sum(student["scores"]) / len(student["scores"])
    status = "Active" if student["active"] else "Inactive"
    print(f"{student['name']:<15} Avg: {avg:.1f}  Status: {status}")


# ---JSON string conversion----
# Convert dict to JSON string
data_dict = {"name": "Farhan", "age": 35, "city": "Delhi"}
json_string = json.dumps(data_dict, indent=2)
print(f"\nJSON string:\n{json_string}")

# Convert JSON string back to dict
back_to_dict = json.loads(json_string)
print(f"\nBack to dict: {back_to_dict}")
print(f"Type: {type(back_to_dict)}")

# Practical - load and save settings
def save_settings(settings, filename):
    """Saves settings to JSON file."""
    with open(filename, "w") as file:
        json.dump(settings, file, indent=4)
        print(f"Settings saved to {filename}")

def load_settings(filename):
    """Loads settings from JSON file."""
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    
settings = {
    "theme"         : "dark",
    "language"      : "French",
    "auto_save"     : True,
    "font_size"     : 14,
    "recent_files"  : ["hello.py", "calculator.py"]
}

save_settings(settings, "settings.json")
loaded = load_settings("settings.json")
print(f"\nLoaded theme        : {loaded['theme']}")
print(f"Loaded langauage    : {loaded['language']}")
print(f"Recent files        : {loaded['recent_files']}")

# Clean up
for f in ["students.json", "settings.json"]:
    if os.path.exists(f):
        os.remove(f)




