from flask import Blueprint, Flask, render_template, request, redirect

from models.notes import Note
import repositories.notes_repository as notes_repository

notes_blueprint = Blueprint("notes", __name__)

# INDEX
# GET '/notes'
@notes_blueprint.route("/notes", methods=["GET"])
def notes():
    notes = notes_repository.select_all()
    return render_template("notes/index.html", all_notes=notes)



# SHOW 
# GET '/cities/<id>'



# NEW 
# GET '/cities/new'


# CREATE



# EDIT



# UPDATE



# DELETE