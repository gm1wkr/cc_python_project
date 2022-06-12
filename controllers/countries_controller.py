from flask import Blueprint, Flask, render_template, request, redirect

from models.countries_list import all_countries_list as list_of_all_countries
from models.countries import Country
import repositories.country_repository as country_repository

countries_blueprint = Blueprint("countries", __name__)

# INDEX
# GET '/countries'
@countries_blueprint.route("/countries", methods=["GET"])
def countries():
    countries = country_repository.select_all()
    return render_template("countries/index.html", all_countries=countries)

# SHOW 
# GET '/countries/<id>'
@countries_blueprint.route("/countries/<id>")
def show_countries(id):
    found_country = country_repository.select(id)
    return render_template("countries/show.html", country=found_country)



# NEW 
# GET '/countries/new'
@countries_blueprint.route("/countries/new")
def new_country():
    all_countries = country_repository.select_all()
    return render_template("countries/new.html", countries=all_countries, list_of_countries=list_of_all_countries)

# CREATE
# POST '/countries'
@countries_blueprint.route("/countries", methods=["POST"])
def create_country():
    # region = request.form['region']
    country = request.form['country']
    new_country = Country(country, None, None, None, None)
    new_country.region = new_country.get_country_by_name(country)['continent']
    new_country.capital = new_country.get_country_by_name(country)['capital']
    new_country.timezones = new_country.get_country_by_name(country)['timezones']
    new_country.code = new_country.get_country_by_name(country)['code']
    # `ADD timezone, capital code HERE, Model, Repository and SQL
    country_repository.save(new_country)
    return redirect("/countries")


# EDIT
# GET '/countries/<id>/edit'
@countries_blueprint.route("/countries/<id>/edit")
def edit_country(id):
    country = country_repository.select(id)
    all_countries = country_repository.select_all()
    return render_template("/countries/edit.html", current_country=country, countries=all_countries)


# UPDATE
@countries_blueprint.route("/countries/<id>", methods=["POST"])
def update_country(id):
    region = request.form['region']
    country = request.form['country']
    country_updated = Country(country, region, id)
    country_repository.update(country_updated)
    return redirect(f"/countries/{id}")


# DELETE
@countries_blueprint.route("/countries/<id>/delete", methods=["POST"])
def delete_country(id):
    country_repository.delete(id)
    return redirect("/countries")