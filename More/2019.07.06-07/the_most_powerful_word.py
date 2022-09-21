from math import floor

word = input()
most_powerful_word_num = 0
most_powerful_word_str = ""
current_word = 0
while word != "End of words":
    sum(ord(ch) for ch in word)
    if sum(ord(ch) for ch in word) > current_word:
        current_word = sum(ord(ch) for ch in word)
    if word[0] == "a" or word[0] == "e" or word[0] == "i" or word[0] == "o" \
            or word[0] == "u" or word[0] == "y" or word[0] == "A"\
            or word[0] == "E" or word[0] == "I" or word[0] == "O"\
            or word[0] == "U" or word[0] == "Y":
        current_word *= len(word)
    else:
        current_word /= len(word)
        current_word = floor(current_word)
    if current_word > most_powerful_word_num:
        most_powerful_word_num = current_word
        most_powerful_word_str = word
    word = input()
print(f"The most powerful word is {most_powerful_word_str} - {most_powerful_word_num}")
