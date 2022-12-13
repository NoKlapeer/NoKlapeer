import random
from flask import Flask
import mysql.connector
from numpy import record


ssp_db = mysql.connector.connect(       # zu Schere Stein Papier DB verbinden
    host="localhost",
    user="root",
    password="",
    database="ssp_db"
)

my_cursor = ssp_db.cursor()
my_cursor.execute("SELECT * FROM stats")
#print(my_cursor.fetchall().index(0))
# einmalige Eintragung, damit danach geupdated werden kann
if(len(my_cursor.fetchall()) < 2):
    sqlpfirst = f'INSERT INTO stats VALUES ("player", 0, 0, 0, 0, 0, 0)'
    sqlcfirst = f'INSERT INTO stats VALUES ("computer", 0, 0, 0, 0, 0, 0)'
    my_cursor.execute(sqlpfirst)
    my_cursor.execute(sqlcfirst)
    ssp_db.commit()



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
            print(spielergewonnenmit)
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
            # else - eigentlich nicht notwendig da durch das nich beachter aller fälle der 5 nicht abgedeckt werden muss
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
        
        playerwins = getdata_from_db(gewählt, gewähltcom, playerwins, compwins)[2]
        compwins = getdata_from_db(gewählt, gewähltcom, playerwins, compwins)[3]
        
        save_data(count_symbol_player, count_symbol_comp, playerwins, compwins, gewählt, gewähltcom)
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
        elif todo == "/resetdb":
            reset_db()
        elif todo == "/stats":
            show_all_data()
        elif todo == "/exit":
            exit = True

def getdata_from_db(gew, gewcom, playerwins, compwins):
    # für die Symbole
    my_cursor.execute(f'SELECT {gew} FROM stats where name = "player"')
    selectionplayer = [int(record[0]) for record in my_cursor.fetchall()]
    selectionplayer = selectionplayer[0]
    my_cursor.execute(f'SELECT {gewcom} FROM stats where name = "computer"')
    selectioncomp = [int(record[0]) for record in my_cursor.fetchall()]
    selectioncomp = selectioncomp[0]

    # für die Wins
    my_cursor.execute(f'SELECT wins FROM stats where name = "player"')
    winsplayer = [int(record[0]) for record in my_cursor.fetchall()]
    winsplayer = winsplayer[0]
    my_cursor.execute(f'SELECT wins FROM stats where name = "computer"')
    winscomp = [int(record[0]) for record in my_cursor.fetchall()]
    winscomp = winscomp[0]
    playerwins = winsplayer + playerwins
    compwins = winscomp + compwins

    return selectionplayer, selectioncomp, playerwins, compwins

def save_data(sym_count_p, sym_count_c, p_wins, c_wins, gew, gewcom):

    # für die Symbole
    #my_cursor.execute(f'SELECT {gew} FROM stats where name = "player"')
    #selectionplayer = [int(record[0]) for record in my_cursor.fetchall()]
    #selectionplayer = selectionplayer[0]
    #my_cursor.execute(f'SELECT {gewcom} FROM stats where name = "computer"')
    #selectioncomp = [int(record[0]) for record in my_cursor.fetchall()]
    #selectioncomp = selectioncomp[0]
    selectionplayer = getdata_from_db(gew, gewcom, p_wins, c_wins)[0]
    selectioncomp = getdata_from_db(gew, gewcom, p_wins, c_wins)[1]

    sqlp = f'UPDATE stats SET {gew} = {selectionplayer} + {sym_count_p[gew]}, wins = {p_wins} WHERE name = "player"'
    sqlc = f'UPDATE stats SET {gewcom} = {selectioncomp} + {sym_count_c[gewcom]}, wins = {c_wins} WHERE name = "computer"'
    
    my_cursor.execute(sqlp)
    my_cursor.execute(sqlc)

    ssp_db.commit()


def show_all_data():
    my_cursor.execute("SELECT * FROM stats")
    result = my_cursor.fetchall()
    print(result)
    data_player = {"name" : result[0][0], "stein" : result[0][1], "spock" : result[0][2], "papier" : result[0][3], "echse" : result[0][4], "schere" : result[0][5], "wins" : result[0][6]}
    return data_player

def reset_db():
    sqlpclear = f'UPDATE stats SET stein = 0, spock = 0, papier = 0, echse = 0, schere = 0,wins = 0 WHERE name = "player"'
    sqlcclear = f'UPDATE stats SET stein = 0, spock = 0, papier = 0, echse = 0, schere = 0,wins = 0 WHERE name = "computer"'
    my_cursor.execute(sqlpclear)
    my_cursor.execute(sqlcclear)
    ssp_db.commit()

if __name__ == "__main__":
    menu()