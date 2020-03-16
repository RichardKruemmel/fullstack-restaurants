from flask import Flask, jsonify
app = Flask(__name__)


# define what to do when the user navigates to "/"
# this could also be served by nginx as a static index.html file.
@app.route('/')
def index():
    content = '<h2>this is a magical full-stack website</h2>'
    return content


# our mock data - like what we could get from a database
restaurants = [
    {'id': 0,
    'name':'Sotto',
    'neighobrhood':'Wedding'
    }, 
    {'id': 1,
    'name':'Curry 36',
    'neighobrhood':'Kreuzberg'
    }
]

@app.route('/api/restaurants/all',  methods=['GET'])
def api_restaurants_all():
    return jsonify(restaurants)

@app.route('/api/restaurants/names',  methods=['GET'])
def api_restaurants_names():
    # create a new list
    restaurant_names = []
    # loop through the data, adding the names of each restaurant to our new list 
    for restaurant in restaurants: 
        restaurant_names.append(restaurant['name'])
    return jsonify(restaurant_names)


# execute 
app.run()