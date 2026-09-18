# Inheritance 
class Shape: # Parent class 
    def __init__(self, name):
        self.name = name
    
    def area(self):
        return 0
    
class Circle(Shape): # Child inherits from Shape
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self): # Override parent method
        return 3.14 * self.radius * self.radius

class Square(Shape): # Child inherits from Shape
    def __init__(self, side):
        super().__init__("Square")
        self.side = side

    def area(self): # Override parent method
        return self.side * self. side
    
class Rectangle(Shape): # Child inherits from Shape
    def __init__(self, side, side1):
        super().__init__("Rectangle")
        self.side = side
        self.side1 = side1

    def area(self): # Override parent method
        return self.side * self. side1
    
# Both Circle and Square inherit 'name' attribute from Shape
circle = Circle(5)
square = Square(4)
rectangle = Rectangle(4,5)

print(circle.name) # "Circle" (inherited from Shape)
print(square.name) #"Square" (inherited from Shape)
print(rectangle.name)
print(circle.area())
print(square.area())
print(rectangle.area())


# Polymorphism
def print_area(shape): # Takes any Shape
    print(f"{shape.name} area: {shape.area()}")

# Same method call, different behaviors
print_area(circle) # "Circle area: 78.5"
print_area(square) # "Square area: 16"

# Or with a list
shapes = [Circle(3), Square(5), Circle(2)]
for shape in shapes:
    print_area(shape) # Same code, different results
