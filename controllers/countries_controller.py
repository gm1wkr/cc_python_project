from flask import Blueprint, Flask, render_template, request, redirect

from models.countries import Country
import repositories.country_repository as country_repository

countries_blueprint = Blueprint("countries", __name__)

# INDEX
# GET '/countries'
@countries_blueprint.route("/countries", methods=["GET"])
def countries():
    countries = country_repository.select_all()
    return render_template("countries/index.html")

# SHOW 
# GET '/countries/<id>'



# NEW 
# GET '/countries/new'


# CREATE



# EDIT



# UPDATE



# DELETE