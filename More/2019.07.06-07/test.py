word = input()


while word != "End of words":
    print(sum(ord(ch) for ch in word))
    print(sum(map(ord, word)))
    break