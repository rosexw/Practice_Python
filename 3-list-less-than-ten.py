# List Less Than Ten  
# list numbers elements if conditional
# Exercise 3 (and Solution)
# Take a list, say for example this one:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.
 
# new_list = []
# for x in a:
#     if x < 5:
#         new_list.append(a[x])

# print(new_list)

# Extras:

# Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
# new_list = []
# for x in a:
#     if x < 5:
#         new_list.append(a[x])

# print(new_list)

# Write this in one line of Python.
# Map
lessThan5 = list(map(lambda x: x<5, a))
print(lessThan5)


# Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.
# new_list = []
# num = int(input("Please enter a number: "))
# for x in a:
#     if x < num:
#         new_list.append(a[x])

# print(new_list)

# Reduce function
# from functools import reduce
# sum = reduce(lambda x, y: x+y, range(1,101))
# print(sum)