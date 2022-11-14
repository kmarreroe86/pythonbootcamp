# For loops with lists

fruits = ["apple", "peach", "pear"]

for fruit in fruits:
    print(fruit)
    print(fruit + " pie")

print(fruits)


print(len("qwerty"))
print(sum([1,2,3]))

# range function
for number in range(0, 10):     # 0 included, 10 excluded, step 1 by default
    print(f"number: {number}")

print("Step 2")
for number in range(0, 10, 2):     # 0 included, 10 excluded, step 2
    print(f"number: {number}")

summa = sum(range(1, 101))
print(f"Sum range(1, 101) = {summa}")