number_students = int(input())
fail_students = 0
students_3_4 = 0
students_4_5 = 0
top_students = 0
average_value = 0

for _ in range(number_students):
    current_value = float(input())
    if current_value < 3:
        fail_students +=1
    elif current_value < 4:
        students_3_4 += 1
    elif current_value < 5:
        students_4_5 += 1
    elif current_value >= 5:
        top_students += 1
    average_value += current_value
average_value /= number_students
percentage_fail_students = fail_students / number_students * 100
percentage_students_3_4 = students_3_4 / number_students * 100
percentage_students_4_5 = students_4_5 / number_students * 100
percentage_top_students = top_students / number_students * 100

print(f"Top students: {percentage_top_students:.2f}%")
print(f"Between 4.00 and 4.99: {percentage_students_4_5:.2f}%")
print(f"Between 3.00 and 3.99: {percentage_students_3_4:.2f}%")
print(f"Fail: {percentage_fail_students:.2f}%")
print(f"Average: {average_value:.2f}")
