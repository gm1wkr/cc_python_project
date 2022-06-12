from db.run_sql import run_sql
from models.countries import Country


def save(country):
    sql = """INSERT INTO countries (name, region, capital, timezones, code) 
    VALUES (%s, %s, %s, %s, %s) 
    RETURNING id
    """
    values = [country.name, 
        country.region, 
        country.capital, 
        country.timezones[0], 
        country.code
        ]
    result = run_sql(sql, values)
    id = result[0]['id']
    country.id = id
    return country


def select_all():
    countries = []

    sql = "SELECT * FROM countries"
    results = run_sql(sql)

    for row in results:
        country = Country(row['name'],row['region'], row['capital'], row['timezones'],row['code'], row['id'])
        countries.append(country)
    return countries


def select(id):
    country = None
    sql = "SELECT * FROM countries where id = %s"
    values = [id]
    row = run_sql(sql, values)[0]
    if row is not None:
        country = Country(row['name'], row['region'], row['capital'], row['timezones'],row['code'], row['id'])
    return country


def select_city_by_name(name):
    country = None
    sql = "SELECT * FROM countries where name = %s"
    values = [name]
    row = run_sql(sql, values)[0]
    if row is not None:
        country = Country(row['name'], row['region'], row['capital'], row['timezones'],row['code'], row['id'])
    return country



def update(country):
    sql = """UPDATE countries 
    SET (name, region, capital, timezones, code) = (%s, %s, %s, %s, %s, %s) 
    WHERE id = %s
    """
    values = [country.name, 
        country.region, 
        country.capital, 
        country.timezones, 
        country.code,
        country.id
        ]
    run_sql(sql, values)


def delete_all():
    sql = "DELETE FROM countries"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM countries WHERE id = %s"
    values = [id]
    run_sql(sql, values)

