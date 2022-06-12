DROP TABLE IF EXISTS notes;
DROP TABLE IF EXISTS countries;
DROP TABLE IF EXISTS cities;
DROP TABLE IF EXISTS attractions;

CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    region VARCHAR(255),
    capital VARCHAR(255),
    timezones VARCHAR(255),
    code VARCHAR(255)
);


CREATE TABLE cities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    country_id INT REFERENCES countries(id) ON DELETE CASCADE
);



CREATE TABLE attractions (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description VARCHAR(255),
    city_id INT REFERENCES cities(id) ON DELETE CASCADE,
    date DATE,
    visited BOOLEAN
);


CREATE TABLE notes(
    id SERIAL PRIMARY KEY,
    date DATE,
    title VARCHAR(255),
    attraction_id INT REFERENCES attractions(id),
    description TEXT
);

