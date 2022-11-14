#Write your code below this row 👇


total_sum = 0
for n in range(2, 101):
    total_sum += n if n % 2 == 0 else 0

print(f"Total sum: {total_sum}")

print("Another solution:")
total_sum2 = 0
for n in range(2, 101, 2):
    total_sum2 += n

print(f"Total sum 2: {total_sum2}")