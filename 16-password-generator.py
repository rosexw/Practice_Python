# Password Generator    
# Exercise 16 (and Solution)
# Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.

import random
import string
# import pyperclip

# length = int(raw_input("How many characters would you like your password to be? "))

# randomChars = string.ascii_letters + string.digits + string.punctuation
# password = ''.join(random.choice(randomChars) for char in range(length))
# print(password)

# print('Your unique password has been copied to clipboard.')
# pyperclip.copy(password)

# Extra:
# Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.

def createAPassword(chosenLength):
    randomChars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(randomChars) for char in range(chosenLength))
    print(password)

passwordStrength = input("How strong would you like your password to be? Pick weak, medium, strong: ")

foo = ["apple", "carrot", "orange", "pineapple", "mango"]
if passwordStrength == "weak":
    print(random.choice(foo))

elif passwordStrength == "medium":
    createAPassword(10)

elif passwordStrength == "strong":
    createAPassword(20)
else:
    print("Invalid input. Please try again")