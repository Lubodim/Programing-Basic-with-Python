number_juniors = int(input())
number_seniors = int(input())
type_route = input()

tax_juniors = 0
tax_seniors = 0

if type_route == "trail":
    if number_juniors:
        tax_juniors = 5.50
    if number_seniors:
        tax_seniors = 7
elif type_route == "cross-country":
    if number_juniors:
        tax_juniors = 8
    if number_seniors:
        tax_seniors = 9.5
elif type_route == "downhill":
    if number_juniors:
        tax_juniors = 12.25
    if number_seniors:
        tax_seniors = 13.75
elif type_route == "road":
    if number_juniors:
        tax_juniors = 20
    if number_seniors:
        tax_seniors = 21.5

sum_donation = number_juniors * tax_juniors + number_seniors * tax_seniors

if type_route == "cross-country" and (number_seniors + number_juniors) >= 50:
    sum_donation *= 0.75
sum_donation *= 0.95    #такси отделени от организаторите

print(f"{sum_donation:.2f}")
