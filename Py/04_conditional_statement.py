# age = 18

# if age >= 18:
#     print("You are an adult.")
# else:
#     print("You are a minor.")



# score = 85

# if score >= 90:
#     grade = "A"
# elif score >= 80:
#     grade = "B"
# elif score >= 70:
#     grade = "C"
# elif score >= 60:
#     grade = "D"
# else:
#     grade = "F"

# print(f"Yourgrade is: {grade}")


# user_age = 25
# has_license = True

# if user_age >= 18 and has_license:
#     print("You are allowed to drive.")
# else:
#     print("You are not allowed to drive.")

# day = "Saturday"

# if day == "Saturday" or day == "Sunday":
#     print("It's the weekend!")
# else:
#     print("It's a weelday.")


# weather = "sunny"
# temperature = 75

# if weather == "sunny":
#     if temperature > 70:
#         print("It's sunny and warm.")
#     else:
#         print("It's sunny but cool.")



# 1.Write  a  program  that  categorizes  BMI  (Body  Mass  Index)  
# into underweight(<18.5),  normal  weight(18.5-24.9),  
# overweight(25-29.9),  and  obese(30  or  more).  
# The  program  should  take  the  user's weight (in kilograms) 
# and height (in meters) as input, 
# calculate the BMI, and print the corresponding category.

Weight = float(input("Enter your weight in kilograms (kg): "))
Height = float(input("Enter your height in meters (m): "))

BMI = Weight / (Height ** 2) # kg/m^2

if(BMI < 18.5):
    print("You are underweight.")
elif(BMI >= 18.5 and BMI <= 24.9):
    print("You have a normal weight.")
elif(BMI >= 25 and BMI <= 29.9):
    print("You are overweight.")
else:
   print("You are obese.")