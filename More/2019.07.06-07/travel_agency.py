city_name = input()
type_package = input()
vip_card = input()
days = int(input())
price_per_day = 0
if days > 7:
    days -= 1
if city_name == "Bansko" and type_package == "withEquipment":
    price_per_day = 100
    if vip_card == "yes":
        price_per_day *= 0.9
elif city_name == "Bansko" and type_package == "noEquipment":
    price_per_day = 80
    if vip_card == "yes":
        price_per_day *= 0.95
elif city_name == "Borovets" and type_package == "withEquipment":
    price_per_day = 100
    if vip_card == "yes":
        price_per_day *= 0.9
elif city_name == "Borovets" and type_package == "noEquipment":
    price_per_day = 80
    if vip_card == "yes":
        price_per_day *= 0.95
elif city_name == "Varna" and type_package == "withBreakfast":
    price_per_day = 130
    if vip_card == "yes":
        price_per_day *= 0.88
elif city_name == "Varna" and type_package == "noBreakfast":
    price_per_day = 100
    if vip_card == "yes":
        price_per_day *= 0.93
elif city_name == "Burgas" and type_package == "withBreakfast":
    price_per_day = 130
    if vip_card == "yes":
        price_per_day *= 0.88
elif city_name == "Burgas" and type_package == "noBreakfast":
    price_per_day = 100
    if vip_card == "yes":
        price_per_day *= 0.93
price = price_per_day * days
if days < 1:
    print("Days must be positive number!")
elif city_name != "Bansko" and city_name != "Borovets" and city_name != "Varna" and city_name != "Burgas":
    print("Invalid input!")
elif type_package != "noEquipment" and type_package != "withEquipment" and type_package != "noBreakfast" and type_package != "withBreakfast":
    print("Invalid input!")
else:
    print(f"The price is {price:.2f}lv! Have a nice time!")