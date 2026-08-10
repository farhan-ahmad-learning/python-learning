def fib(n):
    if n < 0:
        return "Enter positive integer."
    
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a
    
n = int(input("Enter number:"))    
print(fib(n))
