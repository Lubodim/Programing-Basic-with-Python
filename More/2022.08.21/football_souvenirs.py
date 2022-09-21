team = input()
souvenir = input()
number_of_souvenir = int(input())
price = 0

if team == "Argentina":
    if souvenir == "flags":
        price = 3.25
    elif souvenir == "caps":
        price = 7.20
    elif souvenir == "posters":
        price = 5.10
    elif souvenir == "stickers":
        price = 1.25
    else:
        print("Invalid stock!")
elif team == "Brazil":
    if souvenir == "flags":
        price = 4.20
    elif souvenir == "caps":
        price = 8.50
    elif souvenir == "posters":
        price = 5.35
    elif souvenir == "stickers":
        price = 1.20
    else:
        print("Invalid stock!")
elif team == "Croatia":
    if souvenir == "flags":
        price = 2.75
    elif souvenir == "caps":
        price = 6.90
    elif souvenir == "posters":
        price = 4.95
    elif souvenir == "stickers":
        price = 1.10
    else:
        print("Invalid stock!")
elif team == "Denmark":
    if souvenir == "flags":
        price = 3.10
    elif souvenir == "caps":
        price = 6.50
    elif souvenir == "posters":
        price = 4.80
    elif souvenir == "stickers":
        price = 0.90
    else:
        print("Invalid stock!")
else:
    print("Invalid country!")

total_price = price * number_of_souvenir

if team =="Argentina" or team == "Brazil" or team == "Croatia" or team == "Denmark":
    if souvenir == "flags" or souvenir == "caps" or souvenir == "posters" or souvenir == "stickers":
        print(f'Pepi bought {number_of_souvenir} {souvenir} of {team} for {total_price:.2f} lv.')
