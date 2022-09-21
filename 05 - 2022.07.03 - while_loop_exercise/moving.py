width = int(input())
length = int(input())
height = int(input())

free_volume = width * length * height
boxes_counter = 0
while boxes_counter < free_volume:
    command = input()
    if command == "Done":
        break
    else:
        command = int(command)
        boxes_counter += command
difference = abs(boxes_counter - free_volume)
if boxes_counter > free_volume:
    print(f"No more free space! You need {difference} Cubic meters more.")
else:
    print(f"{difference} Cubic meters left.")
