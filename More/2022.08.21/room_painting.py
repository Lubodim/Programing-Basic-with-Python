from math import ceil

number_paint_boxes = int(input())
number_wallpapers = int(input())
gloves_price = float(input())
paintbrush_price = float(input())
number_gloves = ceil(number_wallpapers * 0.35)
number_paintbrush = int(number_paint_boxes * 0.48)

product_price = number_paint_boxes * 21.5 + number_wallpapers * 5.20 + number_gloves\
                * gloves_price + number_paintbrush * paintbrush_price

delivery_price = product_price / 15

print(f"This delivery will cost {delivery_price:.2f} lv.")
