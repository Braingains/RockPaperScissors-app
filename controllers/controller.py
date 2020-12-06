from flask import render_template, request, redirect
from app import app
from models.game import *
from models.player import *

@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route('/rules')
def rules():
    return render_template('rules.html', title='Rules')

@app.route('/play/<player_1_choice>/<player_2_choice>')
def play(player_1_choice, player_2_choice):
    return (f'{play_game(player_1_choice, player_2_choice)}')
    