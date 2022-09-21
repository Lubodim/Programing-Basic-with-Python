unsatisfactory_evaluation = int(input())
average_grade = 0
total_solved_problems = 0
last_problem = ""
bad_grades_counter = 0
is_expelled = False

current_task = input()
while current_task != "Enough":
    current_grade = int(input())
    total_solved_problems += 1
    last_problem = current_task
    average_grade += current_grade
    if current_grade <= 4:
        bad_grades_counter += 1
        if bad_grades_counter == unsatisfactory_evaluation:
            is_expelled = True
            break
    current_task = input()
average_grade = average_grade / total_solved_problems
if is_expelled:
    print(f"You need a break, {unsatisfactory_evaluation} poor grades.")
else:
    print(f"Average score: {average_grade:.2f}")
    print(f"Number of problems: {total_solved_problems}")
    print(f"Last problem: {last_problem}")
