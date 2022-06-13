from flask import Flask, render_template

from controllers.countries_controller import countries_blueprint
from controllers.cities_controller import cities_blueprint
from controllers.attractions_controller import attractions_blueprint
from controllers.notes_controller import notes_blueprint

import repositories.attractions_repository as attractions_repository

app = Flask(__name__)

app.register_blueprint(countries_blueprint)
app.register_blueprint(cities_blueprint)
app.register_blueprint(attractions_blueprint)
app.register_blueprint(notes_blueprint)


@app.route("/")
def main():

    unvisited = attractions_repository.get_unvisited_attractions(),
    visited = attractions_repository.get_visited_attractions()

    return render_template("index.html", visited=visited, unvisited=unvisited)

if __name__ == "__main__":
    app.run()