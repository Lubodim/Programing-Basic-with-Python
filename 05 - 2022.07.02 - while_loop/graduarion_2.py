name = input()
average_grade = 0
bad_grade_counter = 0
class_counter = 0
current_year_grade = 0
while True:
    current_year_grade = float(input())
    average_grade += current_year_grade
    class_counter += 1
    if current_year_grade < 4:
        class_counter -= 1
        bad_grade_counter += 1
        if bad_grade_counter >= 2:
            break

if bad_grade_counter >= 2:
    print(f"{name} has been excluded at {class_counter} grade")
else:
    average_grade /= class_counter
    print(f"{name} graduated. Average grade: {average_grade:.2f}")
