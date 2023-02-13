import random
from sty import fg


def generateRGB():
    red = random.randint(0, 256)
    blue = random.randint(0, 256)
    green = random.randint(0, 256)

    # returning a tuple
    return red, green, blue


def generate_color(red, green, blue):
    return fg(red, green, blue)


red, green, blue = generateRGB()
color = generate_color(red, green, blue)
print(color, "Randomly changing color")
