num_of_students = int(input())

average_counter = 0
fail_counter = 0
counter_3_4 = 0
counter_4_5 = 0
top_students_counter = 0
for _ in range(num_of_students):
    current_grade_of_student = float(input())
    average_counter += current_grade_of_student
    if 2 <= current_grade_of_student < 3:
        fail_counter += 1
    elif current_grade_of_student < 4:
        counter_3_4 += 1
    elif current_grade_of_student < 5:
        counter_4_5 += 1
    elif current_grade_of_student >= 5:
        top_students_counter += 1

top_students_percentage = top_students_counter / num_of_students * 100
percentage_4_5 = counter_4_5 / num_of_students * 100
percentage_3_4 = counter_3_4 / num_of_students * 100
fail_percentage = fail_counter / num_of_students * 100
average = average_counter / num_of_students

print(f"Top students: {top_students_percentage:.2f}%")
print(f"Between 4.00 and 4.99: {percentage_4_5:.2f}%")
print(f"Between 3.00 and 3.99: {percentage_3_4:.2f}%")
print(f"Fail: {fail_percentage:.2f}%")
print(f"Average: {average:.2f}")
