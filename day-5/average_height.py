# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
print(f"student_heights: {student_heights}")
counter = 0
height_acc = 0
for height in student_heights:
    height_acc += height
    counter += 1

average_heihgt = round( height_acc / counter)
print(f"Students average height is: {average_heihgt}")
