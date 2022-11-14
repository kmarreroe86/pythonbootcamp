""" Permutations of a String """

from itertools import permutations

def get_permutations(s: str):
    arr = []
    for i in permutations(s):
        arr.append("".join(i))
    
    return arr


print(get_permutations("ABC"))


# Another way
s = 'ABC'
s = permutations(set(s))
print(type(s))

for c in list(s):
    print(c)

