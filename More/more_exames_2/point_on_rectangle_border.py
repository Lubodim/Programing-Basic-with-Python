x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x = float(input())
y = float(input())

border_point = ""

if (x == x1 or x == x2) and y1 <= y <= y2:
    border_point = "Border"
elif (y == y1 or y == y2) and x1 <= x <= x2:
    border_point = "Border"
else:
    border_point = "Inside / Outside"

print(border_point)