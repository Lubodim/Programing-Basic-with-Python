bye_food = int(input()) * 1000
eaten_food = 0
while True:
    command = input()
    if command == "Adopted":
        break
    command = int(command)
    eaten_food += command
    if eaten_food > bye_food:
        continue
difference = abs(eaten_food - bye_food)
if eaten_food <= bye_food:
    print(f"Food is enough! Leftovers: {difference} grams.")
else:
    print(f"Food is not enough. You need {difference} grams more.")