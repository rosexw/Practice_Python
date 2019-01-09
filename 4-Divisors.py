# Divisors  
# Exercise 4 and Solution
# Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
# If you do not know what a divisor is, it is a number that divides evenly into another number. 
# For example, 13 is a divisor of 26 because 26 modulo 13 has no remainder.
num = int(input("Please enter a number to divide: "))
listRange = list(range(1, num+1))

divisor_list = []

for divisor in listRange:
    if num % divisor == 0:
        divisor_list.append(divisor)

print(divisor_list)