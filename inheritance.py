# INHERITANCE
# Week 3 - Wednesday
# Inheritance = a class can inherit attributes and
# methods from another class
# Parent class = base class
# Child class = derived class

#-----Parent class--------
class Animal:
    """Base class for all animals."""

    def __init__(self, name, age, sound):
        self.name = name
        self.age = age
        self.sound = sound

    def speak(self):
        """Makes the animal speak."""
        print(f"{self.name} says: {self.sound}!")

    def describe(self):
        """Describes the animal."""
        print(f"{self.name} is {self.age} years old.")

    def __str__(self):
        return f"Animal: {self.name}"
    

#------Child classes------
class Dog(Animal):
    """Dog inherits from Animal."""

    def __init__(self, name, age, breed):
        # Call parent __init__ using super()
        super().__init__(name, age, "Woof")
        self.breed = breed      # extra attribute

    def fetch(self):
        """Dog specific method."""
        print(f"{self.name} fetches the ball!")

    def __str__(self):
        return f"Dog: {self.name} ({self.breed})"
    

class Cat(Animal):
    """Cat inherits from Animal."""

    def __init__(self, name, age, indoor):
        super().__init__(name, age, "Meow")
        self.indoor = indoor        # True or False

    def purr(self):
        """Cat specific method."""
        print(f"{self.name} purs contentedly...")

    def describe(self):
        """Override parent method."""
        super().describe()      # call parent version first
        location = "indoor" if self.indoor else "outdoor"
        print(f"{self.name} is an {location} cat.")

    
class Bird(Animal):
    """Bird inherits from Animal."""

    def __init__(self, name, age, can_fly):
        super().__init__(name, age, "Tweet")
        self.can_fly = can_fly

    def fly(self):
        """Bird specific method."""
        if self.can_fly:
            print(f"{self.name} soars through the sky.")
        else:
            print(f"{self.name} cannot fly but runs fast.")


# Create object
dog = Dog("Bruno", 3, "Labrador")
cat = Cat("Whiskers", 5, True)
bird = Bird("Tweety", 2, True)

# Inherited methods
dog.speak()     # from Animal
cat.speak()     # from Animal
bird.speak()    # from Animal

# Overridden method
dog.describe()  # from Animal
cat.describe()  # overridden in Cat

# Child-specific methods
dog.fetch()
cat.purr()
bird.fly()

# str representation
print(dog)
print(cat)
print(bird)




# Multi-level inheritance-----
# Employee -> Manager -> Director

class Employee:
    """Base employee class."""

    company = "Cognizant"

    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def get_info(self):
        print(f"\n---Employee info---")
        print(f"Company : {Employee.company}")
        print(f"Name    : {self.name}")
        print(f"ID      : {self.emp_id}")
        print(f"Salary  : Rs. {self.salary:,}")

    def give_raise(self, percent):
        increase = self.salary * (percent / 100)
        self.salary += increase
        print(f"{self.name} got an {percent}% raise! New salary is Rs.{self.salary:,.0f}")

    def __str__(self):
        return f"Employee: {self.name} ({self.emp_id})"
    
class Manager(Employee):
    """Manager inherits from Employee."""

    def __init__(self, name, emp_id, salary, department):
        super().__init__(name, emp_id, salary)
        self.department = department
        self.team = []          # list of employees

    def add_team_member(self, employee):
        """Adds employee to the team."""
        self.team.append(employee)
        print(f"\n{employee.name} added to {self.name}'s team")

    def get_info(self):
        super().get_info()
        print(f"Role    : Manager")
        print(f"Dept    : {self.department}")
        print(f"Team    : {len(self.team)} members")

    def __str__(self):
        return f"Manager: {self.name} ({self.department})"
    

class Director(Manager):
    """Director inherits from Manager."""

    def __init__(self, name, emp_id, salary, department, budget):
        super().__init__(name, emp_id, salary, department)
        self.budget = budget

    def approve_budget(self, amount):
        """Approves a budget request."""
        if amount <= self.budget:
            print(f"Budget of Rs. {amount:,} approved by {self.name}")
        else:
            print(f"Budget request of Rs. {amount} exceeds available Rs.{self.budget:,}")

    def get_info(self):
        super().get_info()
        print(f"Role    : Director")
        print(f"Budget  : Rs.{self.budget:,}")

    def __str__(self):
        return f"Director: {self.name} ({self.department})"
    

# Create objects
emp1 = Employee("Farhan Ahmad", "EMP001", 60000)
emp2 = Employee("Yusuf Ansari", "EMP002", 80000)
mgr1 = Manager("Sara Ali", "MGR001", 90000, "Localization")
dir1 = Director("Rahul Sharma", "DIR001", 150000, "Technology", 1000000)

# Add Team members
mgr1.add_team_member(emp1)
mgr1.add_team_member(emp2)

# Display info
emp1.get_info()
mgr1.get_info()
dir1.get_info()

# Methods
emp1.give_raise(10)
dir1.approve_budget(500000)
dir1.approve_budget(600000)

# isinstance() - check if object is instance of class
print(f"\nisinstance checks:")
print(f"mgr1 is Employee    : {isinstance(mgr1, Employee)}")
print(f"mgr1 is Manager     : {isinstance(mgr1, Manager)}")
print(f"mgr1 is Director    : {isinstance(mgr1, Director)}")
print(f"dir1 is Manager     : {isinstance(dir1, Manager)}")