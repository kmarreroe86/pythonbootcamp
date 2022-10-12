import random


# Random int
for n in range(10):
    # Random integer 1 - 10 inclusive
    print(f"Generated for {n}: {random.randint(1, 10)}")

# Random float: 0.0.... -> 1 exclusive
random_float = random.random()
print(f"\n Float random: {random_float}")


random_float2 = random.random() * 5  # 0 -> 5 exclusive
print(f"\n Float random: {random_float2}")


# ######################################################################################################################################################################
# Lists
print("============== Lists ============== \n")
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia",
                     "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
                     "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon",
                     "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming",
                     "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america)    # Print all list
print(states_of_america[2])  # Print 3th element
print(states_of_america[-1])  # Prints Hawaii

states_of_america[2] = "new_jersey" # Overwrites the 3th element
states_of_america.append("Wonderland") # Add to end of the list
print(states_of_america)


print("===================== Nested lists ======================")
# dirty_dozen = ["Strawberries","Spinach","Kale","Nectarines","Apples","Grapes","Peaches","Cherries","Pears","Tomatoes","Celery","Potatoes"];
fruits = ["Strawberries","Nectarines","Apples","Grapes","Peaches","Cherries","Pears"];
vegetables = ["Spinach","Kale","Tomatoes","Celery","Potatoes"];

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)