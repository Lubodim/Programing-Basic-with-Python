from math import floor, ceil

whole_vineyard = int(input())
grape_per_squere_meaters = float(input())
needed_litres_wine = int(input())
number_of_workers = int(input())

wine_used_grapes = whole_vineyard * grape_per_squere_meaters * 0.4
litres_of_wine = wine_used_grapes / 2.5

something = abs(litres_of_wine - needed_litres_wine)

if litres_of_wine < needed_litres_wine:
    print(f"It will be a tough winter! More {floor(something)} liters wine needed.")
else:
    print(f"Good harvest this year! Total wine: {floor(litres_of_wine)} liters.")
    print(f"{ceil(something)} liters left -> {ceil(something / number_of_workers)} liters per person.")