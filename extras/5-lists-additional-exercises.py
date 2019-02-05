# -------
# CHECKING FOR STUDENT IN A LIST
# list_of_students = ["Michele", "Sara", "Cassie"]
# students = map(str.lower,list_of_students)
# name = raw_input("Type name to check: ")

# if name.lower() in students:
#     print(name + " is enrolled.")
# else:
#     print(name + " is not enrolled.")


# FILTER FUNCTION
# number_list = range(-5, 5)
# less_than_zero = list(filter(lambda x: x < 0, number_list))
# print less_than_zero
# Output: [-5, -4, -3, -2, -1]

# https://stackoverflow.com/questions/4641765/add-to-integers-in-a-list
# APPENDING ITEMS TO AN ARRAY:
# fooList = [1,3,348,2]
# fooList.append(3)
# fooList.append(2734)
# print(fooList)

# INSERTING ITEMS TO AN ARRAY:
# x = [2, 5, 10]
# x.insert(2, 77)
# print(x) 

# EXTEND AN ARRAY: list2.extend(list1)
# a = range(5)
# print "a = range(5)"
# print a
# b = range(3)
# print "b = range(3)"
# print b
# c = range(2)
# print "c = range(2)"
# print c
# d = b.append(a)
# print "d = b.append(a)"
# print d
# c.extend(a)
# print "c.extend(a)"
# print c

# >>> a = range(5)
# >>> b = range(3)
# >>> c = range(2)
# >>> b.append(a)
# >>> b
# [0, 1, 2, [0, 1, 2, 3, 4]]
# >>> c.extend(a)
# >>> c
# [0, 1, 0, 1, 2, 3, 4]