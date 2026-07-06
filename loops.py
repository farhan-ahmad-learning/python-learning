# FOR LOOPS
# Week 1 - Saturday

# --------Basic for Loop----------------
languages = ["Python", "French", "English", "Arabic"]

for language in languages:
    print(f"I know {language}")


# ---------Loop with range()------------
# range(stop) - 0 to stop-1
for i in range(5):
    print(f"Count: {i}")            # 0, 1, 2, 3, 4

# range(start, stop)
for i in range(1, 6):
    print(f"Day {i} of learning")   # 1, 2, 3, 4, 5

# range (start, stop, step)
for i in range(0, 11, 2):
    print(i)                        # 0, 2, 4, 6, 8, 10

# ----enumerate() - index + value together---------
skills = ["Python", "AWS", "Business Analysis", "French"]
for index, skill in enumerate(skills, 0):
    print(f"{index}. {skill}")
# 1. Python
# 2. AWS
# 3. Business Analysis
# 4. French

# ---------Nested for loop--------------
subjects = ["Python", "AWS"]
days = ["Monday", "Tuesday", "Wednesday"]

for subject in subjects:
    for day in days:
        print(f"Study {subject} on {day}")


# WHILE LOOPS
# ------Basic WHILE Loop----
Count = 1
while Count >=5:
    print(f"Count: {Count}")
    count = +1              #always update or infinite loop!

# ---------Password checker------
password = "python123"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    guess = input("Enter password: ")
    if guess == password:
        print("Access granted.")
        break
    else:
        attempts += 1
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"Wrong! {remaining} attempts remaining.")

if attempts == max_attempts:
    print("Account locked! Too many wrong attempts.")


# -break and continue---------
# break - exits loop completely
# continue - skips to next iteration

print("\nNumbers that are not multiples of 3:")
for num in range(1, 15):
    if num % 3 == 0:
        continue                # skip multiples of 3
    print(num)

print("\nStop at first multiple of 7:")
for num in range(1, 50):
    if num % 7 == 0:
        print(f"Found it: {num}")
        break