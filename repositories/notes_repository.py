from db.run_sql import run_sql
from models.attractions import Attraction
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
