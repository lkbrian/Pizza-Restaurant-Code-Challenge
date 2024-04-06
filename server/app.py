#!usr/bin/env python3
from flask import Flask,make_response,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import db, Restaurant,Pizza,RestaurantPizza

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///restaurant.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return '<h2><pre>/restaurants(GET)</pre><pre>restaurants/:id(GET,DELETE)</pre><pre>/pizzas(GET)</pre><pre>/restaurant_pizzas(POST)</pre></h2>'



if __name__ == "__main__":
    app.run(port=5555, debug=True)