name_of_actor = input()
academy_points = float(input())
number_of_evaluators = int(input())

total_points = academy_points

for _ in range(number_of_evaluators):
    current_name_of_evaluators = input()
    current_points = float(input())
    final_points = len(current_name_of_evaluators) * current_points / 2
    total_points += final_points
    if total_points > 1250.5:
        break
if total_points > 1250.5:
    print(f"Congratulations, {name_of_actor} got a nominee for leading role with {total_points:.1f}!")
else:
    difference = 1250.5 - total_points
    print(f"Sorry, {name_of_actor} you need {difference:.1f} more!")