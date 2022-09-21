type_fuel = input()
litres_fuel = int(input())

if 0 <= litres_fuel < 25:
    if type_fuel == "Diesel":
        print(f"Fill your tank with diesel!")
    else:
        if type_fuel == "Gasoline":
            print(f"Fill your tank with gasoline!")
        else:
            if type_fuel == "Gas":
                print(f"Fill your tank with gas!")
            else:
                print(f"Invalid fuel!")
if litres_fuel >= 25:
    if type_fuel == "Diesel":
        print(f"You have enough diesel.")
    else:
        if type_fuel == "Gasoline":
            print(f"You have enough gasoline.")
        else:
            if type_fuel == "Gas":
                print(f"You have enough gas.")
            else:
                print(f"Invalid fuel!")