# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


# Write your code below this row 👇
amount = 0
sum_heights = 0
for height in student_heights:
    sum_heights += int(height)
    amount += 1

avarage_height = sum_heights / amount
print(round(avarage_height))
