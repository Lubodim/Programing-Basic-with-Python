from sys import maxsize

number_of_movies = int(input())
rating_counter = 0
min_rating = maxsize
max_rating = -maxsize
max_rating_name = ""
min_rating_name = ""

for _ in range(number_of_movies):
    movie_name = input()
    movie_rating = float(input())
    if movie_rating > max_rating:
        max_rating = movie_rating
        max_rating_name = movie_name
    elif movie_rating < min_rating:
        min_rating = movie_rating
        min_rating_name = movie_name
    rating_counter += movie_rating
average_rating = rating_counter / number_of_movies
print(f"{max_rating_name} is with highest rating: {max_rating}")
print(f"{min_rating_name} is with lowest rating: {min_rating}")
print(f"Average rating: {average_rating:.1f}")