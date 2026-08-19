# A decorator wraps a function to add behaviour

def timer(func):
    """Measures how long a function takes."""
    import time
    def wrapper(*args, **kwargs):
        start   = time.time()
        result  = func(*args, **kwargs)
        end     = time.time()
        print(f"{func.__name__} took {end-start:.4f} seconds")
        return result
    return wrapper    
@timer
def calculate(n):
    return sum(range(n))

calculate(1000000)      # prints time taken automatically