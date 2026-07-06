print(f"===================================")
print(f"      PYTHON CALCULATOR v1.0       ")
print(f"===================================")

count = 0 
while True:
    print()
    num1 = float(input("Enter first number   : "))
    num2 = float(input("Enter second number  : "))
    operation = input("Choose operation (+, -, *, /, //, %, **)")
    result = None

    if operation == "+":
        result = num1 + num2
        
    elif operation == "-":
        result = num1 - num2
        
    elif operation == "*":
        result = num1 * num2
        
    elif operation == "/":
        if num2 == 0:
            print(f"\n Error: Cannot divide by zero!")
        else:
            result = num1 / num2
        
    elif operation == "//":
        if num2 == 0:
            print("\n Error: Cannot divide by zero!")
        else:
            result = num1 // num2
        
    elif operation == "%":
        result = num1 % num2
        
    elif operation == "**":
        result = num1 ** num2
        
    else:
        print(f"\n Error: Invalid operation!")
        print("  Valid operations: +  -  *  /  //  %  **")
    
    if result is not None:
        print(f"n\ {num1} {operation} {num2} = {result}")
        count += 1
    
    print()
    again = input("Calculate again? (yes/no)?: ").lower().strip()
    if again == "no":
        break
print()

print("===================================")
print(f"  Total calculations: {count}")
print("  Thank you for using Calculator!")
print("===================================")