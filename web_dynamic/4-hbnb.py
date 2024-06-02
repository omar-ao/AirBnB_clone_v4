#!/usr/bin/python3
"""
Builds a Flask App that integrates with AirBnB static HTML Template
"""
from flask import Flask, render_template, url_for
from models import storage
import uuid;

# Setup Flask
app = Flask(__name__)
app.url_map.strict_slashes = False
port = 5000
host = '0.0.0.0'


# lauch flask page rendering
@app.teardown_appcontext
def teardown_db(exception):
    """
    This method calls .close() (i.e. .remove()) on
    the SQLAlchemy current Session After each request.
    """
    storage.close()


@app.route('/4-hbnb')
def hbnb_filters(the_id=None):
    """
    Handles custom template with states, cities & amentities requests
    """
    state_objs = storage.all('State').values()
    states = dict([state.name, state] for state in state_objs)
    amens = storage.all('Amenity').values()
    places = storage.all('Place').values()
    users = dict([user.id, "{} {}".format(user.first_name, user.last_name)]
                 for user in storage.all('User').values())
    return render_template('4-hbnb.html',
                           cache_id=uuid.uuid4(),
                           states=states,
                           amenity=amenity,
                           places=places,
                           users=users)

if __name__ == "__main__":
    """
    Run Main Flask App"""
    app.run(host=host, port=port)
