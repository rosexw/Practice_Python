
# https://stackoverflow.com/questions/17718271/python-count-for-multidimensional-arrays-list-of-lists

list = [['foobar', 'a', 'b'], ['x', 'c'], ['y', 'd', 'e', 'foobar'], ['z', 'f','foobar']]
print(sum(x.count('foobar') for x in list))
