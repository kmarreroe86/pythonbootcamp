################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")


# Local Scope

def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
# print(potion_strength)


### There is not such thing as block scope, only global and local(functions) ###
### Variables created inside if, or bucle will have global or local(function scope)
game_level = 3

def create_enemy():
    enemies = ["Skeleton", "Zombie", "Alien"]
    if game_level < 5:
        new_enemy = enemies[0]  # new_enemy has local scope, can be call inside the function anywhere

    print(new_enemy)


# Modifying Global Scope
enemies = 1

def increase_enemies():
    # global enemies    tells to the interpreter that this variable is global and its defined outside
    print(f"enemies inside function: {enemies}")
    return enemies + 1

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")



#Global Constants

PI = 3.14159
URL = "https://www.google.com"
TWITTER_HANDLE = "@yu_angela"