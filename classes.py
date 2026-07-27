# CLASSES AND OBJECTS
# Week 3 - Monday

# -------Defining a class---------
# class = blueprint for creating objects
# object = an instance of a class

class Dog:
    """Blueprint for creating Dog objects."""

    # __init__ = constructor - runs when an object is created
    # self = refer to the object being created
    def __init__(self, name, breed, age):
        self.name = name    #attribute
        self.breed = breed  #attribute
        self.age = age      #attribute

    def bark(self):
        """Makes the dog bark."""
        print(f"{self.name} says: Woof!")

    def describe(self):
        """Describes the dog."""
        print(f"{self.name} is a {self.age} year old {self.breed}.")

    def have_birthday(self):
        """Increases age by 1."""
        self.age += 1
        print(f"Happy birthday {self.name}! Now {self.age} years old.")


# Creating objects------
# object_name = ClassName(arguments)
dog1 = Dog("Bruno", "Labrador", 3)
dog2 = Dog("Max", "Poodle", 5)
dog3 = Dog("Buddy", "Beagle", 1)

# Calling methods-------
dog1.bark()
dog2.bark()
dog3.bark()

dog1.describe()
dog2.describe()

dog1.have_birthday()
dog1.describe()


#--Accessing attributes directly------
print(f"\nDog 1 name: {dog1.name}")
print(f"Dog 1 breed: {dog1.breed}")
print(f"Dog 1 age: {dog1.age}")


#--Modifying attributes directly--------
dog1.name = "Bruno Max"
print(f"New name: {dog1.name}")






#------A practical class - Student--------
class Student:
    """Represents a student with scores."""

    # Class variable - shared by ALL objects
    school_name = "Cognizant Academy"
    total_students = 0

    def __init__(self, name, age, course):
        # Instance variables - unique to each object
        self.name = name
        self.age = age
        self.course = course
        self.scores = []            # empty list to start

        # Update class variable
        Student.total_students += 1
    
    def add_score(self, score):
        """Adds a score to student's list."""
        self.scores.append(score)
        print(f"Score {score} added for {self.name}")

    def get_average(self):
        """Returns average score."""
        if len(self.scores) == 0:
            return 0
        return round(sum(self.scores) / len(self.scores), 1)
    
    def get_grade(self):
        """Returns grade based on average."""
        avg = self.get_average()
        if avg >= 90: return "A"
        if avg >= 75: return "B"
        if avg >= 60: return "C"
        if avg >= 40: return "D"
        else:         return "F"

    def display(self):
        """Displays full student information."""
        print(f"\n===== STUDENT INFO =====")
        print(f"School  : {Student.school_name}")
        print(f"Name    : {self.name}")
        print(f"Age     : {self.age}")
        print(f"Course  : {self.course}")
        print(f"Scores  : {self.scores}")
        print(f"Average : {self.get_average()}")
        print(f"Grade   : {self.get_grade()}")
        print(f"========================")

    
# Create students
s1 = Student("Farhan", 35, "Python + AWS")
s2 = Student("Ahmad",  28, "Python")
s3 = Student("Sara",   31, "Business Analysis")

# Add scores
s1.add_score(85)
s1.add_score(92)
s1.add_score(78)

s2.add_score(67)
s2.add_score(71)
s2.add_score(80)

s3.add_score(91)
s3.add_score(95)
s3.add_score(88)

# Display info
s1.display()
s2.display()
s3.display()

# Class variable - shared by all
print(f"\nTotal students enrolled: {Student.total_students}")