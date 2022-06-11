from flask import Blueprint, Flask, render_template, request, redirect

from models.cities import City
import repositories.city_repository as city_repository

cities_blueprint = Blueprint("cities", __name__)

# INDEX
# GET '/cities'
@cities_blueprint.route("/cities", methods=["GET"])
def cities():
    cities = city_repository.select_all()
    return render_template("cities/index.html", all_cities=cities)



# SHOW 
# GET '/cities/<id>'



# NEW 
# GET '/cities/new'


# CREATE



# EDIT



# UPDATE



# DELETE