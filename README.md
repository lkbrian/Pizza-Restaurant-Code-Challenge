# Pizza-Restaurant-Code-Challenge

I have the models in a `models.py` file containing the three required models
instanciate the database and API routes in the `app.py` .seeding the database
happens in the `seed.py`

#### Model intialization
Created three classes Restaurant,Pizza,RestaurantPizzas used to instansiate database
tables for a many to many relationship through the use of an assisiation table 

Serialization is implemented in these classes to provide a convenient way to convert the objects
into JSON format. This is achieved using the SerializerMixin provided by SQLAlchemy, which helps in
serializing the objects and their relationships.

Association proxy is utilized in the Restaurant and Pizza classes to provide a simplified 
for accessing related objects. It allows direct access to the associated objects without explicitly 
manipulating the intermediate table.

#### Set Up Routes:
Defined routes to handle various HTTP requests according to the specifications 
provided in the challenge.
```python
@app.route('/restaurants',)
def restaurants():
    restaurants = [restaurant.to_dict() for restaurant in Restaurant.query.all()]
    return make_response(restaurants,200)
```
The following routes are available in the application:

- `GET /restaurants`: Retrieves a list of all restaurants.
- `GET /restaurants/<id>`: Retrieves details of a specific restaurant by ID.
- `DELETE /restaurants/<id>`: Deletes a restaurant by ID.
- `GET /pizzas`: Retrieves a list of all pizzas.
- `POST /restaurant_pizzas`: Creates a new restaurant pizza relationship.

After creating the virtual environment get into the environment & run
```bash
pip install -r requirements.txt
```

 To access the API  run 
```bash
cd server
flask db init
flask db migrate
flask db upgrade
python seed.py
python app.py 
```