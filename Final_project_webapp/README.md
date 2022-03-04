---
layout: post
title: Blog Post 2 - Simple Flask Web Development
---

Hi everyone! In this blog post, I am going to create a simple, interesting Message Bank webapp using Flask. This webapp allows users to submit and view their message on the web page. In this tuturial, I will show you how to create this webapp step by step!

The skills/languages we will use to create this webapp:

- Python
- HTML
- CSS
- SQL

## §1. Enable Submissions

First of all, we need to create a 'submit' template with three user interface elements:

1. text box 1 - Submit the message
2. text box 2 - Submit the name of the user
3. A 'submit' botton

### HTML Files

We first create two HTML files, "base.html", "submit.html". We put navigation links inside the template "base.html", and we then had the "submit.html" extend "base.html".

**base.html**

```html
{%raw%}
<!doctype html>
<!-- Link to the CSS stylesheet -->
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">

<!-- This appears at the top of the browser window -->
<title>Blog Post 2</title>
<nav>
  <!-- Web page heading -->
  <h1>A Simple Message Bank By Jeff</h1>
  <ul>
    <!-- Link the submit page on main page -->
    <li><a href="{{ url_for('submit') }}">Submit a Message</a></li>
    <!-- Link the view page on main page -->
    <li><a href="{{ url_for('view') }}">View Messages</a></li>
  </ul>
</nav>

<section class="content">
  <header>
    {% block header %}{% endblock %}
  </header>
  {% block content %}
    <br>
    <p> Welcome to Jeff's simple message bank! Click Submit button to submit a message and view them by clicking View Message</p>
  {% endblock %}
</section>
{%endraw%}
```

**submit.html**


```html
{%raw%}
<!--The Submit Message Page Extended from base.html-->

{% extends 'base.html' %}

{% block header %}
  <h1>{% block title %}Enter Your Message and Name{% endblock %}</h1>
{% endblock %}

{% block content %}
    <!-- Creating the three user interfaces within a form tag -->
    <br>
    <form method="post">

      <!-- Create a text box to submit names or handles -->
      <label for="handle">Enter Your Name</label>
      <input type="text" name="handle" id="handle">
      <br>

      <!-- Create a text box to submit a message -->
      <label for="message">Enter Your Message:</label>
      <input type="text" name="message" id="message">
      <br>
      
      <!-- Creating a submit button -->
      <input type="submit" value="Submit message">
    </form>

{% if thanks %}
    <b>Thank you for submitting a message!</b>
{% endif %}


{% endblock %}
{%endraw%}
```

Then, we create a new file "app.py" and write two Python functions for database management:

- **get_message_db():** This function will create the database of messages.

- **insert_message(request):** This function will handle inserting a user messageinto the database of messages we've create using get_message_db()

Before we start writing our function, we need to make sure we've imported necessary packages. Also, we should create an instance of the Flask class with the name of our web app module. This will enable Flask to locate our template and static/CSS file.


```python
from random import random
from flask import Flask, g, render_template, request
import sqlite3

app = Flask(__name__)
```

Then, let's define our get_message_db() function


```python
def get_message_db():
    '''
    This function check whether there is a 
    database call "message_db". If not, we connect to
    that database.
    '''
    # open a database to store the messages
    if "message_db" not in g:
        g.message_db = sqlite3.connect("messages_db.sqlite")
    cursor = g.message_db.cursor()

    # Check whether a table called messages exists in message_db
    # Create this table if not
    cmd = "CREATE TABLE IF NOT EXISTS \
    messages (id integer PRIMARY KEY \
    AUTOINCREMENT, handle text, message text)"
    cursor.execute(cmd)
    
    # Don't forget to close the database
    cursor.close()
    return g.message_db
```

Next, we define "insert_message(request)" function.


```python
def insert_message(request):
    '''
    This function handle inserting a user message
    into the database of messages.
    '''
    # Extract message and handle
    input_message = request.form['message']
    input_handle = request.form['handle']

    # Insert the message into the message database
    # using a cursor
    db = get_message_db()
    cursor = db.cursor()
    cursor.execute(f"INSERT INTO messages (handle, message) VALUES (?, ?)", (input_handle, input_message))

    # Ensure that the row insertion has been saved
    db.commit()
    
    # Close the database
    db.close()
```

