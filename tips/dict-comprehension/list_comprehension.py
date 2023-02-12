fruits = ["apples", "bananas", "strawberries"]
uppercase_fruits = []

for fruit in fruits:
    uppercase_fruits.append(fruit.upper())

print(uppercase_fruits)

##############################################################################
uppercase_fruits_better = [fruit.upper() for fruit in fruits]
print(f"uppercase_fruits_better: {uppercase_fruits_better}")

##############################################################################
bits = [
    True, False, True, True, True, False, False, False, False, True, False,
    True, False, True, False, True
]

number_bits = [1 if b else 0 for b in bits]
print(f"bits: {bits}")
print(f"number_bits: {number_bits}")

##############################################################################
a_string = "HelloMyNameIsBob"

modified_string = "".join([
    s if s.islower() else " " + s.lower() if s in ["I", "N"] else " " + s
    for s in a_string])[1:] # keeps all characters from 1 until the end (spare index 0)
print(f"modified_string: {modified_string}")