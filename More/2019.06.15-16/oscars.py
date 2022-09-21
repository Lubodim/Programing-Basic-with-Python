actor_name = input()
points_from_academy = float(input())
jury_number = int(input())
total_points = points_from_academy
for _ in range(jury_number):
    current_jury_name = input()
    current_jury_points = float(input())
    points_for_actor = len(current_jury_name) * current_jury_points / 2
    total_points += points_for_actor
    if total_points > 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
        break
else:
    print(f"Sorry, {actor_name} you need {1250.5 - total_points:.1f} more!")
