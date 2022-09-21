budget = float(input())
command = input()

while command != "ACTION":
    if len(command) > 15:
        current_actor_salary = budget * 0.2
    else:
        current_actor_salary = float(input())
    budget -= current_actor_salary
    if budget < 0:
        break
    command = input()

if budget >= 0:
    print(f"We are left with {abs(budget):.2f} leva.")
else:
    print(f"We need {abs(budget):.2f} leva for our actors.")