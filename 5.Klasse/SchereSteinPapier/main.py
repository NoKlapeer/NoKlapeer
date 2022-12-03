import random


symbol_dic = {"Stein" : 1, "Spock" : 2, "Papier" : 3,  "Echse" : 4, "Schere" : 5}
dic_symbol = {1 : "Stein", 2 : "Spock", 3 : "Papier", 4 : "Echse", 5 : "Schere"}

count_symbol = {"Stein" : 0, "Spock" : 0, "Papier" : 0,  "Echse" : 0, "Schere" : 0}

print("Willkommen zu Schere, Stein, Papier, Spock, Echse!")
#gamemode = input("\nWähle zwischen Easy(E) und Hard(H): ")
next_round = "j"
spieler_counter = 0
com_counter = 0
while next_round == "j":
    gewählt = input("\nWähle Schere, Stein, Papier, Spock oder Echse: ")
    if gewählt not in symbol_dic:
        print("Eingabe war falsch, bitte nochmal!")
        continue

    count_symbol[gewählt]+=1
    gewählt_zahl = symbol_dic[gewählt]
    print("\nSpieler:", gewählt)

    gewähltcom = random.randrange(1, len(symbol_dic)+1)
    count_symbol[dic_symbol[gewähltcom]]+=1
    print("\nGegner:", dic_symbol[gewähltcom], "\n")
    
    unterschied=(gewählt_zahl-gewähltcom) % 5
    if unterschied == 0:
        gewinner = "Unentschieden!"
    elif unterschied <= 2:
        gewinner = "Spieler gewinnt!"
        spieler_counter+=1
    elif unterschied <= 4:
        gewinner = "Computer gewinnt!"
        com_counter+=1

    print(gewinner)
    print("\nSpieler:", spieler_counter, "Computer:", com_counter)

    next_round = input("\nNoch eine Runde?(j/n)")