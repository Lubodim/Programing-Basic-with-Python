name = input()
password = input()
current_password = input()
while password != current_password:
    current_password = input()
else:
    print(f"Welcome {name}!")
