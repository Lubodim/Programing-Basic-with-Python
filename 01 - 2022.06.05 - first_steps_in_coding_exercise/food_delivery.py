chicken_menu = int(input())
fish_menu = int(input())
vegetarian_menu = int(input())

price_chicken_menu = chicken_menu * 10.35
price_fish_menu = fish_menu * 12.40
price_vegetarian_menu = vegetarian_menu * 8.15
price_for_delivery = 2.50

price_all_main_food = price_vegetarian_menu + price_chicken_menu + price_fish_menu
price_desert = price_all_main_food * 1.2 - price_all_main_food

total_delivery_price = price_all_main_food + price_desert + price_for_delivery

print(total_delivery_price)