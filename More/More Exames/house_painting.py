x = float(input())
y = float(input())
h = float(input())

triangle_area = x * h / 2
rectangle_area_roof = x * y
rectangle_area_wall = x * y - 1.5 * 1.5
front_wall_area = x * x - 1.2 * 2
back_wall_area = x * x

roof_area = triangle_area * 2 + rectangle_area_roof * 2
wall_area = rectangle_area_wall * 2 + front_wall_area + back_wall_area

green_paint_needed = wall_area / 3.4
red_paint_needed = roof_area / 4.3

print(format(green_paint_needed, ".2f"))
print(format(red_paint_needed, ".2f"))