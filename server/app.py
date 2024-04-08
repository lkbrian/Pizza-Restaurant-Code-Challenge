#!usr/bin/env python3
from flask import Flask,make_response,jsonify,request
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
    return '<h2><pre>GET /restaurants: Retrieves a list of all restaurants.<br>GET /restaurants/<id>: Retrieves details of a specific restaurant by ID.<br>DELETE /restaurants/<id>: Deletes a restaurant by ID.<br>GET /pizzas: Retrieves a list of all pizzas.<br>POST /restaurant_pizzas: Creates a new restaurant pizza.</pre></h2>'

@app.route('/restaurants',)
def restaurants():
    restaurants = [restaurant.to_dict() for restaurant in Restaurant.query.all()]
    return make_response(restaurants,200)

@app.route('/restaurants/<int:id>', methods=['GET','DELETE'])
def get_restaurants(id):
    restaurant = Restaurant.query.filter_by(id=id).first()

    
    if request.method == 'GET':
        response = restaurant.to_dict()
        return make_response(response,200)
    
    elif request.method == 'DELETE':
        db.session.delete(restaurant)
        db.session.commit()
        response = {'succesfull': True,'message':'Restaurant deleted succesfully'}
        return make_response(response,200)



@app.route('/pizzas',)
def get_pizzas():
    pizzas = [pizza.to_dict() for pizza in Pizza.query.all()]
    return make_response(pizzas,200)

@app.route('/restaurant_pizzas',methods=['GET','POST'])
def post_restaurants_pizzas():
    if request.method == "GET":
        restaurant_pizzas = [restaurant_pizza.to_dict() for restaurant_pizza in RestaurantPizza.query.all()]
        return make_response(restaurant_pizzas,200)
    elif request.method == 'POST':
        try:
            new_restaurants_pizza = RestaurantPizza(
                price = request.form.get('price'),
                pizza_id = request.form.get('pizza_id'),
                restaurant_id = request.form.get('restaurant_id')
            )
            db.session.add(new_restaurants_pizza)
            db.session.commit()
            restaurant_pizza = new_restaurants_pizza.to_dict()
            return make_response(restaurant_pizza,201)
        except:
            response = {  "errors": ["validation errors"]}
            return make_response(response,200)        


if __name__ == "__main__":
    app.run(port=5555, debug=True)