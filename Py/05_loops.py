# for i in range (5):
#     print(i)

# for i in range (1,6):
#     print(i)

# for i in range(0, 10, 2):
#     print(i)

# count = 0
# while count < 5:
#     print(count)
#     count += 1

# for i in range(10):
#     if i == 3:
#         continue    # Skip this iteration
#     if i == 7:
#         break   # Exit the loop
#         # continue
#     print(i)

# for i in range(2):
#     for j in range(3):
#         print(f"({i},{j})")

# # 1. Create a multiplicaiton table generator.
# number = int(input("Enter a number: "))
# for i in range(1,13):
#     print(f"{number}*{i} = {number * i}")

#2. Write a program that finds all prime numbers 
# up to a given number. (limit = 20)

limit = 20
for number in range (2, limit + 1):
    is_prime = True
    for i in range(2,number):
        if number%i == 0:
            is_prime = False
            break
    if is_prime:
        print(number)

# i = 0
# for i in range (1,3):
#     print(i)

# x= 2%2
# print(x)