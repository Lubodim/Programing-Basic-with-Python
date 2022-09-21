browser_tab = int(input())
salary = int(input())

for current_tab in range(browser_tab):
    web_site_name = input()
    if web_site_name == "Facebook":
        salary -= 150
    elif web_site_name == "Instagram":
        salary -= 100
    elif web_site_name == "Reddit":
        salary -= 50
    if salary <= 0:
        break

if salary <= 0:
    print(f"You have lost your salary.")
else:
    print(f"{salary}")
