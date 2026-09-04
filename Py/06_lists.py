fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]
mixed = ["hello", 42, 3.14, True]
empty_list = []

# # Accessing Elements
# print(fruits[0])
# print(fruits[-1])
# print(numbers[1:4])
# print(numbers[:3])
# print(numbers[2:])

# fruits.append("grape")      # ["apple", "banana", "orange", "grape"]
# fruits.insert(1, "kiwi")    # ["apple", "kiwi", "banana", "orange", "grape"]
# fruits.remove("banana")     # ["apple", "kiwi", "orange", "grape"]
# popped = fruits.pop()       # grape >> ["apple", "kiwi", "orange"]
# fruits.sort()               # No change
# fruits.reverse()            # ["orange", "kiwi", "apple"]

# List operations
# len(fruits)                  # 3
# print("apple" in fruits )    # TRUE
# print(fruits + ["mango"])    # ["orange", "kiwi", "apple", "mango"]
# print(fruits * 2)            # Repetition

# print(len(fruits))
# print(fruits)
# print(popped)

# 1. Create a grocery list and perform various operations. 
# grocery = ["accessories", "fruits", "meat"]

# # Accessing Elements
# print(grocery[0])
# print(grocery[-1])
# print(grocery[1:4])
# print(grocery[:3])
# print(grocery[2:])

# grocery.append("tool")      # ["apple", "banana", "orange", "grape"]
# grocery.insert(1, "dessert")    # ["apple", "kiwi", "banana", "orange", "grape"]
# grocery.remove("fruits")     # ["apple", "kiwi", "orange", "grape"]
# popped = grocery.pop()       # grape >> ["apple", "kiwi", "orange"]
# grocery.sort()               # No change
# grocery.reverse()            # ["orange", "kiwi", "apple"]

# # List operations
# len(grocery)                  # 3
# print("meat" in grocery )    # TRUE
# print(grocery + ["shirt"])    # ["orange", "kiwi", "apple", "mango"]
# print(grocery * 2)            # Repetition

# print(len(grocery))
# print(grocery)
# print(popped)


# 2. Write a program that 
# finds the largest and smallest number in list.

numbers = [1, 3, 5, 7, 9, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]

largest = numbers[0]
smallest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

    if number < smallest:
        smallest = number

print("Largest:", largest)
print("Smallest:", smallest)
print("Largest:", max(numbers))
print("Smallest:", min(numbers))

# number = 1

# 1 > largest(1) ? No
# largest stays 1

# 1 < smallest(1) ? No
# smallest stays 1


# number = 3

# 3 > largest(1) ? Yes
# replace 1 with 3

# largest = 3

# 3 < smallest(1) ? No
# smallest stays 1