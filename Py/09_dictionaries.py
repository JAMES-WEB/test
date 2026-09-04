# student = { 
#     "name": "Alice",
#     "age":20,
#     "grade": "A",
#     "courses": ["Math", "Science", "English"]
# }

# # Iterating through dictionaries 
# for key in student:
#     print(f"{key}: {student[key]}")

# for key, value in student.items():
#     print(f"{key}: {value}")

# # Accessing and modifying
# print(student["name"])
# print(student["age"])
# student["age"] = 21
# student["email"] = "alice@email.com"
# print(student)

# keys = student.keys()
# values = student.values()
# items = student.items()

# print(keys)
# print(values)
# print(items)

# company = { 
#     "employees": {
#         "john": {"age": 30, "department": "IT"},
#         "jane": {"age": 25, "department": "HR"}
#     },
#     "departments": ["IT", "HR", "Finance"]
# }

# print(company["employees"].items())
# print(company["departments"])


# 1. Create a dictionary called student_records with the followign information

student_records = { 
    "student_001":
    {
    "name": "John",
    "age":19,
    "major": "Computer Science",
    "grades": [85, 92, 78]
    },
    "student_002":
    {
    "name": "Sarah",
    "age": 20,
    "major": "Biology",
    "grades": [90, 88, 95]
    }
}


# Add a new student "student_003" with name "Mike",
# age 18, major "Math", grades [82,79,91]

student_records["student_003"] = {
                           "name":"Mike", 
                           "age": 18, 
                           "major": "Math", 
                           "grades": [82,79,91]}



# Update John's age to 20
student_records["student_001"]["age"] = 20
# print(student_records)

# Loop through the dictionary and print each student's 
# information in this format: 
# "Student ID: [id], Name:[name], Major:[major]"
for student_id, student in student_records.items():
    print(f"Student ID: {student_id}, Name: {student['name']}, Major: {student['major']}")
