book_name = input()
current_book_name = input()
book_counter = 0
while current_book_name != "No More Books":
    if current_book_name == book_name:
        print(f"You checked {book_counter} books and found it.")
        break
    book_counter += 1
    current_book_name = input()
else:
    print("The book you search is not here!")
    print(f"You checked {book_counter} books.")
