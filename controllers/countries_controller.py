from flask import Blueprint, Flask, render_template, request, redirect

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
def show(id):
    found_country = country_repository.select(id)
    return render_template("countries/show.html", country=found_country)



# NEW 
# GET '/countries/new'


# CREATE



# EDIT



# UPDATE



# DELETE