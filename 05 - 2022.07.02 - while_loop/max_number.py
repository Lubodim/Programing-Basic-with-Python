from sys import maxsize


max_size = -maxsize
command = input()

while command != "Stop":
    number = int(command)
    if max_size < number:
        max_size = number
    command = input()
else:
    print(max_size)