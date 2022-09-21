best_movie = 0
best_movie_name = ""
current_movie = ""
movie_name = ""
for current_movie in range(1, 7 + 1):
    movie_name = input()
    if movie_name == "STOP":
        break
    lower_counter = 0
    up_er_counter = 0
    ascii_sum = 0
    for char in movie_name:
        ascii_sum += ord(char)

        if char.islower():
            lower_counter += 1
        if char.isupper():
            up_er_counter += 1
    ascii_sum = ascii_sum - 2 * len(movie_name) * lower_counter - len(movie_name) * up_er_counter
    if ascii_sum > best_movie:
        best_movie = ascii_sum
        best_movie_name = movie_name
if current_movie == 7 and movie_name == "STOP":
    print(f"The best movie for you is {best_movie_name} with {best_movie} ASCII sum.")
elif current_movie == 7:
    print("The limit is reached.")
    print(f"The best movie for you is {best_movie_name} with {best_movie} ASCII sum.")
else:
    print(f"The best movie for you is {best_movie_name} with {best_movie} ASCII sum.")
