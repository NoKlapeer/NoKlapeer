from flask import Flask
from flask_restful import Api, Resource
import mysql.connector


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
    data_player = {"name" : result[0][0], "stein" : result[0][1], "spock" : result[0][2], "papier" : result[0][3], "echse" : result[0][4], "schere" : result[0][5], "wins" : result[0][6]}
    data_comp = {"name" : result[1][0], "stein" : result[1][1], "spock" : result[1][2], "papier" : result[1][3], "echse" : result[1][4], "schere" : result[1][5], "wins" : result[1][6]}
    print(data_player)
    print(data_comp)
    return data_player

def reset_db():
    sqlpclear = f'UPDATE stats SET stein = 0, spock = 0, papier = 0, echse = 0, schere = 0,wins = 0 WHERE name = "player"'
    sqlcclear = f'UPDATE stats SET stein = 0, spock = 0, papier = 0, echse = 0, schere = 0,wins = 0 WHERE name = "computer"'
    my_cursor.execute(sqlpclear)
    my_cursor.execute(sqlcclear)
    ssp_db.commit()


app = Flask(__name__)
api = Api(app)

class ApiClass(Resource):
    def get(self):
        data = show_all_data()
        return data

api.add_resource(ApiClass, '/')
app.run(debug = "True")