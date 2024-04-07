#!usr/bin/env python3
from random import randint,choice
from faker import Faker
from app import app
from models import db,Restaurant,Pizza,RestaurantPizza

fake = Faker()

with app.app_context():

    Restaurant.query.delete()
    Pizza.query.delete()
    RestaurantPizza.query.delete()


    restaurants =[]
    restaurants.append(Restaurant(name='Mambo Italia',address=fake.address()))
    restaurants.append(Restaurant(name='Dominos Pizza',address=fake.address()))
    restaurants.append(Restaurant(name='Pizza Inn',address=fake.address()))
    restaurants.append(Restaurant(name='Mojo Pizza',address=fake.address()))
    restaurants.append(Restaurant(name='Que Pasa',address=fake.address()))
    restaurants.append(Restaurant(name='Pizza Hut',address=fake.address()))
    db.session.add_all(restaurants)

    pizzas = []
    pizzas.append(Pizza(name='Chicken Pizza', ingredients='Grilled chicken breast, BBQ sauce, Mozzarella cheese, Red onion'))
    pizzas.append(Pizza(name='Meat Pizza', ingredients='Pepperoni, Italian sausage, Bacon, Marinara sauce, Mozzarella cheese'))
    pizzas.append(Pizza(name='Pepperoni Pizza', ingredients='Pepperoni, Marinara sauce, Mozzarella cheese, Parmesan cheese, Oregano'))
    pizzas.append(Pizza(name='Cheese Pizza', ingredients='Marinara sauce, Mozzarella cheese, Parmesan cheese, Basil leaves, Garlic (optional), Olive oil (optional)'))
    pizzas.append(Pizza(name='Hawaiian Pizza', ingredients='Ham or Canadian bacon, Pineapple chunks, Marinara sauce, Mozzarella cheese'))
    db.session.add_all(pizzas)


    for _ in range(10):
        price = round(randint(10, 30) + randint(0, 99) / 100, 2)
        pizza_type = choice(pizzas)
        place = choice(restaurants)
        restaurant_pizzas = RestaurantPizza(price=price, pizza=pizza_type, restaurant=place)
        db.session.add(restaurant_pizzas)
    db.session.commit()
    print("Seeded databse") 