import random

def pokerziehung(anz=5):
    mlist = []
    for i in range(0, 53):
        mlist.append(i)
    for j in range(anz):
        index = random.randrange(0, 53)
        lastposition = len(mlist)-1-j
        mlist[index], mlist[lastposition] = mlist[lastposition], mlist[index]
    return karte(index)



def karte(zahl):
    symbol = zahl // 13
    if symbol == 0:
        symbol = 'Kreuz'
    elif symbol == 1:
        symbol = 'Pik'
    elif symbol == 2:
        symbol = 'Herz'
    else:
        symbol = 'Karo'

    nummer = zahl % 13
    if nummer == 10:
        nummer = 'Bube'
    elif nummer == 11:
        nummer = 'Dame'
    elif nummer == 12:
        nummer = 'König'
    elif nummer + 1 == 1:
        nummer = 'Ass'
    else:
        nummer = nummer +1

    return  symbol + ' ' + str(nummer)


if __name__ == '__main__':
    print(pokerziehung())