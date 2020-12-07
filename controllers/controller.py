from flask import render_template, request, redirect
from random import Random
from app import app
from models.game import *
from models.player import *

@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route('/rules')
def rules():
    return render_template('rules.html', title='Rules')

#this was supposed to work on the ('/') route, the ('/play') route was supposed to be for playing the cpu
@app.route('/play/<player_1_choice>/<player_2_choice>', methods=['GET', 'POST'])
def play(player_1_choice, player_2_choice):
    winner = play_game(player_1_choice, player_2_choice)
    return render_template('play.html', title='Play', player_1_choice = player_1_choice, player_2_choice = player_2_choice, winner = winner) 
    



# @app.route('/cpu', methods=['POST'])
# def vs_cpu(player_1_choice):
#     player_choice = player_1_choice
#     cpu_choice = cpu_choice()
#     winner = play_cpu(player_1_choice, computer_choice)
#     return render_template('play.html', title='Play', player_1_choice = player_1_choice, winner = winner)
