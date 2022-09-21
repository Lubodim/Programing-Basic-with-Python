movie_name = input()
days_number = int(input())
tickets_number = int(input())
tickets_price = float(input())
percentage_for_cinema = int(input())

total_sum = days_number * tickets_number * tickets_price\
            - (days_number * tickets_number * tickets_price * percentage_for_cinema / 100)
print(f"The profit from the movie {movie_name} is {total_sum:.2f} lv.")