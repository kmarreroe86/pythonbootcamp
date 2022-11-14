""" Unpacking a list( or similar to deconstruct in javascript)"""

names = [ "John", "Mary", "Lisa", "Rose"]

boy, *girls = names
print(boy)
print(girls)

names2 = ["Mary", "Lisa", "Rose", "John"]

*girls2, boy2 = names2
print(boy2)
print(girls2)

"""
Output:
John
['Mary', 'Lisa', 'Rose']
"""