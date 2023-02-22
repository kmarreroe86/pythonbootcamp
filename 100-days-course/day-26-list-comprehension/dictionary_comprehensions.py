import random

# Ex 1
names = [" Alex", "Beth", "Caroline", "Jane", "Eleanor", "Freddie"]
score_students = {student: random.randint(1, 100) for student in names}
print(f"Students scores: {score_students}")


# Ex 2
passed_students = {student: grade for (student, grade) in score_students.items() if grade >= 60}
print(f"Passed students: {passed_students}")


# Ex 3
print("===============================================================================================================")
""" 
You are going to use Dictionary Comprehension to create a dictionary called result that takes each word in the given
sentence and calculates the number of letters in each word.
"""

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
words = sentence.split()
# print(words)
result = {word: len(word) for word in words}
print(f"result: {result}")


# Ex 4
print("===============================================================================================================")
""" 
You are going to use Dictionary Comprehension to create a dictionary called weather_f that takes each temperature in
degrees Celsius and converts it into degrees Fahrenheit.
To convert temp_c into temp_f:
(temp_c * 9/5) + 32 = temp_f
"""
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}


weather_f = {day: temp_c * 9/5 + 32 for (day, temp_c) in weather_c.items()}
print(f"weather_f: {weather_f}")
























