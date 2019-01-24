# Exercise 15 -Reverse Word Order strings
# Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. For example, say I type the string:

aLongString = raw_input("Please enter a long string here: ")

# aLongString = "here I am and there you are"
splitWords = aLongString.split()
splitWords.reverse()
result = " ".join(splitWords)
print(result)



### FROM site or practice:


# s="This is New York"
# # split first
# a=s.split()
# # reverse list
# a.reverse()
# # now join them
# result = " ".join(a)
# # print it
# print(result)

# Example
# My name is Michele
# Then I would see the string:
# Michele is name My
# shown back to me.

# Discussion
# Concepts for this week:

# More string things
# Python has a lot of interesting things you can do with strings. I will show a few here, but you can see many more methods that may or may not be useful at the official Python documentation about the string format.

# Remember that strings are lists.

# Splitting strings
# You can _split_ or tear apart strings based on a given set of characters. For example:

# teststring = "this is a test"
# result = teststring.split("t")
# print(result)
# And at the end, result will contain the list:

  # ['', 'his is a ', 'es', '']
# Instead of _t_, you can write any character you want. If you do not include any character, it means _split on all whitespace_:

#   teststring = _  this      has a lot    of   spaces and    tabs_
#   result = testring.split()
# Then result contains:

#   ['this', 'has', 'a', 'lot', 'of', 'spaces', 'and', 'tabs']
# Joining strings
# You can also relatively easily _join_ or _smush_ strings together:

# listofstrings = ['a', 'b', 'c']
# result = "**".join(listofstrings)
# print result
# Then result will contain the string:

#   a**b**c
# Take a look at the official Python documentation for more information.