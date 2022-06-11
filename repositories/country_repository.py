from db.run_sql import run_sql
from models.countries import Country


def save(country):
    sql = "INSERT INTO countries (name, region) VALUES (%s, %s) RETURNING id"
    values = [country.name, country.region]
    result = run_sql(sql, values)
    id = result[0]['id']
    country.id = id
    return country


def select_all():
    countries = []

    sql = "SELECT * FROM countries"
    results = run_sql(sql)

    for row in results:
        country = Country(row['name'], row['region'], row['id'])
        countries.append(country)
    return countries


def select(id):
    country = None
    sql = "SELECT * FROM countries where id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        country = Country(result['name'], result['region'] ,result['id'])
    return country



def update(country):
    sql = "UPDATE countries set (name, region) = (%s, %s) WHERE id = %s"
    values = [country.name, country.region, country.id]
    run_sql(sql, values)


def delete_all():
    sql = "DELETE FROM countries"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM countries WHERE id = %s"
    values = [id]
    run_sql(sql, values)

