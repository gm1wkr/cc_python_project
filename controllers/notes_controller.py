from flask import Blueprint, Flask, render_template, request, redirect

from models.notes import Note
from models.attractions import Attraction
import repositories.notes_repository as notes_repository
import repositories.attractions_repository as attractions_repository

notes_blueprint = Blueprint("notes", __name__)

# INDEX
# GET '/notes'
@notes_blueprint.route("/notes", methods=["GET"])
def notes():
    notes = notes_repository.select_all()
    return render_template("notes/index.html", all_notes=notes)



# SHOW 
# GET '/notes/<id>'
@notes_blueprint.route("/notes/<id>")
def show_note(id):
    found_note = notes_repository.select(id)
    return render_template("notes/show.html", note=found_note)




# GET '/notes/new/<attraction_id>'
@notes_blueprint.route("/notes/new/<attraction_id>", methods=["GET"])
def add_note_to_attraction(attraction_id):
    attraction = attractions_repository.select(attraction_id)
    return render_template("notes/new.html", attraction=attraction)


# NEW 
# GET '/notes/new'
@notes_blueprint.route("/notes/new", methods=["GET"])
def new_note():
    attractions = attractions_repository.select_all()
    return render_template("notes/new.html", all_attractions=attractions)

# CREATE
@notes_blueprint.route("/notes", methods=["POST"])
def create_note():
    title = request.form['title']
    attraction_id = request.form['attraction_id']
    date = request.form['date']
    description = request.form['description']
    attraction = attractions_repository.select(attraction_id)
    new_note = Note(title, date, attraction, description)
    notes_repository.save(new_note)
    return redirect("/notes")


# EDIT
@notes_blueprint.route("/notes/<id>/edit", methods=["GET"])
def edit_note(id):
    note = notes_repository.select(id)
    attractions = attractions_repository.select_all()
    return render_template("/notes/edit.html", note=note, all_attractions=attractions)



# UPDATE
@notes_blueprint.route("/notes/<id>", methods=["POST"])
def update_attraction(id):
    title = request.form['title']
    attraction_id = request.form['attraction_id']
    date = request.form['date']
    description = request.form['description']
    attraction = attractions_repository.select(attraction_id)
    new_note = Note(title, date, attraction, description, id)
    notes_repository.update(new_note)

    return redirect(f"/notes")


# DELETE
# POST '/notes/<id>/delete'
@notes_blueprint.route("/notes/<id>/delete", methods=["POST"])
def delete_attraction(id):
    notes_repository.delete(id)
    return redirect("/notes")