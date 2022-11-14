
def my_function(num1, num2):
    result = num1 * num2
    return result

multiply = my_function(2, 3)
print(f"Result is {multiply}")


def format_name(first_name, last_name):
    capitlize_first_name = first_name.capitalize()
    capitalized_last_name = last_name.capitalize()

    return f"{capitlize_first_name}, {capitalized_last_name}"


print(format_name("karel", "marrero"))