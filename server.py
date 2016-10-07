from flask import Flask, render_template, request, redirect, session
import random
from datetime import datetime, date, time
app = Flask(__name__)
app.secret_key = 'supersecret111'

@app.route('/')
def index():
    if (session.get('gold') is None):
        session['gold'] = 0
        session['activity'] = []
    length = len(session['activity'])
    return render_template('index.html', activity = session['activity'], length = length)

@app.route('/process', methods = ['POST'])
def process():
    option  = request.form['option']
    currentactivity = ""
    if (option == 'pan'):
        change = random.randrange(10,21)
        session['gold'] += change
        currentactivity += "Earned " + str(change) + " gold by panning!"
    elif (option == 'mine'):
        change = random.randrange(0,41)
        session['gold'] += change
        currentactivity += "Earned " + str(change) + " gold by mining!"
    elif (option == 'pick'):
        chance = random.random()
        if (chance > 0.5):
            change = random.randrange(20,101)
            session['gold'] += change
            currentactivity += "Earned " + str(change) + " gold by pickpocketing!"
        elif (chance < 0.05):
            change = -1 * session['gold']
            session['gold'] = 0
            currentactivity += "Lost all " + str(-change) + " gold for thievery!"
        else:
            change = 0
            currentactivity += "Failed to pickpocket anything!"
    elif (option == 'gamble'):
        change = random.randrange(-50,51)
        session['gold'] += change
        if (session['gold'] < 0):
            session['gold'] = 0
        if (change < 0):
            currentactivity += "Lost " + str(-change) + " gold by gambling!"
        elif (change > 0):
            currentactivity += "Won " + str(change) + " gold by gambling!"
        elif (chang == 0):
            currentactivity += "Broke even at the casino!"
    now = str(datetime.now())
    now = now[:19]
    currentactivity += " (" + now + ")"
    session['activity'].append(currentactivity)
    return redirect('/')

app.run(debug=True)
