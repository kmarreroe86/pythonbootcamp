#Write your code below this line 👇
import math

def prime_checker(number):
    test_limit = math.ceil(number / 2)
    is_prime = True

    while test_limit > 1 and is_prime:
        if number % test_limit == 0:
            is_prime = False
        test_limit -= 1

    return is_prime



#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
is_prime = prime_checker(number=n)
print(f"Is {n} prime: {is_prime}")