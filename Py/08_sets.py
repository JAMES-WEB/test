# fruits = {"apple", "banana", "orange"}
# numbers = {1, 2, 3, 4, 5}

# fruits.add("grape")         # Add element
# fruits.remove("banana")     # Remove element
# fruits.discard("kiwi")    # Remove if exists no error

# print (fruits)

# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}

# print(set1.union(set2))
# print(set1.intersection(set2))
# print(set1.difference(set2))




# 1. Create a system that stores student grades as tuples 
# (name, subject, grade) and uses sets to find unique
#  subjects and students. 

grades = [ 
    ("Alice", "Math", 85),  
    ("Bob", "Science", 92),  
    ("Alice", "Science", 78),  
    ("Charlie", "Math", 90),  
    ("Bob", "Math", 88),  
    ("Alice", "English", 95)
    ] 

students = set()
subjects = set()

for name, subject, grade in grades:
    students.add(name)
    subjects.add(subject)

print("Students:", students)
print("Subjects:", subjects)
