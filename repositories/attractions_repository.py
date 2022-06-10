from db.run_sql import run_sql
from models.countries import Country
from models.attractions import Attraction

import repositories.city_repository as city_repository


def save(attraction):
    sql = """INSERT INTO attractions (name, description, city_id, date) 
    VALUES (%s, %s,%s, %s)
    RETURNING id
    """
    
    values = [
        attraction.name, 
        attraction.description, 
        attraction.city.id, 
        attraction.date
    ]
    
    result = run_sql(sql, values);
    print(result)
    id = result[0]['id']
    attraction.id = id



def select_all():
    attractions = []

    sql = "SELECT * FROM attractions"
    results = run_sql(sql)

    for row in results:
        city = city_repository.select(row['city_id'])
        attraction = Attraction(row['name'], row['description'], city, "", row['id'])
        attractions.append(attraction)
    return attractions


def select(id):
    pass


def update():
    pass


def delete_all():
    pass


def delete(id):
    pass
