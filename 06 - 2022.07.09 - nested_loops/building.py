num_flats = int(input())
num_rooms = int(input())
type_room = ""
room_number = 0
for n1 in range(num_flats, 0, -1):
    for n2 in range(num_rooms):
        room_number = n1 * 10 + n2
        if n1 == num_flats:
            type_room = "L"
        elif n1 % 2 == 0:
            type_room = "O"
        elif n1 % 2 != 0:
            type_room = "A"
        print(f"{type_room}{room_number}", end=" ")
    print()