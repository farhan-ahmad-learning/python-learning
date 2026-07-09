# DICTIONARIES - Key: value pairs
# Week 2 - Wednesday

# ----------Creating dictionaries--------
person = {
    "name" : "Farhan",
    "age" :35,
    "city" : "New Delhi",
    "job" : "Localization Professional",
    "languages" : ["Python", "French", "English"]
}

# ------Accessing values----------
print(person)
print(person["name"])               # Farhan
print(person["age"])                # 35
print(person["languages"])          # ['Python', 'French', 'English']
print(person["languages"][0])       # Python - item in nested list

# Safe access - won't crash if key doesn't exist
print(person.get("Salary", "Not found"))    # Not found
print(person.get("country"))                # None

#----Modifying dictionaries--------
person["age"] = 36
person["salary"] = 60000
person["city"] = "Mumbai"
del person["city"]

print(person)


# Check if key exists
if "salary" in person:
    print(f"Salary found: {person['salary']}")

if "city" not in person:
    print(f"City key was deleted successfully.")


# ---Dictionary methods--------
print(person.keys())        # all keys
print(person.values())      # all values
print(person.items())       # all key-value pairs as tuples

#---Looping through dictionary--------
print("\n==== PERSON DETAILS ====")
for key, value in person.items():
    print(f"{key.title()}: {value}")

#==== PERSON DETAILS ====
# Name: Farhan
# Age: 36
# Job: Localization Professional
# Languages: ['Python', 'French', 'English']
# Salary: 60000



# ----Nested dictionary-----
employees = {
    "EMP001": {
        "name": "Farhan Ahmad",
        "department": "Localization",
        "salary": 60000,
        "skills": ["Python", "French", "English"]
    },
    "EMP002": {
        "name": "Ahmad Khan",
        "department": "Development",
        "salary": 75000,
        "skills": ["Python", "AWS", "Docker"] 
    },
    "EMP003": {
        "name": "Sara Ali",
        "department": "Business Analysis",
        "salary": 65000,
        "skills": ["Jira", "SQL", "Python"] 
    }
}

# Accessing nested values
print(employees["EMP001"]["name"])      # Farhan Ahmad
print(employees["EMP002"]["salary"])    # 75000
print(employees["EMP003"]["skills"][1]) # SQL

# Loop through nested dictionary
print(f"\n=====Employee Directory=====")
for emp_id, details in employees.items():
    print(f"\n{emp_id}:")
    print(f"Name        :   {details['name']}") 
    print(f"Department  :   {details['department']}")
    print(f"Salary      :   Rs. {details['salary']:,}")
    print(f"Skills      :   {', '.join(details['skills'])}")