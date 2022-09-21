capacity_hall = int(input())
command = input()
price1 = 0
people1 = 0

while command != "Movie time!":
    enter_people = int(command)
    people1 += enter_people
    if people1 > capacity_hall:
        break
    price1 += enter_people * 5
    if enter_people % 3 == 0:
        price1 -= 5
    command = input()
if command == "Movie time!":
    difference = capacity_hall - people1
    print(f"There are {difference} seats left in the cinema.")
else:
    print("The cinema is full.")
print(f"Cinema income - {price1} lv.")


capacity = int(input())
command = input()
people = 0
price = 0

while command != "Movie time!":
    people_entering = int(command)
    people += people_entering
    if capacity < people:
        break
    price += people_entering * 5
    if people_entering % 3 == 0:
        price -= 5

    command = input()

if command == "Movie time!":
    print(f"There are {capacity - people} seats left in the cinema.")
else:
    print("The cinema is full.")
print(f"Cinema income - {price} lv.")