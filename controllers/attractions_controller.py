from flask import Blueprint, Flask, render_template, request, redirect

from models.attractions import Attraction
import repositories.attractions_repository as attractions_repository
import repositories.city_repository as city_repository

attractions_blueprint = Blueprint("attractions", __name__)

# INDEX
# GET '/attractions'
@attractions_blueprint.route("/attractions", methods=["GET"])
def attractions():
    attractions = attractions_repository.select_all()
    return render_template("attractions/index.html", all_attractions=attractions)



# SHOW 
# GET '/attractions/<id>'
@attractions_blueprint.route("/attractions/<id>")
def show_attraction(id):
    found_attraction = attractions_repository.select(id)
    return render_template("attractions/show.html", attraction = found_attraction)



# NEW 
# GET '/attractions/new'
@attractions_blueprint.route("/attractions/new", methods=["GET"])
def add_attraction():
    cities = city_repository.select_all()
    return render_template("attractions/new.html", all_cities=cities)



# CREATE
# POST '/attractions'
@attractions_blueprint.route("/attractions", methods=["POST"])
def create_attraction():
    name = request.form['name']
    city_id = request.form['city_id']
    date = request.form['date']
    description = request.form['description']
    city = city_repository.select(city_id)
    new_attraction = Attraction(name, description, city, date, None, False)
    attractions_repository.save(new_attraction)
    return redirect("/attractions")





# EDIT
# GET '/attractions/<id>/edit'
@attractions_blueprint.route("/attractions/<id>/edit", methods=["GET"])
def edit_attraction(id):
    attraction = attractions_repository.select(id)
    cities = city_repository.select_all()
    return render_template("/attractions/edit.html", attraction=attraction, all_cities=cities)


# UPDATE
# POST '/attractions/<id>'
@attractions_blueprint.route("/attractions/<id>", methods=["POST"])
def update_attraction(id):
    name = request.form['name']
    city_id = request.form['city_id']
    date = request.form['date']
    description = request.form['description']
    visited = request.form['visited']
    city = city_repository.select(city_id)
    new_attraction = Attraction(name, description, city, date, id, visited)
    attractions_repository.update(new_attraction)
    print(new_attraction)
    return redirect(f"/attractions/{id}")



# DELETE
@attractions_blueprint.route("/attractions/<id>/delete", methods=["POST"])
def delete_attraction(id):
    attractions_repository.delete(id)
    return redirect("/attractions")