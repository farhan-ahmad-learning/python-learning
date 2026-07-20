# Functions Deep Practice
# Week 2 - Saturday

# ----------Nested functions-----------
# Functions can be defined inside other functions

def outer_function(name):
    """Outer function that contains an inner function."""

    def inner_function(greeting):
        """Inner function. Only accessible inside outer."""
        return f"{greeting} {name}!"
    
    # Call inner function from inside outer
    english = inner_function("Hello")
    french = inner_function("Bonjour")
    arabic = inner_function("Marhaba")

    return [english, french, arabic]

greetings = outer_function("Farhan")
for g in greetings:
    print(g)
# Hello Farhan!
# Bonjour Farhan!
# Marhaba Farhan!


#---Functions calling another function-----
# This is how real programs are structured.

def get_grade(score):
    """Returns grade letter based on score."""
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 40:
        return "D"
    else:
        return "F"

def get_status(score):
    """Returns pass or fail status."""
    return "Pass" if score >= 40 else "Fail"

def get_remarks(score):
    """Returns remarks based on score."""
    if score >= 90:
        return "Excellent performance!"
    elif score >= 75:
        return "Good work - Keep it up!"
    elif score >= 60:
        return "Average - room for improvement"
    elif score >= 40:
        return "Below average - need more effort"
    else:
        return "Failed - please retake"

def generate_report(name, score):
    """
    Generated full student report.
    Call other functions to build the report.
    """
    grade = get_grade(score)        # calls get_grade
    status = get_status(score)      # calls get_status
    remarks = get_remarks(score)    # calls get_remarks

    print("\n====STUDENT REPORT====")
    print(f"Name        : {name}")
    print(f"Score       : {score}/100")
    print(f"Grade       : {grade}")
    print(f"Status      : {status}")
    print(f"Remarks     : {remarks}")
    print(f"=======================")

generate_report("Farhan", 45)
generate_report("Yusuf", 91)




#-----Functions working with Lists---------
def filter_scores(scores, minimum):
    """Return scores above minimum threshold"""
    return [s for s in scores if s >= minimum]

def calculate_stats(scores):
    """Returns statistics dictionary for a list of scores."""
    return {
        "count"     : len(scores),
        "total"     : sum(scores),
        "min"       : min(scores),
        "max"       : max(scores),
        "average"   : round(sum(scores)/len(scores), 1),
        "passed"    : len([s for s in scores if s >= 40]),
        "failed"    : len([s for s in scores if s < 40])
    }

def top_scorers(students, n):
    """"Returns top n students sorted by score."""
    sorted_students = sorted(
        students,
        key = lambda x: x["score"],
        reverse=True
    )
    return sorted_students[:n]

# Test all 3 functions
all_scores = [45, 82, 91, 67, 38, 55, 79, 93, 41, 88]
print(f"\nAll scores        : {all_scores}")
print(f"Above 70            : {filter_scores(all_scores, 70)}")
print(f"Above 80            : {filter_scores(all_scores, 80)}")

stats = calculate_stats(all_scores)
print(f"\n===== STATISTICS =====")
for key, value in stats.items():
    print(f"{key.title():<10}: {value}")

students_list = [
    {"name":"Farhan", "score":85},
    {"name":"Ahmed", "score":45},
    {"name":"Sara", "score":92},
    {"name":"Rahul", "score":67},
    {"name":"Priya", "score":78},
    {"name":"Rahul", "score":91},
]
print(f"\nTop 3 students:")
for rank, student in enumerate(top_scorers(students_list, 3), 1):
    print(f"    {rank}. {student['name']} - {student['score']}")



# --------Temperature converter functions-----
def celsius_to_fahrenheit(c):
    """Converts celsius to fahrenheit."""
    return round((c* 9/5) + 32, 1)

def fahrenheit_to_celsius(f):
    """Converts fahrenheit to celsius."""
    return round((f - 32) * 5/9, 1)

def celsius_to_kelvin(c):
    """Converts celsius to kelvin."""
    return round(c + 273.15, 2)

def convert_all(temp, unit="C"):
    """
    Converts temperature to all units.
    Args:
    temp: Temperature value
    unit: C for celsius, F for fahrenheit
    
    Returns:
    Dictionary with all conversions
    """
    if unit.upper() == "C":
        return {
            "celsius"   : temp,
            "fahrenheit": celsius_to_fahrenheit(temp),
            "kelvin"    : celsius_to_kelvin(temp)
        }
    elif unit.upper() == "F":
        celsius = fahrenheit_to_celsius(temp)
        return {
            "celsius"   : celsius,
            "fahrenheit": temp,
            "kelvin"    : celsius_to_kelvin(celsius)
        }
    else:
        return "Invalid unit - use C or F"
    
# Test conversions
temp_to_convert = [0, 20, 37, 100]
print(f"\n==== TEMPERATURE CONVERSIONS ====")
print(f"{'Celsius':<12} {'Fahrenheit':<15} {'Kelvin'}")
print(f"{'-------':<12} {'----------':<15} {'------'}")

print()
result_f = convert_all(98.6, "F")
print(f"98.6 F = {result_f['celsius']}°C = {result_f['kelvin']}K")