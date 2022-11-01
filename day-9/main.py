empty_dictionary = {}

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "Action of doing something over and over.",
}

# Retrieving
print(programming_dictionary["Function"])
print()


# Adding
programming_dictionary["Java"] = "Multi porpouse programming language"
print(programming_dictionary)

# Editing an entry. Edits the value if key is found, add new entry otherwise
programming_dictionary["Java"] = "Multi thread environemtn language"

# Loop through a dictionary. Prints the keys
print("Looping:")
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

# Wipe an existing dictionary. Clear all entries
programming_dictionary = {}


####################################################################################################################################
# Nesting
print("Nesting")
travel_log = {
    "France": {"cities_visited": ["Paris","Lille","Dijon"]},
    "Gernamy": ["Berlin", "Hamburg"],
    "Spain": {"1": "Madrid", 2: "Barcelona", "2": "Sevilla"}
}

print(travel_log)

# Nesting dictionary inside a list
travel_log2 = [
    {
        "country": "France",
        "cities_visited": ["Paris","Lille","Dijon"],
        "total_visits": 12
        },
    {
        "country": "Gernamy",
        "cities_visited": ["Berlin", "Hamburg"],
        "total_visits": 5
    }
]

print(travel_log2)