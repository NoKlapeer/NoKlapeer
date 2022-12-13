from flask import Flask

from main import show_all_data


app = Flask(__name__)
@app.route('/')
def home():
    return show_all_data()

app.run()