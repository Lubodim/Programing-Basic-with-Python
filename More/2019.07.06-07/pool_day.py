from math import ceil

number_people = int(input())
tax_input = float(input())
price_sun_lounger = float(input())
price_umbrella = float(input())

tax = tax_input * number_people
umbrella = price_umbrella * ceil(number_people / 2)
sun_lounger = price_sun_lounger * ceil(number_people *0.75)
total_sum = tax + umbrella + sun_lounger
print(f"{total_sum:.2f} lv.")
