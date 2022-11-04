import winsound


class Melody:

    while True:
        for i in range(200, 2400, 200):
            winsound.Beep(i, 300)
        for i in range(2200, 200, - 200):
            winsound.Beep(i, 300)
