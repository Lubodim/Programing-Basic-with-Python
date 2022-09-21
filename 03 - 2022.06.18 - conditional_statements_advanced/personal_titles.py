age = float(input())
gander = input()

if gander == "m" and age >= 16:
    print("Mr.")
elif gander == "m" and age < 16:
    print("Master")
if gander == "f" and age >= 16:
    print("Ms.")
elif gander == "f" and age < 16:
    print("Miss")
