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