names = ["Bob", "Gandalf", "Batman"]
professions = ["programmer", "wizard", "superhero"]

# using for loop zip
dict_zip = {}
for (key, value) in zip(names, professions):
    dict_zip[key] = value

print(f"Dict with for-zip: {dict_zip}")

dict_zip_better = {key: value for (key, value) in zip(names, professions)}
print(f"Dict with for-zip comprehension: {dict_zip_better}")
#########################################################
print("#########################################################")

dict_for = {}
for idx in range(len(names)):
    dict_for[names[idx]] = professions[idx]

print(f"Dict with for: {dict_for}")

dict_for_better = {names[0][i]: professions[0][i] for i in range(len(names))}
print(f"Dict with for comprehension: {dict_for_better}")

#########################################################
print("#########################################################")
#Modifiying dictionary in place
my_dic = {
    "Spider": "photographer",
    "Bat": "philantropist",
    "Wonder Wo": "nurse"
}

my_dic = {key + "man": value for (key, value) in my_dic.items()}
print(my_dic)

my_dic2 = {
    "Spider": "photographer",
    "Bat": "philantropist",
    "Wonder Wo": "nurse"
}

my_dic2 = {(key + "man" if key != "Spider" else "Superman"):
           (value if value != "photographer" else "journalist")
           for (key, value) in my_dic2.items()}
print(f"my_dic2: {my_dic2}")

#########################################################
# Dictionary of lists
print("#########################################################")
import random

bases = ["A", "C", "T", "G"]
strand1 = random.choices(bases, k=10)
print(f"strand1: {strand1}")

dna = {
    key: [
        value, "T" if value == "A" else
        "A" if value == "T" else "C" if value == "G" else "G"
    ]
    for (key, value) in enumerate(strand1)
}
print(f"dna: {dna}")

#########################################################
# List of dictionaries
import string

print("#########################################################")
print(f"string.printable: {string.printable}")
keys = ["id", "username", "password"]
devs = ["unclebob", "ericgamma"]

data = [{
    key: (i if key == "id" else devs[i] if key == "username" else "".join(random.choices(string.printable, k = 8))) for key in keys
} for i in range(len(devs))]

print(f"data: {data}")