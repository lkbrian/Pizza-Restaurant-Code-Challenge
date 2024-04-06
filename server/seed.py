#!usr/bin/env python3
from random import randint,choice as rc
from app import app
from models import db,Restaurant,Pizza,RestaurantPizza

with app.app_context():

    Restaurant.query.delete()
    Pizza.query.delete()
    RestaurantPizza.query.delete()

    pizza_types=['Chicken Pizza','Meat Pizza','Pepperoni Pizza','Chhese Pizza','Hawaiian Pizza','Cheeseburger Pizza']

    places = ['Mambo Italia','Dominos Pizza','Pizza Inn','Mojo Pizza','Que Pasa']

    restaurants =[]
    for place in places:
        restaurant = Restaurant(name=place)
        restaurants.append(restaurant)
        db.session.add(restaurant)
    db.session.commit()

    pizzas = []
    for pizza_type in pizza_types:
        pizza = Pizza(name=pizza_type)
        pizzas.append(pizza)
        db.session.add(pizza)
    db.session.commit()

    for restaurant in restaurants:
        for pizza in pizzas:
            price = round(randint(10, 30) + randint(0, 99) / 100, 2)
            restaurant_pizzas =RestaurantPizza(price=price,pizza=pizza,restaurant=restaurant)
            db.session.add(restaurant_pizzas)
        db.session.commit()

    print("Seeded databse")