Then, let's update our "app.py" file by defining main() and submit() functions.


```python
# Define main() function
@app.route("/")
def main():
    '''
    This function set the base template 
    to be the home page
    '''
    return render_template('base.html')
```


```python
# Define submit() function so that we can put the message into
# the database
@app.route("/submit/", methods=['GET', 'POST'])
def submit():
    '''
    This function allow us to submit the name 
    and message into the database.
    '''
    # Jump to the submit page if we receive "GET" methods
    if request.method == 'GET':
        return render_template('submit.html')
    # Insert messages into database if "POST" request
    # And return to submit template after submitting message
    else:
        insert_message(request)
        return render_template('submit.html', thanks=True)
```

## §2. Viewing Random Submissions

In first part, we've create the 'base' and 'submit' templates, and we've also updated 'main()' and 'submit()' methods in the 'app.py' file. Now in second part, we are going to write a 'view' template to randomly view our submissions. 

**random_messages()**

We first write a function in 'app.py' file called 'random_messages()' to return a collection of n random messsages from the database 'message_db'.


```python
def random_messages(n):
    '''
    This function return a collection 
    of n random messages from the 'message_db'
    # First we connect the database
    '''
    # connect to the database
    db = get_message_db()
    cursor = db.cursor()
    n_random_message = cursor.execute(f'SELECT message, handle FROM messages ORDER BY RANDOM() LIMIT {n}').fetchall()

    # Close the database
    db.close()
    # return n random messages
    return n_random_message
```

**view()**

Then, we define view() method to let the users randomly view 5 submissions. 


```python
# Define view() function
@app.route("/view/", methods=['GET'])
def view():
    '''
    This function allow us to pass
    the random messages as an argument to
    render_template().
    '''
    return render_template("view.html", messages = random_messages(5))
```

**view.html**

We then write our view template "view.html", and it should also extend "base.html". 


```html
{%raw%}
<!--The View Page Extended from base.html-->
{% extends 'base.html' %}

{% block header %}
    <!-- Title -->
<h1>{% block title %}Some Cool Messages{% endblock %}</h1>
{% endblock %}

{% block content %}
  {% for m in messages %}
  <br>
  <b>{{m.1}}</b>
  <br>
  <i>- {{m.0}}</i>
  <br>
  {% endfor %}
{% endblock %}
{%endraw%}
```

## §3. Customize Your App

To make our app more beautiful, we can customize our web app by editing the CSS.

**style.css**


```css
{%raw%}
html {
    background: rgb(249, 205, 173);
    padding: 1rem;
    font-family: Monospace;
    font-size: x-large;
}

body {
    max-width: 900px;
    margin: 0 auto;
    line-height: 1cm;

}

h1 {
    color: rgb(23, 23, 24);
    font-family: cursive;
    margin: 1 auto;
    text-align: center;
    padding: 1rem;
}

nav {
    padding: 0 1rem;
    border-radius: 25px;
    max-width: 5000px;
}

nav ul li a {
    display: block;
    padding: 0.4rem;
}


input {
    outline-style: none;
    border-radius: 3px;
}

a {
    text-decoration: none;
}
{%endraw%}
```

Let's see some screenshots of our web app! Also, we should remember to activate the appropriate PIC16B conda environment and navigate to the directory where app.py file located at. After activate the conda environment, we run the following code in the terminal before we test our web app.

```zsh
 {%raw%}
conda activate PIC16B
export FLASK_ENV=development
flask run
{%endraw%}
```

**Screencap 1 - Example of a user submitting a message** 

![Figure 1](https://github.com/jeff1hwang/jeff1hwang.github.io/blob/master/images/blog_post2/figure4.png?raw=true)

**Screencap 2 - An example of a user viewing submitted messages**

![Figure 2](https://github.com/jeff1hwang/jeff1hwang.github.io/blob/master/images/blog_post2/figure5.png?raw=true)

