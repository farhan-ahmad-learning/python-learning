# Updated via Git terminal - Week 1

# CONDITIONS - if / elif / else
# Week 1 - Saturday

# ------Basic if/else---------
age = int(input ("Enter your age: "))
if age >= 18:
    print(f"You are an adult.")
else:
    print(f"You are a minor.")


# ----if / elif / else---------
score = int(input("Enter exam score (0-100): "))

if score >= 90:
    print(f"Grade A - Distinction.")
elif score >= 75:
    print(f"Grade B - Good.")
elif score >= 60:
    print(f"Grade C - Average")
elif score >= 40:
    print(f"Grade D - Below Average")
else:
    print(f"Grade F - Fail")



# LOGICAL OPERATORS - and, or , not
# and - both conditions must be True
# or - atleast one condition must be True
# not - reverses True to False or False to True

age = int(input("Enter age: "))
has_id = input("Do you have ID? (yes/no): ").lower()
is_member = input("Are you a member? (yes/no): ").lower()

# AND - both conditions must be True
if age >= 18 and has_id == "yes":
    print("Access granted!")
else:
    print("Access denied.")

# OR - atleast one must be True
if age >= 18 or is_member == "yes":
    print("You qualify for discount.")
else:
    print("No discount available.")

# NOT - reverses the condition
if not has_id == "yes":
    print("Please bring your ID  next time.")



# NESTED CONDITIONS
salary = float(input("Enter monthly salary: "))
experience = int(input("Years of experience: "))
has_certification = input("AWS certified? (yes/no)").lower()

if salary >=50000:
    if experience >= 3:
        if has_certification == "yes":
            print("Senior role - eligible for promotion!")
        else:
            print("Get certified to qualify for promotion.")
    else:
        print("Need 3+ years of experience for promotion.")
else:
    print("Salary below threshold for promotion.")

# TERNARY OPERATOR - shorthand if/else in one line
# result = value_if_true if condition else value_if_false
status = "Adult" if age >= 18 else "Minor"
print(f"Status: {status}")

grade = "Pass" if score >= 40 else "Fail"
print(f"Result: {grade}")