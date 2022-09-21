duration_of_contract = input()
type_of_contact = input()
mobile_internet = input()
number_of_mounts = int(input())
price = 0
if duration_of_contract == "one" and type_of_contact == "Small":
    price = 9.98
elif duration_of_contract == "one" and type_of_contact == "Middle":
    price = 18.99
elif duration_of_contract == "one" and type_of_contact == "Large":
    price = 25.98
elif duration_of_contract == "one" and type_of_contact == "ExtraLarge":
    price = 35.99
elif duration_of_contract == "two" and type_of_contact == "Small":
    price = 8.58
elif duration_of_contract == "two" and type_of_contact == "Middle":
    price = 17.09
elif duration_of_contract == "two" and type_of_contact == "Large":
    price = 23.59
elif duration_of_contract == "two" and type_of_contact == "ExtraLarge":
    price = 31.79

if mobile_internet == "yes":
    if price <= 10:
        price += 5.50
    elif price <= 30:
        price += 4.35
    else:
        price += 3.85
if duration_of_contract == "two":
    price -= price * 3.75 / 100
price *= number_of_mounts
print(f"{price:.2f} lv.")
