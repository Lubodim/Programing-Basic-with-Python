bugget = float(input())
seasone = input()

type_car = ""
type_class = ""
if bugget <= 100:
    type_class = "Economy class"
    if seasone == "Summer":
        type_car = "Cabrio"
        bugget *= 0.35
    elif seasone == "Winter":
        type_car = "Jeep"
        bugget *= 0.65
elif 100 < bugget <= 500:
    type_class = "Compact class"
    if seasone == "Summer":
        type_car = "Cabrio"
        bugget *= 0.45
    elif seasone == "Winter":
        type_car = "Jeep"
        bugget *= 0.80
elif bugget > 500:
    type_class = "Luxury class"
    type_car = "Jeep"
    bugget *= 0.90
print(type_class)
print(f"{type_car} - {bugget:.2f}")
