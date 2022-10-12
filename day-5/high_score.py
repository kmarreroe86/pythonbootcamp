# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split(",")
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
min = min(student_scores)
max = max(student_scores)
print(f"easy min: {min}" )
print(f"easy max: {max}")

print("=============================")
import sys
high_score = -sys.maxsize - 1
for score in student_scores:
    # if high_score < score:
        # high_score = score
    high_score = score if high_score < score else high_score    

print(f"The highest score in the class is: {high_score}")