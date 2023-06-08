# Exceptions:
# try: => Code that might cause an exception
# except: => Code executed if there was an exception
# else: => Code executed if were no exceptions
# finally:=> Code executed no matter what happens

# Breaks the program
# with open("a_file.txt") as file:
#     file.read()

try:
    file = open("a_file.txt")

    # a_dictionary = {"key": "value"}
    # print(a_dictionary["abc"])
except FileNotFoundError:
    # print("There was an error open the file")
    file = open("a_file.txt", "w")
    file.write("dummy")
except KeyError as error_message:
    print(f"That key {error_message} doesn't not exists")
else:
    # Has context of variables in the try block. Only get executed if no exceptions are thrown
    content = file.read()
    print(content)
finally:
    file.close()
    print("File closed")

height = float(input("Height(m):"))
weight = float(input("Weight(kg):"))
if height > 3:
    raise ValueError("Human height should not be over 3 meters")

bmi = weight / height ** 2
print(bmi)
