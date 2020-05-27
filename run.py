import os
import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html" , page_tittle="About", company=data)
    

@app.route('/contact')
def contact():
     return render_template("contact.html" , page_tittle="Contact")

@app.route("/careers")
def careers():
     return render_template("careers.html" , page_tittle="Careers")

if __name__ == '__main__':
    app.run(debug=True)