# # Functions with parameters
# def greet_person(name):
#     print(f"Hello, {name}!")

# greet_person("Alice")

# # Functions with return values
# def add_numbers(a, b):
#    return a + b

# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))

# result = add_numbers(a, b)

# # result = add_numbers(5,3)
# print(result) #8

# # Default parameters
# def greet_with_title(name, title="Mr."):
#     return f"Hello, {title} {name}!"

# print(greet_with_title("Smith"))
# print(greet_with_title("Johnson", "Dr."))


# # *args - variable number of arguments 
# def sum_all(*args):
#     return sum(args)

# print(sum_all(1,2,3,4,5))

# # **kwargs - keyword arguments 
# def print_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# print_info(name = " Alice", age = 25, city="New York")

# # Combining *args and **kwargs
# def flexible_function(*args, **kwargs):
#     print("Positional  arguments:", args)
#     print("Keyword arguments:", kwargs)

# flexible_function( 1,2,34,5, name = "Alice", age = 25, city = "Kuala Lumpur")

# # Lambda functison (anonymous funcitons)
# square = lambda x: x **2
# print(square(5)) # 25

# add = lambda x,y: x + y
# print(add(3, 4)) # 7



# # 1. Write a function that checks if a number is prime.
# def prime_number(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
# num = int(input("Enter Prime Number: "))
# x = prime_number(num)
# print(x)  # True



# # 2. Build a tempertuer converter function. (Celsisu to Fahrenheit)
# def celsius_to_fahrenheit(celsius):
#     return (celsius * 9/5) + 32

# celsius = float(input("Enter temperature in Celsius: "))

# result = celsius_to_fahrenheit(celsius)

# print(f"Temperature in Fahrenheit: {result}")



# def sum_all(*args):
#     print("Arguments received:", args[1])
#     return sum(args)

# print(sum_all(1, 2, 3, 4, 5))



def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


# Test the functions
print(f"25°C = {celsius_to_fahrenheit(25)}°F")
print(f"77°F = {fahrenheit_to_celsius(77)}°C")


# More complete converter with user input
def temperature_converter():
    temp = float(input("Enter temperature: "))
    unit = input("Enter unit (C for Celsius, F for Fahrenheit): ").upper()

    if unit == "C":
        result = celsius_to_fahrenheit(temp)
        print(f"{temp}°C = {result}°F")

    elif unit == "F":
        result = fahrenheit_to_celsius(temp)
        print(f"{temp}°F = {result}°C")

    else:
        print("Invalid unit!")


# Run the converter
temperature_converter()