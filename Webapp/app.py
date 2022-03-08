# Import the require package and render_template()

from operator import methodcaller
from random import random
from flask import Flask, g, render_template, request
import sqlite3
import pandas as pd
import pickle

# Loading the XGB pre-trained model
xgb_model = pickle.load(open("xgb_model.dat", "rb"))

# Create web app, run with flask run
# (set "FLASK_ENV" variable to "development")

app = Flask(__name__)

def get_message_db():

    # check whether there is a database called "message_db"
    # If not, then we connect to that database
    # open a database to store the messages
    if "message_db" not in g:
        g.message_db = sqlite3.connect("messages_db.sqlite")

    cursor = g.message_db.cursor()

    # Check whether a table called messages exists in message_db
    # Create if not
    cmd = "CREATE TABLE IF NOT EXISTS messages (id integer PRIMARY KEY AUTOINCREMENT, handle text, message text, result text)"
    cursor.execute(cmd)
    cursor.close()
    return g.message_db

def insert_message(request):
    '''
    This function handle inserting a user message
    into the database of messages.
    '''

    # Extract message and handle
    input_message = request.form['message']
    input_handle = request.form['handle']
    muscle_stiffness = request.form['muscle_stiffness']
    weakness = request.form['weakness']
    visual_blurring = request.form['visual_blurring']
    Irritability = request.form['Irritability']
    Alopecia = request.form['Alopecia']
    Polyuria = request.form['Polyuria']
    Polydipsia = request.form['Polydipsia']
    sudden_weight_loss = request.form['sudden_weight_loss']
    Polyphagia = request.form['Polyphagia']
    partial_paresis = request.form['partial_paresis']
    
    d = {'muscle stiffness': [muscle_stiffness], 'weakness': [weakness], 'visual blurring': [visual_blurring],
    'Irritability':[Irritability], 'Alopecia': [Alopecia],
    'Polyuria':[Polyuria], 'Polydipsia':[Polydipsia], 'sudden weight loss':[sudden_weight_loss],
    'Polyphagia':[Polyphagia],'partial paresis':[partial_paresis]}

    df = pd.DataFrame(data = d)
    df = df.replace("no", 0)
    df = df.replace("yes", 1)

    result = xgb_model.predict(df)
    result = result[0]
    if result == 1:
        result = "positive"
    else:
        result = "negative"
    # Insert the message into the message database
    # using a cursor
    db = get_message_db()
    cursor = db.cursor()

    cursor.execute(f"INSERT INTO messages (handle, message, result) VALUES (?, ?, ?)", (input_handle, input_message, result))

    # Ensure that the row insertion has been saved
    db.commit()
    
    # Close the database
    db.close()

# Define random_message() function
def random_messages(n):
    '''
    This function return a collection 
    of n random messages from the 'message_db'
    # First we connect the database
    '''
    db = get_message_db()
    cursor = db.cursor()
    n_random_message = cursor.execute(f'SELECT message, handle, result FROM messages ORDER BY id Desc LIMIT {n}').fetchall()

    # Close the database
    db.close()

    return n_random_message


# Define main() function
@app.route("/")
def main():
    '''
    This function set the base template 
    to be the home page
    '''
    return render_template('base.html')

# Define submit() function so that we can put the message into 
@app.route("/submit/", methods=['GET', 'POST'])
def submit():
    if request.method == 'GET':
        return render_template('submit.html')
    else:
        insert_message(request)
        return render_template('submit.html', thanks=True)

# Define view() function
@app.route("/view/", methods=['GET'])
def view():
    return render_template("view.html", messages = random_messages(1))

