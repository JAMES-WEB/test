# from math_utils import add, multiply, factorial, PI, Calculator

# result = add(5, 3)
# print(f"Addition Result: {result}")

import os
import sys 
import datetime
import random 

# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# # Adjust path for imports to root diretory

now = datetime.datetime.now()
today = datetime.date.today()
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")


print(f"Now date: {now}")
print (f"Today date: {today}")
print(f"Current Date and Time: {formatted_date}")

random_number = random.randint(1, 100)  
random_choice = random.choice(['apple', 'banana', 'cherry'])
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)

print(f"Random Number: {random_number}")
print(f"Random Choice: {random_choice}")
print(f"Shuffled List: {numbers}")

# 1. Find current Python file
current_file = __file__

# 2. Get the full path
full_path = os.path.abspath(current_file)
print(full_path)
# 3. Get current file's folder
current_folder = os.path.dirname(full_path)
print(current_folder)
# 4. Go up one folder
parent_folder = os.path.dirname(current_folder)
print(parent_folder)
# 5. Add that folder to Python's search path
sys.path.append(parent_folder)
print(sys.path.append(parent_folder))