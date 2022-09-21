bugget = float(input())
season = input()

trip_to = ""
type_rest = ""

if bugget <= 100:
    trip_to = "Bulgaria"
    if season == "summer":
        bugget *= 0.3
    elif season == "winter":
        bugget *= 0.7
elif bugget <= 1000:
    trip_to = "Balkans"
    if season == "summer":
        bugget *= 0.4
    elif season == "winter":
        bugget *= 0.8
elif bugget > 1000:
    trip_to = "Europe"
    if trip_to == "Europe":
        bugget *= 0.9

if season == "summer":
    type_rest = "Camp"
else:
    type_rest = "Hotel"

if trip_to == "Europe":
    type_rest = "Hotel"

print(f"Somewhere in {trip_to}")
print(f"{type_rest} - {bugget:.2f}")
