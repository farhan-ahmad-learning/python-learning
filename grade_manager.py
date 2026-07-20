def calculate_average(scores):
    return round(sum(scores)/len(scores), 1)

def assign_grade(average):
    """Returns grade letter based on score."""
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"

def get_status(average):
    return "Pass" if average >= 40 else "Fail"

def add_student(students, name, scores):
    average = calculate_average(scores)
    grade = assign_grade(average)
    status = get_status(average)

    students[name] = {
        "scores"    : scores,
        "average"   : average,
        "grade"     : grade,
        "highest"   : max(scores),
        "lowest"    : min(scores),
        "status"    : status
    }

    print(f"    ✓ {name:<15} added - Scores: {scores}")

def display_report(students):
    print(f"\n===== CLASS REPORT =====\n")
    print(f"{'Name':<16} {'Avg':<7} {'Grade':<7} {'High':<6} {'Low':<6} Status")
    print(f"{'-------':<16} {'-----':<7} {'-----':<7} {'----':<6} {'---':<6} ------")

    for name, data in students.items():
        print(f"{name:<16} "
              f"{data['average']:<7} "
              f"{data['grade']:<7} "
              f"{data['highest']:<6} "
              f"{data['lowest']:<6} "
              f"{data['status']}"
              )

def display_summary(students):
    total = len(students)
    all_averages = [data["average"] for data in students.values()]
    class_avg = round(sum(all_averages) / len(all_averages), 1)
    passed = sum(1 for data in students.values() if data ["status"] == "Pass")
    failed = total - passed

    top_name = max(students, key=lambda x: students[x]["average"])
    top_avg = students[top_name]["average"]

    print(f"\n===== CLASS SUMMARY =====")
    print(f"Total Students : {total}")
    print(f"Class Average  : {class_avg}")
    print(f"Top Student    : {top_name} ({top_avg})")
    print(f"Passed         : {passed}")
    print(f"Failed         : {failed}")
    print(f"==========================")

print(f"===== STUDENT GRADE MANAGER =====")
print("\nAdding students....")

students = {}
add_student(students, "Farhan Ahmad",  [85, 92, 78])
add_student(students, "Ahmed Khan",    [67, 71, 80])
add_student(students, "Sara Ali",      [91, 95, 88])
add_student(students, "Rahul Sharma",  [45, 52, 48])
add_student(students, "Priya Gupta",   [78, 85, 90])

display_report(students)
display_summary(students)




    

