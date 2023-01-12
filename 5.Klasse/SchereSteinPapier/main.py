import json
import random

from flask import Flask
from numpy import record

import requests


symbol_dic = {"stein" : 1, "spock" : 2, "papier" : 3,  "echse" : 4, "schere" : 5}
dic_symbol = {1 : "stein", 2 : "spock", 3 : "papier", 4 : "echse", 5 : "schere"}

count_symbol_player = {"stein" : 0, "spock" : 0, "papier" : 0,  "echse" : 0, "schere" : 0}
count_symbol_comp = count_symbol_player.copy()

spielergewonnenmit = []


print("Willkommen zu Schere, Stein, Papier, Spock, Echse!")


def game():
    rundencounter = 0
    gamemode = "E"
    next_round = "j"
    while next_round == "j":
        rundencounter+=1
        playerwins = 0
        compwins = 0
        if(rundencounter > 5):
            gamemode = input("\nDie ersten Runden sind geschafft! Soll die nächste Runde lieber Easy(E) oder Hard(H) sein?: ")
        gewählt = input("\nWähle Schere, Stein, Papier, Spock oder Echse: ")
        if gewählt not in symbol_dic:
            print("Eingabe war falsch, bitte nochmal!")
            continue
        count_symbol_player[gewählt] = 1
        #print(count_symbol_player[gewählt])
        gewählt_zahl = symbol_dic[gewählt]
        print("\nSpieler:", gewählt)
        if gamemode == "E":
            gewähltcomp = random.randrange(1, len(symbol_dic)+1)
            gewähltcom = dic_symbol[gewähltcomp]
            count_symbol_comp[gewähltcom] = 1
            #print(count_symbol_comp)
            print("\nComputer:", dic_symbol[gewähltcomp], "\n")
        elif gamemode == "H":
            #print(spielergewonnenmit)
            counter = 0
            element = spielergewonnenmit[0] 
            for i in spielergewonnenmit: 
                curr_frequency = spielergewonnenmit.count(i) 
                if(curr_frequency > counter): 
                    counter = curr_frequency 
                    element = i 
            if(element == "echse" or element == "schere"):
                gewähltcomp = 1
            elif(element == "stein"):
                gewähltcomp = 2
            elif(element == "spock"):
                gewähltcomp = 3
            elif(element == "papier"):
                gewähltcomp = 4
            # else - eigentlich nicht notwendig da durch das nicht beachten aller fälle der 5 nicht abgedeckt werden muss
            else:                  
                gewähltcomp = 5

        unterschied=(gewählt_zahl-gewähltcomp) % 5
        if unterschied == 0:
            gewinner = "Unentschieden!"
        elif unterschied <= 2:
            gewinner = "Spieler gewinnt!"
            spielergewonnenmit.append(gewählt)
            playerwins+=1
        elif unterschied <= 4:
            gewinner = "Computer gewinnt!"
            compwins+=1
        playerwins = requests.get("http://localhost:5000/", data=json.dumps({"gewählt": gewählt, "gewähltcom": gewähltcom, "playerwins": playerwins, "compwins": compwins}))
        print(playerwins)
        #playerwins = getdata_from_db(gewählt, gewähltcom, playerwins, compwins)[2]
        compwins = requests.get("http://localhost:5000/", data={"gewählt": gewählt, "gewähltcom": gewähltcom, "playerwins": playerwins, "compwins": compwins})
        
        #requests.put("http://localhost:5000/", data={"count_symbol_player": count_symbol_player, "count_symbol_comp": count_symbol_comp, "playerwins": playerwins, "compwins": compwins, "gewählt": gewählt, "gewähltcom": gewähltcom})
        #save_data(count_symbol_player, count_symbol_comp, playerwins, compwins, gewählt, gewähltcom)
        print(gewinner)
        
        print("\nSpieler:", playerwins, "Computer:", compwins)
        
        next_round = input("\nNoch eine Runde?(j/n)")
        if next_round == "n":
            menu()

        #if input("\nDB zurücksetzen?(ja/nein)") == "ja":
            #restart()
        
def menu():
    exit = False
    print("Willkommen im Menü!")
    while exit == False:
        todo = input("Sie können wählen zwischen /game, /resetdb, /stats oder /exit: ")
        if todo == "/game":
            game()
        #elif todo == "/resetdb":
            #reset_db()
        #elif todo == "/stats":
            #show_all_data()
        elif todo == "/exit":
            exit = True

if __name__ == "__main__":
    menu()