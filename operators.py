# ARITHMETIC OPERATORS
# Week 1 - Thursday

a = 20
b = 6

print(f"{a} + {b} = {a + b}")       # 26 - addition
print(f"{a} - {b} = {a - b}")       # 14 - subtraction
print(f"{a} * {b} = {a * b}")       # 120 - multiplication
print(f"{a} ? {b} = {a / b}")       # 3.333 - always gives float, decimal if it is
print(f"{a} // {b} = {a // b}")     # 3 - floor division, no decimal
print(f"{a} % {b} = {a % b}")       # 2 - remainder after division
print(f"{a} ** {b} = {a ** b}")     # 64000000 - 20 to the power of 6



# COMPARISON OPERATORS
# These always give True or False

x = 10
y = 20

print(f"{x} == {y} -> {x == y}")        # False - are they equal?
print(f"{x} != {y} -> {x != y}")        # False - are they not equal?
print(f"{x} > {y} -> {x > y}")          # False - is x greater?
print(f"{x} < {y} -> {x < y}")          # True - is x smaller?
print(f"{x} >= 10 -> {x >= 10}")        # True - greater than or equal?
print(f"{x} <= 9 -> {x <= 9}")          # False - less than or equal?

# Comparing strings
name1 = "Farhan"
name2 = "farhan"
print(f"'Farhan' == 'farhan' -> {name1 == name2}")      #False - case sensitive!
print(f"'Farhan' == 'farhan' (fixed) -> {name1.lower () == name2.lower ()}")      #True


# TYPE CONVERSION - critical concept!
# input() ALWAYS returns a string, even if user types a number

# This will cause an ERROR - try it first
# age = input("Enter age :")
# print(age + 1)    # TypeError! Can't add string and number

# CORRECT way - convert it to int first
age_text = input("Enter your age :")
age_number = int(age_text)      # convert string -> integer
print(f"Next year you will be {age_number + 1}")
print(f"In 10 years : {age_number + 10}")


# Float conversion
height = float(input("Enter your height in cm: "))
print(f"Your height in metres: {height / 100:.3f}m")


# Converting number back to string
score = 95
message = "Your score is " + str(score) + " out of 100"
print(message)


# Check types before and after conversion
value = "42"
print(f"Before: {type(value)}")     # class 'str'>
converted = int(value)
print(f"After: {type(converted)}")     # class 'int'>



# AUGMENTED ASSIGNMENT - shortcuts for updating variables
score = 100
print(type(score))

score += 10                         # same as score = score + 10
print(f"After +=10: {score}")       # 110

score -= 5                         # same as score = score - 5
print(f"After -=5: {score}")       # 105

score *= 2                         # same as score = score * 2
print(f"After *=2: {score}")            # 210

score /= 2                         # same as score = score * 2
print(f"After /=2: {score}")            # 210

score //= 2                         # same as score = score // 2
print(f"After //=2: {score}")            # 210

score **= 2                         # same as score = score ** 2
print(f"After **=2: {score}")            # 210

