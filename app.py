from flask import Flask, render_template

from controllers.countries_controller import countries_blueprint
from controllers.cities_controller import cities_blueprint
from controllers.attractions_controller import attractions_blueprint
from controllers.notes_controller import notes_blueprint

import repositories.country_repository as country_repository
import repositories.city_repository as city_repository
import repositories.attractions_repository as attractions_repository
import repositories.notes_repository as notes_repository

app = Flask(__name__)

app.register_blueprint(countries_blueprint)
app.register_blueprint(cities_blueprint)
app.register_blueprint(attractions_blueprint)
app.register_blueprint(notes_blueprint)


@app.route("/")
def main():

    unvisited = attractions_repository.get_unvisited_attractions(),
    visited = attractions_repository.get_visited_attractions()
    stats = {
        "num_notes":notes_repository.get_number_of_notes(),
        "num_cities":city_repository.get_number_of_cities(),
        "num_countries":country_repository.get_number_of_countries()
    }

    return render_template("index.html", visited=visited, unvisited=unvisited, stats_dict=stats)

if __name__ == "__main__":
    app.run()