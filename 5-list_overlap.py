# Exercise 5: List Overlap  https://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html
# Take two lists, say for example these two:

import random

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

# list1 = []
# for bvalue in b:
#     if bvalue in a and bvalue not in list1:
#         list1.append(bvalue)
# print list1

# Extras:
# 1. Randomly generate two lists to test this

a = [random.randint(1,100) for _ in range(10)]
b = [random.randint(1,100) for _ in range(10)]

list1 = []
for bvalue in b:
    if bvalue in a and bvalue not in list1:
        list1.append(bvalue)
print (list1 if len(list1)>0 else "There are no numbers alike in these two arrays")



# 2. Write this in one line of Python (do not worry if you cannot figure this out at this point - we will get to it soon)
# filter() function

# first = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# second = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# # first = [random.randint(1,100) for _ in range(10)]
# print first
# # second = [random.randint(1,100) for _ in range(10)]
# print second

# def diff(first, second):
#         second = set(second)
#         return [item for item in first if item in second]

# print diff(first, second)