# Array mit 1-45
# Dann zahl ziehen in schleife 6 mal
# An den index wo zahl gezogen wurde stellt man die zahl von dem index an die letzte stelle und man macht die range der zufallszahl um 1 kürzer und das so lange bis man 6 zahlen hat
import random


dic = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 0,
       18: 0, 19: 0, 20: 0, 21: 0, 22: 0, 23: 0, 24: 0, 25: 0, 26: 0, 27: 0, 28: 0, 29: 0, 30: 0, 31: 0, 32: 0,
       33: 0, 34: 0, 35: 0, 36: 0, 37: 0, 38: 0, 39: 0, 40: 0, 41: 0, 42: 0, 43: 0, 44: 0, 45: 0}

listen = []


def liste():
    x = 0
    while x < 45:
        x += 1
        listen.append(x)


def lottoziehung():
    zahlen = []
    y = 0
    ziehen = listen[:]
    while y <= 6:
        zahl = random.choice(ziehen)
        y += 1
        ziehen.remove(zahl)
        zahlen.append(zahl)
    return zahlen


def statistik(zahl):
    for i in range(zahl):
        for j in lottoziehung():
            dic[j] += 1
    print(dic)


liste()
lottoziehung()
statistik(1000)
