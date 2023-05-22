students_height = input("Please enter students height ").split()
# student_height_list = int(student_height)


for i in range(len(students_height)):
    students_height[i] = int(students_height[i])

# ave_height = int(sum(student_height_list) / len(student_height_list))
print(students_height)

height_of_student = 0

for height in students_height:
    height_of_student = height_of_student + height

number_of_students = 0

for students in students_height:
    number_of_students += 1

print(height_of_student / number_of_students)


# print('Average height of students is: ', ave_height)


