voucher_price = int(input())
movie = input()
ticket_counter = 0
other_products_counter = 0
current_price = 0
while movie != "End":
    if len(movie) > 8:
        current_price = ord(movie[0]) + ord(movie[1])
        voucher_price -= current_price
        if voucher_price < 0:
            break
        ticket_counter += 1
    else:
        current_price = ord(movie[0])
        voucher_price -= current_price
        if voucher_price < 0:
            break
        other_products_counter += 1
    movie = input()
print(f"{ticket_counter}")
print(f"{other_products_counter}")