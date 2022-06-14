from itertools import count
from flask import Blueprint, Flask, render_template, request, redirect

from models.cities import City
from models.countries import Country
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository
import repositories.attractions_repository as attractions_repository
from models.countries_list import all_countries_list as list_of_all_countries

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
    found_attractions = attractions_repository.attractions_by_city(id)
    return render_template("cities/show.html", city=found_city, attractions=found_attractions)


# NEW 
# GET '/cities/new'
@cities_blueprint.route("/cities/new")
def new_city():
    all_countries = country_repository.select_all()
    return render_template("cities/new.html",countries=all_countries ,list_of_countries=list_of_all_countries)

# CREATE
# POST '/cities'
@cities_blueprint.route("/cities", methods=["POST"])
def create_city():
    country = request.form['country']
    city = request.form['city']

    # country_exists = country_repository.country_name_exists(country)
    # if not country_exists:
        # create country
    new_country = Country(country, None, None, None, None)
    new_country.region = new_country.get_country_by_name(country)['continent']
    new_country.capital = new_country.get_country_by_name(country)['capital']
    new_country.timezones = new_country.get_country_by_name(country)['timezones']
    new_country.code = new_country.get_country_by_name(country)['code']
    new_country = country_repository.save(new_country)
    
    new_city = City(city, new_country)
    city_repository.save(new_city)
        
    return redirect("/cities")



# EDIT
@cities_blueprint.route("/cities/<id>/edit", methods=["GET"])
def edit_city(id):
    city = city_repository.select(id)
    countries = country_repository.select_all()
    return render_template("/cities/edit.html", city=city, countries=countries)


# UPDATE
@cities_blueprint.route("/cities/<id>", methods=["POST"])
def update_city(id):
    city_name = request.form['city']
    country = request.form['country']
    new_country = Country(country, None, None, None, None)
    new_country.region = new_country.get_country_by_name(country)['continent']
    new_country.capital = new_country.get_country_by_name(country)['capital']
    new_country.timezones = new_country.get_country_by_name(country)['timezones']
    new_country.code = new_country.get_country_by_name(country)['code']
    new_country = country_repository.save(new_country)

    city = city_repository.select(city_id)
    new_city = City(city_name, new_country, id)
    city_repository.update(new_city)
    return redirect(f"/cities/{id}")


# DELETE 
@cities_blueprint.route("/cities/<id>/delete", methods=["POST"])
def delete_city(id):
    city_repository.delete(id)
    return redirect("/cities")