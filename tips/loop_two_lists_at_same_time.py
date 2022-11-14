a = [1, 2, 3, 4]
b = ["one", "two", "three"]

for item1, item2 in zip(a, b):
    print(item1, item2)

"""
Output:
1 one
2 two
3 three

-4 is left out
"""