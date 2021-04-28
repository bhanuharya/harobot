from flask import Flask, render_template, request

from processInput import *


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start/')
def start():
    return render_template('start.html')

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    answer = str(processInput(userText))
    # if(userText == "halo"):
    #     # return str(english_bot.get_response(userText))
    #     return str('Haro, Warudo!')
    # if(userText == "hi"):
    #     # return str(english_bot.get_response(userText))
    return answer
    