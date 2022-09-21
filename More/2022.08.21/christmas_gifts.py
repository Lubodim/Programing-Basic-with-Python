adults = 0
kids = 0
toys = 0
sweaters = 0

while True:
    command = input()
    if command == "Christmas":
        break
    command = int(command)
    if command <= 16:
        kids += 1
        toys += 5
    else:
        adults += 1
        sweaters += 15

print(f"Number of adults: {adults}")
print(f"Number of kids: {kids}")
print(f"Money for toys: {toys}")
print(f"Money for sweaters: {sweaters}")
