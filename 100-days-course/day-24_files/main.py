# Open file
# file = open("my_file.txt")
# content = file.read()
# print(content)
#
# file.close()


# Another way to open file. Manage to closing the file after finish using it
# mode= "r" (default mode) -> read || "w" -> write || "a" -> append
# with open("my_file.txt", mode="r") as file:
    # content = file.read()
    # print(content)


with open("my_file.txt", mode="a") as file:
    file.write("\nNew text!")


# Create a file that didn't exist
with open("new_file.txt", mode="w") as file:
    file.write("New content for new file")
