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
@cities_blueprint.route("/cities/<id>")
def show_cities(id):
    found_city = city_repository.select(id)
    return render_template("cities/show.html", city=found_city)


# NEW 
# GET '/cities/new'
@cities_blueprint.route("/cities/new")
def new_city():
    return render_template("cities/new.html")

# CREATE
# POST '/cities'
@cities_blueprint.route("/cities", methods=["POST"])
def create_city():
    region = request.form['region']
    city = request.form['city']
    new_city = city(city, region)
    city_repository.save(new_city)
    return redirect("/cities")



# EDIT



# UPDATE



# DELETE 
@cities_blueprint.route("/cities/<id>/delete", methods=["POST"])
def delete_city(id):
    city_repository.delete(id)
    return redirect("/cities")