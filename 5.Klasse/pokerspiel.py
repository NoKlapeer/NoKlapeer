import random

mlist = []
hand = []

def ziehung(anz=5):
    global mlist, hand
    mlist = []
    hand = []
    for i in range(0, 52):
        mlist.append(i)
    for j in range(anz):
        index = random.randrange(0, 52)
        lastposition = len(mlist)-1-j
        mlist[index], mlist[lastposition] = mlist[lastposition], mlist[index]
    for k in mlist[-anz:]:
        hand.append(k)
        mlist[mlist.index(k)] = karte(k)
    return mlist[-anz:], hand



def karte(zahl):
    symbol = getsymbol(zahl)
    if symbol == 0:
        symbol = 'Kreuz'
    elif symbol == 1:
        symbol = 'Pik'
    elif symbol == 2:
        symbol = 'Herz'
    else:
        symbol = 'Karo'

    nummer = getnummer(zahl)
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

    return symbol + ' ' + str(nummer)

def getnummer(zahl):
    return zahl % 13

def getsymbol(zahl):
    return int(zahl) // 13

def gethandr(hand):
    handr = []
    for i in range (len(hand)):
        handr.append(getnummer(hand[i]))
    return handr

def getsymr(hand):
    symr = []
    for i in range (len(hand)):
        symr.append(getsymbol(hand[i]))
    return symr

def pair(hand):
    #for i in range(0,5):
       # print(getnummer(hand[i]))
       # if(getnummer(hand[i])):
    handr = gethandr(hand)
    #print(handr)
    dup = [x for i, x in enumerate(handr) if i != handr.index(x)]
    if(len(dup) == 1):
        return True
    return False

def drilling(hand):
    handr = gethandr(hand)
    #print(handr)
    dup = [x for i, x in enumerate(handr) if i != handr.index(x)]
    dup.append("fill")
    counter = 0
    #print(dup)
    for j in range (len(hand)):
        if((len(dup) == 1) or (dup[0] == dup[1])):
            if(dup[0] == handr[j]):
                counter += 1
    if(counter == 3):
        return True
    return False

def vierling(hand):
    handr = gethandr(hand)
    #print(handr)
    dup = [x for i, x in enumerate(handr) if i != handr.index(x)]
    dup.append("fill")
    counter = 0
    #print(dup)
    for j in range (len(hand)):
        if((len(dup) == 4)):
            if(dup[0] == handr[j]):
                counter += 1
    if(counter == 4):
        return True
    return False


def straight(hand):
    handr = gethandr(hand)
    #print(handr)
    counter = 0
    handr.sort()
    for i in range(len(hand)):
        if((handr[i] - handr[i-1])==1):
            counter += 1
    if(counter >=4):
        return True
    return False

def straight_flush(hand):
    handr = gethandr(hand)
    symr = getsymr(hand)
    #print(handr)
    #print(symr)
    counter = 0
    handr.sort()
    for j in range(len(hand)):
        if((symr[j] - symr[j-1])!=0):
            return False
    for i in range(len(hand)):
        if(((handr[i] - handr[i-1])==1)):
            counter += 1
    if(counter ==4):
        return True
    return False

def royal_flush(hand):
    handr = gethandr(hand)
    symr = getsymr(hand)
    #print(handr)
    #print(symr)
    counter = 0
    handr.sort()
    for j in range(len(hand)):
        if((symr[j] - symr[j-1])!=0):
            return False
    for i in range(2,5):
            if((handr[0] == 0) and (handr[1] == 9) and ((handr[i] - handr[i-1])==1)):
                counter += 1
    if(counter == 3):
        return True
    return False

def flush(hand):
    symr = getsymr(hand)
    #print(symr)
    counter = 0
    for i in range(len(hand)):
        if((symr[i] - symr[i-1])==0):
            counter += 1
    if(counter >=4):
        return True
    return False

def full_house(hand):
    handr = gethandr(hand)
    handr.sort()
    #print(handr)
    #for i in range(0,3):
        #if(((handr[i] - handr[i-1])==0)):
            #counter += 1
    #for i in range(2,5):
        #if(((handr[i] - handr[i-1])==0)):
            #counter += 1
    #if(counter == 4):
        #return True
    #return False
    if((drilling(handr[0:3]) and pair(handr[3:5])) or(pair(handr[0:2]) and drilling(handr[2:5]))):
        return True
    return False   

def twopair(hand):
    handr = gethandr(hand)
    #print(handr)
    dup = [x for i, x in enumerate(handr) if i != handr.index(x)]
    dup.append("fill")
    #print(dup)
    if((len(dup) == 3) and (dup[0] != dup[1])):
        return True
    return False

dic1 = {'Royal Flush' : 0, 'Straight Flush' : 0, 'Vierling' : 0, 'Full House' : 0, 'Flush' : 0, 'Straight' : 0, 'Drilling' : 0, 'Two Pair' : 0, 'Pair' : 0, 'High Card' : 0}
dic = {}
komb = ['Royal Flush', 'Straight Flush', 'Vierling', 'Full House', 'Flush', 'Straight', 'Drilling', 'Two Pair', 'Pair', 'High Card']

def createdic(min, max):
    for i in range(min, max+1):
        dic[i] = 0

def kombinationen(hand):
        for i in range(len(hand)):
            if royal_flush(hand):
                dic[0] += 1
                return 'Royal flush'
            elif straight_flush(hand):
                dic[1] += 1
                return 'Straight flush'
            elif vierling(hand):
                dic[2] += 1
                return 'Four of a kind'
            elif full_house(hand):
                dic[3] += 1
                return 'Full House'
            elif flush(hand):
                dic[4] += 1
                return 'Flush'
            elif straight(hand):
                dic[5] += 1
                return 'Straight'
            elif drilling(hand):
                dic[6] += 1
                return 'Three of a kind'
            elif twopair(hand):
                dic[7] += 1
                return 'Two pair'
            elif pair(hand):
                dic[8] += 1
                return 'Pair'
        dic[9] += 1
        return "High Card"

def kalkulation(anz):
    for j in range(anz):
        ziehung()
        kombinationen(hand)       
    return dic

def kalkundausgabe(dic, komb, anz):
    ausgabe = 0
    for i in range(0, 10):
        
        print(komb[i] + " : " + str(round((dic[i]/anz)*100, 5)) + "%")
    return ausgabe

def main():
    createdic(0,9)
    #print(ziehung())
    #print(pair(hand))
    #print(drilling(hand))
    #print(straight(hand))
    #print(straight_flush(hand))
    #print(royal_flush(hand))
    #print(flush(hand))
    #print(full_house(hand))
    #print(twopair(hand))
    #print(vierling(hand))
    #print(kombinationen(hand, 100000))
    kalkulation(1000000)
    print(dic)
    kalkundausgabe(dic, komb, 1000000)


if __name__ == '__main__':
    main()