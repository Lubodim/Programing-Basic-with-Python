cat_breed = input()
gender = input()
cat_life = 0
if gender == "m":
    if cat_breed == "British Shorthair":
        cat_life = 13 * 12 / 6
    elif cat_breed == "Siamese":
        cat_life = 15 * 12 / 6
    elif cat_breed == "Persian":
        cat_life = 14 * 12 / 6
    elif cat_breed == "Ragdoll":
        cat_life = 16 * 12 / 6
    elif cat_breed == "American Shorthair":
        cat_life = 12 * 12 / 6
    elif cat_breed == "Siberian":
        cat_life = 11 * 12 / 6
elif gender == "f":
    if cat_breed == "British Shorthair":
        cat_life = 14 * 12 / 6
    elif cat_breed == "Siamese":
        cat_life = 16 * 12 / 6
    elif cat_breed == "Persian":
        cat_life = 15 * 12 / 6
    elif cat_breed == "Ragdoll":
        cat_life = 17 * 12 / 6
    elif cat_breed == "American Shorthair":
        cat_life = 13 * 12 / 6
    elif cat_breed == "Siberian":
        cat_life = 12 * 12 / 6

if cat_breed == "British Shorthair" or cat_breed == "Siamese" or cat_breed == "Persian"\
        or cat_breed == "Ragdoll" or cat_breed == "American Shorthair" or cat_breed == "Siberian":
    print(f"{int(cat_life)} cat months")
else:
    print(f"{cat_breed} is invalid cat!")