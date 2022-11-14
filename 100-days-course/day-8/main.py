def greet():
    print("Hello John")
    print("How do you do?")
    print("Isn't the weather nice today?")

greet()


def great_with_name(name):
    print(f"Hello {name}")
    print("How do you do?")
    print("Isn't the weather nice today?")

great_with_name("Jane")


def great_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

great_with("Jack", "Nowhere")
great_with(location = "Nowhere", name = "Jack")