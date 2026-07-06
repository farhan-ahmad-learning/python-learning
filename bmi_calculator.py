<<<<<<< HEAD
name = input("Enter name: ")
weight = int(input("Enter weight (Kg): "))
height = float(input("Enter height (cms): "))

height_m = height/100
BMI = weight / (height_m ** 2)

if BMI < 18.5:
    category = "Underweight"
elif BMI < 25:
    category = "Normal weight"
elif BMI < 30:
    category = "Overweight"
else:
    category = "Obese"

print()
print(f"Name    : {name}")
print(f"Weight  : {weight} Kg")
print(f"Height  : {height_m} m")
print(f"BMI     : {BMI:.2f}")
=======
name = input("Enter name: ")
weight = int(input("Enter weight (Kg): "))
height = float(input("Enter height (cms): "))

height_m = height/100
BMI = weight / (height_m ** 2)

if BMI < 18.5:
    category = "Underweight"
elif BMI < 25:
    category = "Normal weight"
elif BMI < 30:
    category = "Overweight"
else:
    category = "Obese"

print()
print(f"Name    : {name}")
print(f"Weight  : {weight} Kg")
print(f"Height  : {height_m} m")
print(f"BMI     : {BMI:.2f}")
>>>>>>> fab3683d8196c1621f5725473890127b19f45853
print(f"Status  : {category}")