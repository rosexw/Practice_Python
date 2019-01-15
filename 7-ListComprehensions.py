# List Comprehensions  
# Exercise 7 (and Solution)
# Let us say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
allEven = [number for number in a if number % 2 == 0]
print(allEven)

# List Comprehension example
# print "append"
# years_of_birth = [1990, 1991, 1990, 1990, 1992, 1991]
# ages = []
# for year in years_of_birth: 
#     ages.append(2014 - year)
# print ages

# # [24, 23, 24, 24, 22, 23]

# print "list comprehension: condense the for loop and the list appending into one simple line. Notice that the for loop just shifted to the end of the list comprehension, and the part before the for keyword is the thing to append to the end of the new list."
# [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
# # [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
# years_of_birth2 = [1990, 1991, 1990, 1990, 1992, 1991]
# ages2 = [2014 - year for year in years_of_birth2]
# print ages2