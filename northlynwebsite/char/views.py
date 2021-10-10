# char/views.py
from flask import render_template,request,Blueprint

char = Blueprint('char',__name__)

@char.route('/rotmus')
def rotmus():
    return render_template('rotmus.html')

@char.route('/doc')
def doc():
    return render_template('doc.html')

@char.route('/game')
def game():
    return render_template('game.html')
