import random


# Random int
for n in range(10):
    print(f"Generated for {n}: {random.randint(1, 10)}")    #Random integer 1 - 10 inclusive

# Random float: 0.0.... -> 1 exclusive
random_float = random.random()
print(f"\n Float random: {random_float}")


random_float2 = random.random() * 5 # 0 -> 5 exclusive
print(f"\n Float random: {random_float2}")