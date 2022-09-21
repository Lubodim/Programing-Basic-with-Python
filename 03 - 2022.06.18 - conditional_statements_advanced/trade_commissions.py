city = input()
sales = float(input())

comisions = sales
error_condition = False

if city == "Sofia":
    if 0 <= sales <= 500:
        comisions *= 0.05
    elif 500 < sales <= 1000:
        comisions *= 0.07
    elif 1000 < sales <= 10000:
        comisions *= 0.08
    elif sales > 10000:
        comisions *= 0.12
    else:
        error_condition = True
elif city == "Varna":
    if 0 <= sales <= 500:
        comisions *= 0.045
    elif 500 < sales <= 1000:
        comisions *= 0.075
    elif 1000 < sales <= 10000:
        comisions *= 0.10
    elif sales > 10000:
        comisions *= 0.13
    else:
        error_condition = True
elif city == "Plovdiv":
    if 0 <= sales <= 500:
        comisions *= 0.055
    elif 500 < sales <= 1000:
        comisions *= 0.08
    elif 1000 < sales <= 10000:
        comisions *= 0.12
    elif sales > 10000:
        comisions *= 0.145
    else:
        error_condition = True
else:
    error_condition = True

if not error_condition:
    print(f"{comisions:.2f}")
else:
    print("error")
