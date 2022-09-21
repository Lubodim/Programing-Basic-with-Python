price_mackerel = float(input()) # скумрия
price_sprat = float(input()) # цаца

kilogram_bonito = float(input())
kilogram_horse_mackerel = float(input())
kilogram_mussels = int(input())

price_bonito = price_mackerel + price_mackerel * 0.6 # паламуд
price_horse_mackerel = price_sprat + price_sprat * 0.8 # сафрид
price_mussels = 7.50 # миди

needed_money = price_bonito * kilogram_bonito \
               + price_horse_mackerel * kilogram_horse_mackerel \
               + price_mussels * kilogram_mussels
print("%.2f" % needed_money)