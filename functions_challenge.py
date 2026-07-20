# FUNCTIONS CHALLENGE
# Week 2 - Friday
# Build all functions yourself!

# Challenge 1:
# Write a function that takes a sentence and returns:
# - word count
# - character count (no spaces)
# - most common letter

def analyze_text(sentence):
    words = len(sentence.split())
    chars = len(sentence.replace(" ",""))
    letters_only = sentence.lower().replace(" ", "")
    most_common = max(letters_only, key=letters_only.count)
    
    return {
        "words": words,
        "chars": chars,
        "most_common": most_common
    }
    
result = analyze_text("Python is amazing for localization")
print(f"\nChallenge 1 - Text Analysis:")
print(f"    Words       :   {result['words']}")
print(f"    Characters  :   {result['chars']}")
print(f"    Most common :   {result['most_common']}")

print()

# Challenge 2:
# Write a function that converts a list of temperatures
# from Celsius to Fahrenheit and returns only
# temperatures above 100°F

def hot_temps(*celsius_temps):
    fahrenheit = [(c * 9/5) + 32 for c in celsius_temps]
    hot = [round(f, 1) for f in fahrenheit if f > 100]
    return hot

print("Challenge 2 - Hot Temperatures:")
print(f"    {hot_temps(20, 35, 40, 45, 50)}")


# Challenge 3:
# Write a function that takes **student_scores
# (name=score pairs) and returns a dictionary
# with name: grade (A/B/C/D/F)
def assign_grades(**student_scores):
    grades = {}
    for name, score in student_scores.items():
        if score >= 90:
            grades[name] = "A"
        elif score >= 75:
            grades[name] = "B"
        elif score >= 60:
            grades[name] = "C"
        elif score >= 40:
            grades[name] = "D"
        else:
            grades[name] = "F"
    return grades

print(f"Challenge 3 - Assign Grades:")
result = assign_grades(Farhan=85, Ahmad=45, Sara=92, Rahul=67)
for name, grade in result.items():
    print(f"    {name}: {grade}")





# Challenge 4 - Palindrome
print(f"\nChallenge 4 ---------")
def is_palindrome(word):
    cleaned = word.lower().replace(" ", "")
    return cleaned == cleaned[::-1]
    
test_words = ["racecar", "python", "madam", "level", "hello", "civic"]
for word in test_words:
    result2 = is_palindrome(word)
    symbol = "v" if result2 else "x"
    print(f"    {symbol}  '{word}' - {result2}")
print()



# Challenge 5 — Sort Students by Score:
#  Rank   Name       Score
#  ----   ----       -----
#  1      Sara       92
#  2      Farhan     85
#  3      Rahul      67
#  4      Ahmed      45

def sort_students(students):
    return sorted(students, key=lambda x: x["score"], reverse=True)

print("Challenge 5 - Sort students by score:")
students = [
    {"name": "Farhan", "score": 85},
    {"name": "Ahmad",  "score": 45},
    {"name": "Sara",   "score": 92},
    {"name": "Rahul",  "score": 67}
]

sorted_students = sort_students(students)
print(f"    {'Rank':<6} {'Name':<10} {'Score'}")
print(f"    {'----':<6} {'----':<10} {'-----'}")
for rank, student in enumerate(sorted_students, 1):
    print(f"    {rank:<6} {student['name']:<10} {student['score']}")