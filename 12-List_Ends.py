# 12-List_Ends

# Exercise 12 (and Solution)
# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.

# Concepts to practice
## Lists and properties of lists
## List comprehensions (maybe)
## Functions
import random
numbers = [random.randint(1,100) for _ in range(10)]
# numbers = [5, 10, 15, 20, 25]
print numbers
if len(numbers) == 0:
    print("Array is empty!")
elif len(numbers) == 1:
    print([numbers[0]])
else:
    print([numbers[0], numbers[-1]])