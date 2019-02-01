# 10: List Overlap Comprehensions
# The exercise for this week is going to be revisiting an old exercise (see Exercise 5), except require the solution in a different way.

import random
# Take two lists, say for example these two:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# a = [random.randint(1,100) for _ in range(10)]
# print a
# b = [random.randint(1,100) for _ in range(10)]
# print b

# # list comprehension in one line!
# thesame = [item for item in a if item in b]
# print thesame

import random
# a = random.sample(range(1,30), 12)
# b = random.sample(range(1,30), 16)
result_overlaps = [i for i in set(a) if i in b]
result = [i for i in result_overlaps if result_overlaps.count(i) == 1]
print(a, b)
print(result)
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes. Write this in one line of Python using at least one list comprehension. (Hint: Remember list comprehensions from Exercise 7).

# The original formulation of this exercise said to write the solution using one line of Python, but a few readers pointed out that this was impossible to do without using sets that I had not yet discussed on the blog, so you can either choose to use the original directive and read about the set command in Python 3.3, or try to implement this on your own and use at least one list comprehension in the solution.

# Extra:

# Randomly generate two lists to test this


# x = [1, 2, 3]
# y = [5, 10, 15]
# allproducts = [a*b for a in x for b in y]

# print allproducts
# [5, 10, 15, 10, 20, 30, 15, 30, 45]