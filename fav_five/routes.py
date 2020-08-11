from fav_five import app
from flask import render_template

#home route
@app.route('/')
def home():
    name = "Hot Stuff"
    return render_template("home.html", name=name,)

#Fav_five route
@app.route('/fav_five')
def fav_five():
    fav_dict = {1: 'Otis Redding', 2: 'The Beatles', 3: 'Jesse Dee', 4: 'Ray Charles', 5: 'Gorillaz'}
    return render_template("fav_five.html", fav_dict=fav_dict)