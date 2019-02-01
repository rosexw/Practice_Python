# String Lists  
# strings lists index
# Exercise 6 (and Solution)
# Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

word = str(input("Please enter the word you would like to test if a palindrome: "))

# Negative values also work to make a copy of the same list in reverse order:
# >>> L[::-1]

rvs=word[::-1]
print("Reverse of word is: " + rvs)
if word == rvs:
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")


# # Slicing a word by even numbers:
# L = range(10)
# print L[::2]

# # by factors of three
# L = range(10)
# print L[::3]

# https://docs.python.org/2.3/whatsnew/section-slices.html