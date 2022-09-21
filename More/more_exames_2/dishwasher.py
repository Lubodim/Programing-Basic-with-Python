detergent = int(input())
detergent *= 750
command = input()
detergent_counter = 0
plate_counter = 0
pot_counter = 0
command_counter = 0
while command != "End":
    command = int(command)
    command_counter += 1
    if command_counter % 3 == 0:
        detergent_counter += command * 15
        pot_counter += command
    else:
        detergent_counter += command * 5
        plate_counter += command
    if detergent_counter > detergent:
        break
    command = input()
difference = abs(detergent - detergent_counter)
if detergent > detergent_counter:
    print("Detergent was enough!")
    print(f"{plate_counter} dishes and {pot_counter} pots were washed.")
    print(f"Leftover detergent {difference} ml.")
else:
    print(f"Not enough detergent, {difference} ml. more necessary!")
