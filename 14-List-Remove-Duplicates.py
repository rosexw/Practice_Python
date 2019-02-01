
# Exercise 14 - List Remove Duplicates  
# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

oldList = [1, 2, 3, 4, 5, 5, 6, 6, 7, 7, 7]
# def removeDupes():
#     newList = list(set(oldList))
#     print(newList)
# removeDupes()

# Extras:

# Write two different functions to do this - one using a loop and constructing a list, and another using sets.

# this one uses a for loop
def removeDupes1(oldList):
  newList = []
  for i in oldList:
    if i not in newList:
      newList.append(i)
  return newList

#this one uses sets
def removeDupes2(oldList):
    return list(set(oldList))


print(removeDupes1(oldList))
print(removeDupes2(oldList))

# Go back and do Exercise 5 using sets, and write the solution for that in a different function.
# Discussion

# Concepts for this week:

# Sets
## Set: in mathematics, a collection of elements where no element is repeated. If you know your data is stored in a set, you are guaranteed to have unique elements.
## Features of sets: 
## 1. Sets are not ordered. This means that there is no _first element_ or _last element_. There are just _elements_. You cannot ask a set for it is _next element_.
## 2. There are no repeat elements in sets.
## 3. You can convert between sets and lists very easily.

## In Python, you make and use a set with the set() keyword. For example:

# names = set()
# names.add("Michele")
# names.add("Robin")
# names.add("Michele")
# print(names)

## You can do to a set almost anything you can do to a list (except ask for things like _the third element_). See the Python documentation about sets to get a full list of things you can do to sets.

## You can convert from a list to a set and a set to a list pretty easily:

# names = ["Michele", "Robin", "Sara", "Michele"]
# names = set(names)
# names = list(names)
# print(names)