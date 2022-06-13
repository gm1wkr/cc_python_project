from db.run_sql import run_sql
from models.countries import Country
from models.cities import City
import repositories.country_repository as country_repository

def save(city):
    sql = "INSERT INTO cities (name, country_id) VALUES (%s, %s) RETURNING id"
    values = [city.name, city.country.id]
    result = run_sql(sql, values)
    id = result[0]['id']
    city.id = id
    return city


def select_all():
    cities = []

    sql = "SELECT * FROM cities"
    results = run_sql(sql)

    for row in results:
        country = country_repository.select(row['country_id'])
        city = City(row['name'], country, row['id'])
        cities.append(city)
    return cities


def select(id):
    city = None
    sql = "SELECT * FROM cities where id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    country = country_repository.select(result['country_id'])
    if result is not None:
        city = City(result['name'], country, result['id'])
    return city



def update(city):
    sql = "UPDATE cities SET (name, country_id) = (%s, %s) WHERE id = %s"
    values = [city.name, city.country.id, city.id]
    run_sql(sql, values)


def delete_all():
    sql = "DELETE FROM cities"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM cities WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def get_number_of_cities():
    sql = "SELECT count(*) from cities"
    row = run_sql(sql)[0]
    if row[0] >= 1:
        return row[0]
    return None
