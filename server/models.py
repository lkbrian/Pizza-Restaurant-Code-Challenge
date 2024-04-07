from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Restaurant(db.Model, SerializerMixin):
    __tablename__ = 'restaurants'
    serialize_rules=("-restaurant_pizzas.restaurant",)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    address =db.Column(db.String)

    # Relationship with Pizza through association table
    restaurant_pizzas = db.relationship('RestaurantPizza', back_populates='restaurant',cascade="all, delete-orphan")

    # Association proxy for accessing pizzas directly
    pizzas = association_proxy('restaurant_pizzas', 'pizza', creator=lambda pizza_obj: RestaurantPizza(pizza=pizza_obj))

    def __repr__(self):
        return f'<Restaurant => {self.name}>'


class Pizza(db.Model, SerializerMixin):
    __tablename__ = 'pizzas'
    serialize_rules=("-restaurant_pizzas.pizza",)
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    ingredients = db.Column(db.String)

    # Relationship with Restaurant through association table
    restaurant_pizzas = db.relationship('RestaurantPizza', back_populates='pizza',cascade="all, delete-orphan")

    # Association proxy for accessing restaurants directly
    restaurants = association_proxy('restaurant_pizzas', 'restaurant', creator=lambda rest_obj: RestaurantPizza(restaurant=rest_obj))
    
    def __repr__(self):
        return f'<Pizza => {self.name}>'

class RestaurantPizza(db.Model, SerializerMixin):
    __tablename__ = 'restaurantpizzas'
    serialize_rules=("-pizza.restaurant_pizzas","-restaurant.restaurant_pizzas")

    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'), nullable=False)
    price = db.Column(db.Float, nullable=False)

    # Relationship with Restaurant
    restaurant = db.relationship('Restaurant', back_populates='restaurant_pizzas')

    # Relationship with Pizza
    pizza = db.relationship('Pizza', back_populates='restaurant_pizzas')




