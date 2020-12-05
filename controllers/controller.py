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
