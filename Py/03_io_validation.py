# name = input("Enter your name: ")
# height = float(input("Enter your height: "))

# #Input Validation
# while True:
#     try: 
#         age = int(input("Enter your age: "))
#         if age > 0:
#             break
#         else:
#             print("Age must be positive!")
#     except ValueError:
#         print("Please enter a valid number!")

# #Output validation
# print(f"Hello,{name}!")
# print(f"You are {age} years old and {height} feet tall.")





# #Input Validation
# while True:
#     try: 
#         X = int(input("Enter a number for X: "))
#         if X > 0:
#             break
#         else:
#             print("X must be positive!")
#     except ValueError:
#         print("Please enter a valid number!")

# while True:
#     try: 
#         Y = int(input("Enter a number for Y: "))
#         if Y > 0:
#             break
#         else:
#             print("Y must be positive!")
#     except ValueError:
#         print("Please enter a valid number!")

# Z = X + Y

# #Output validation
# print(f"Your answer is {Z}.")



while True:
    # Input Validation
    score = 0
     
    # Question 1 - I/O Manipulation
    while True:
        try: 
            X = int(input("Question 1: What is the square of 2? "))
            if X == 4:
                print("Congratulations! Your answer is correct.")
                score += 1
                break
            else:
                print("Your answer is wrong.")
                break
        except ValueError:
            print("Please enter a valid number!")



    # Question 2 - String Manipulation
    X = input("Question 2: What is the result of 'Hello'.upper()? ")
    if X == "HELLO":
            print("Congratulations! Your answer is correct.")
            score += 1
    else:
            print("Your answer is wrong.")

    # Question 3 - Data Type

    X = input("Question 3: What data type is 10.5? ")
    if X.lower() == "float":
            print("Congratulations! Your answer is correct.")
            score += 1
    else:
            print("Your answer is wrong.")


    # Output Validation

    print("\n===== QUIZ RESULT =====")
    print(f"You got {score} out of 3 questions correct.")

    if score == 3:
        print("Excellent! You answered all questions correctly.")
        break
    elif score >= 2:
        print("Good job! You answered most questions correctly.")
        break
    elif score == 1:
        print("You got 1 question correct. Keep practicing!")
        break
    elif score == 0:
        print("You got 0 questions correct. Please try again!")
        print(f"Your score is {score} out of 3 questions correct.")
        print("Restarting the quiz...\n")
        continue
