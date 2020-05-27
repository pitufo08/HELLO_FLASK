import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html" , page_tittle="About", list_of_numbers=[1, 2, 3])

@app.route('/contact')
def contact():
     return render_template("contact.html" , page_tittle="Contact")

@app.route("/careers")
def careers():
     return render_template("careers.html" , page_tittle="Careers")

if __name__ == '__main__':
    app.run(debug=True)