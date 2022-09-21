

steps_counter = 0
target_steps = 10000

while steps_counter < target_steps:
    steps = input()
    if steps == "Going home":
        steps = int(input())
        steps_counter += steps
        break
    steps = int(steps)
    steps_counter += steps
difference = abs(steps_counter - target_steps)
if steps_counter >= target_steps:
    print("Goal reached! Good job!")
    print(f"{difference} steps over the goal!")
else:
    print(f"{difference} more steps to reach goal.")
