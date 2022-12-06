import random
#min = 50 max = 100 7 ziehungen(wieoft)



def ziehunggescheit(min, max, wieoft):
    lottzahlen = []
    for i in range(min, max+1):
        lottzahlen.append(i)
    for j in range(wieoft):
        index = random.randrange(0, max-min+1)
        lastposition = len(lottzahlen)-1-j
        lottzahlen[index], lottzahlen[lastposition] = lottzahlen[lastposition], lottzahlen[index]
    return lottzahlen[-wieoft:]#alle zahlen in lottozahlen von 45-wieoft bis 45 in dem array




#1000 Ziehungen:
def stats(min, max, wieoft=6, anz_ziehungen=1000):
    stat_dict = {}
    for i in range(min, max+1):
        stat_dict[i] = 0

    for i in range(anz_ziehungen):
        for elm in ziehunggescheit(min, max ,wieoft):
            stat_dict[elm] += 1
    return stat_dict

if __name__ == '__main__':
    min = 0
    max = 45
    wieoft = 6
    anz_ziehungen = 10000
    unser_stats = stats(min, max, wieoft, anz_ziehungen)
    print(sorted(unser_stats.items()))
 #   print(ziehunggescheit(1, 45, 6))