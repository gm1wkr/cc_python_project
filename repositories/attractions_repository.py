from db.run_sql import run_sql
from models.cities import City
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
    id = result[0]['id']
    attraction.id = id



def select_all():
    attractions = []

    sql = "SELECT * FROM attractions"
    results = run_sql(sql)

    for row in results:
        city = city_repository.select(row['city_id'])
        attraction = Attraction(row['name'], row['description'], city, row['date'], row['id'])
        attractions.append(attraction)
    return attractions


def select(id):
    sql = "SELECT * FROM attractions WHERE id = %s"
    values = [id]
    row = run_sql(sql, values)[0]

    if row is not None:
        city = city_repository.select(row['city_id']) 
        attraction = Attraction(row['name'], row['description'], city, row['date'], row['id'], row['visited'])
    return attraction



def update(attraction):

    sql = """UPDATE attractions 
    SET (name, description, city_id, date, visited) = (%s, %s, %s, %s, %s) 
    WHERE id = %s
    """
    values = [
        attraction.name, 
        attraction.description, 
        attraction.city.id, 
        attraction.date, 
        attraction.visited, 
        attraction.id
        ]

    run_sql(sql, values)


def delete_all():
    sql = "DELETE FROM attractions"
    values = []
    run_sql(sql, values)


def delete(id):
    sql = "DELETE FROM attractions WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def get_number_of_attractions():
    sql = "SELECT count(*) from attractions"
    row = run_sql(sql)[0]
    if row[0] >= 1:
        return row[0]
    return None


def get_number_of_unvisited_attractions():
    sql = "SELECT count(*) from attractions"
    row = run_sql(sql)[0]
    if row[0] >= 1:
        return row[0]
    return None


def get_visited_attractions():
    attractions = []
    sql = "SELECT * from attractions WHERE visited IS TRUE"
    row = run_sql(sql)[0]
    results = run_sql(sql)
    for row in results:
        city = city_repository.select(row['city_id'])
        attraction = Attraction(row['name'], row['description'], city, row['date'], row['id'], row['visited'])
        attractions.append(attraction)
        
    return attractions


def get_unvisited_attractions():
    attractions = []
    sql = "SELECT * from attractions WHERE visited IS NOT TRUE"
    row = run_sql(sql)[0]
    results = run_sql(sql)
    for row in results:
        city = city_repository.select(row['city_id'])
        attraction = Attraction(row['name'], row['description'], city, row['date'], row['id'],row['visited'])
        attractions.append(attraction)

    return attractions
