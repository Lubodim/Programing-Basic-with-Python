from math import ceil

height = int(input())
width = int(input())
area = height * width * 4
percentage_not_painting = int(input())
percentage_painting_area = area - area * percentage_not_painting / 100
percentage_painting_area = ceil(percentage_painting_area)
paint_counter = 0
command = input()
while command != "Tired!":
    command = int(command)
    paint_counter += command
    if paint_counter >= percentage_painting_area:
        break
    command = input()
difference = abs(paint_counter - percentage_painting_area)
if command == "Tired!":
    print(f"{difference} quadratic m left." )
if paint_counter > percentage_painting_area:
    print(f"All walls are painted and you have {difference} l paint left!")
if paint_counter == percentage_painting_area:
    print("All walls are painted! Great job, Pesho!")