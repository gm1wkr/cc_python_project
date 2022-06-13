from db.run_sql import run_sql
from models.attractions import Attraction
from models.notes import Note
import repositories.attractions_repository as attractions_repository

def save(note):
    sql = """INSERT INTO notes (date, title, attraction_id, description)
    VALUES (%s, %s, %s, %s)
    RETURNING id
    """
    values = [note.date, note.title, note.attraction.id, note.description]
    result = run_sql(sql, values)
    note.id = result[0]['id']

    return note


def select_all():
    notes = []

    sql = "SELECT * FROM notes"
    results = run_sql(sql)

    for row in results:
        note = Note(
        row['title'],
        row['date'], 
        row['attraction_id'],
        row['description'],
        row['id']
        )

        notes.append(note)

    return notes


def select(id):
    note = None
    sql = "SELECT * FROM notes WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    attraction = attractions_repository.select(result['attraction_id'])
    if result is not None:
        note = Note(
            result['title'],
            result['date'],
            attraction,
            result['description'],
            result['id']
        )
    return note
    


def update(note):
    sql = """UPDATE notes 
    SET (date, title, attraction_id, description) = (%s, %s, %s, %s)
    WHERE id = %s
    """
    values = [
        note.date,
        note.title,
        note.attraction.id,
        note.description,
        note.id
    ]
    run_sql(sql, values)


def delete_all():
    sql = "DELETE FROM notes"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM notes WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def get_number_of_notes():
    sql = "SELECT count(*) from notes"
    row = run_sql(sql)[0]
    if row[0] >= 1:
        return row[0]
    return None
