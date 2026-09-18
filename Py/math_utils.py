def add(a, b):
    """Return the sum of a and b."""
    return a + b
def multiply(a, b):
    """Return the product of a and b."""
    return a * b
def factorial(n):
    """Return the factorial of n."""
    if n < 1:
        return 1
    return n * factorial(n - 1)

PI = 3.14159

class Calculator: 
    def __init__(self):
        self.history = []

    def calculate(self, operation, a, b):
        if operation == 'add':
            result = add(a, b)
        elif operation == 'multiply':
            result = multiply(a, b)
        else:
            result = None
            raise ValueError("Unsupported operation")
        
        self.history.append(f"{operation}({a}, {b}) = {result}")
        return result