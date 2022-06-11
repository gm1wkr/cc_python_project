from flask import Blueprint, Flask, render_template, request, redirect

from models.attractions import Attraction
import repositories.attractions_repository as attractions_repository

attractions_blueprint = Blueprint("attractions", __name__)

# INDEX
# GET '/attractions'
@attractions_blueprint.route("/attractions", methods=["GET"])
def attractions():
    attractions = attractions_repository.select_all()
    return render_template("attractions/index.html", all_attractions=attractions)



# SHOW 
# GET '/cities/<id>'



# NEW 
# GET '/cities/new'


# CREATE



# EDIT



# UPDATE



# DELETE