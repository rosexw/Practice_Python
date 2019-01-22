# Check Primality Functions   
# Exercise 11 (and Solution)
# Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors). You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions, described below.

def get_integer(help_text="Please enter a number: "):
    return int(input(help_text))

prime = False
number = get_integer()
is_prime = [x for x in range(2, number) if number % x == 0]
print(is_prime)
if len(is_prime) > 0:
    print(str(number) + " is not a prime number")
else:
    print(str(number) + " is a prime number")

# Functions: A function wraps a piece of code that we want to reuse, labels it, and allows us to use it again relatively easily
# Reusable functions: add variables to the functions to make your code even MORE reusable
# get_integer is reused below in age and school_year
# Default arguments: I want there to be a _default_ behavior for my function that happens when I create an argument for it but do not give it any.
# The first time I call the function, it will print "Tell me your age: ", but the second time, it will print "Give me a number: ", because I did not give it a string and it will execute the default behavior.

# def get_integer(help_text="What grade are you in?: "):
#     return int(input(help_text))

# age = get_integer("Tell me your age: ")
# school_year = get_integer()
# if age > 15:
#     print("You are over the age of 15 in grade " + str(school_year))
# else:
#     print("You are 15 or under in grade " + str(school_year))