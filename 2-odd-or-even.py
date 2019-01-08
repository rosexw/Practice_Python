# Exercise 2 (and Solution)
# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

num = int(input("Please enter a number: "))
check = int(input("Please enter a number to divide by: "))

# remainder = num % 2

# if remainder == 1:
#     print(num, " is an odd number")
# elif remainder == 0:
#     print(num, " is an even number")
# else:
#     print(num, " is not even or odd")

# Extras:

# If the number is a multiple of 4, print out a different message.
# number = int(input("Please enter a number: "))
# if num % 4 == 0:
#     print(num, " is a multiple of 4")

# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

answer = num/check

if num % check == 0:
    print(num, " divides evenly by ", check)
    print("the answer is ", answer)
else:
    print(num, " DOES NOT divide evenly by ", check)