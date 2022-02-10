from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("main_page.html")

@app.route("/other_page1/")
def view():
    return render_template("other_page1.html")

@app.route("/other_page2/")
def view():
    return render_template("other_page2.html")

@app.route("/result_page/")
def view():
    return render_template("result_page1.html")