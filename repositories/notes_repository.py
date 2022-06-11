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





def delete_all():
    sql = "DELETE FROM notes"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM notes WHERE id = %s"
    values = [id]
    run_sql(sql, values)


