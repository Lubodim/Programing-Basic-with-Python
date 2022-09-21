from sys import maxsize


min_size = maxsize
command = input()

while command != "Stop":
    number = int(command)
    if min_size > number:
        min_size = number
    command = input()
else:
    print(min_size)