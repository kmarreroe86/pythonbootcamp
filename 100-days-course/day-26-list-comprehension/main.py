"""
Instructions
Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.
You are going to create a list called result which contains the numbers that are common in both files.
e.g. if file1.txt contained:
1
2
3
and file2.txt contained:
2
3
4
result = [2, 3]
"""

with open("file1.txt", mode="r") as f1:
    list1 = [int(n.strip()) for n in f1.readlines()]

with open("file2.txt", mode="r") as f2:
    list2 = [int(n.strip()) for n in f2.readlines()]

result = [n for n in list1 if n in list2]

print(list1)
print(list2)
print(result)
