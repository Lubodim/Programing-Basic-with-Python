movie_name = input()
type_pack = input()
ticket_number = int(input())
price = 0
if movie_name == "John Wick":
    if type_pack == "Drink":
        price = 12
    elif type_pack == "Popcorn":
        price = 15
    elif type_pack == "Menu":
        price = 19
elif movie_name == "Star Wars":
    if type_pack == "Drink":
        price = 18
    elif type_pack == "Popcorn":
        price = 25
    elif type_pack == "Menu":
        price = 30
    if ticket_number >= 4:
        price *= 0.7
elif movie_name == "Jumanji":
    if type_pack == "Drink":
        price = 9
    elif type_pack == "Popcorn":
        price = 11
    elif type_pack == "Menu":
        price = 14
    if ticket_number == 2:
        price *= 0.85
price = price * ticket_number
print(f"Your bill is {price:.2f} leva.")