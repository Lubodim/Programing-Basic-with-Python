width = int(input())
lenght = int(input())
cake_volume = width * lenght
pices_counter = 0
while cake_volume > 0:
    command = input()
    if command == "STOP":
        break
    else:
        command = int(command)
    pices_counter += command
    if pices_counter > cake_volume:
        break
difference = abs(cake_volume - pices_counter)
if pices_counter > cake_volume:
    print(f"No more cake left! You need {difference} pieces more.")
else:
    print(f"{difference} pieces are left.")
