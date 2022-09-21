name = input()
average_grade = 0
bad_grade_counter = 0
class_counter = 0
for _ in range(1, 12 + 1):
    current_grade = float(input())
    average_grade += current_grade
    if current_grade < 4:
        bad_grade_counter += 1
        if bad_grade_counter == 2:
            break
    class_counter += 1
average_grade /= class_counter
if class_counter == 12:
    print(f"{name} graduated. Average grade: {average_grade:.2f}")
else:
    print(f"{name} has been excluded at {class_counter} grade")
