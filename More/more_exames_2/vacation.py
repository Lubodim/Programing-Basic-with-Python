
bugget = float(input())
seasone = input()

place_for_sleep = ""
location = ""
price = 0

if bugget <= 1000:
    place_for_sleep = "Camp"
    if seasone == "Summer":
        location = "Alaska"
        price = bugget * 0.65
    elif seasone == "Winter":
        location = "Morocco"
        price = bugget * 0.45
elif 1000 < bugget <= 3000:
    place_for_sleep = "Hut"
    if seasone == "Summer":
        location = "Alaska"
        price = bugget * 0.8
    elif seasone == "Winter":
        location = "Morocco"
        price = bugget * 0.6
elif bugget > 3000:
    place_for_sleep = "Hotel"
    if seasone == "Summer":
        location = "Alaska"
        price = bugget * 0.9
    elif seasone == "Winter":
        location = "Morocco"
        price = bugget * 0.9
print(f"{location} - {place_for_sleep} - {price:.2f}")
