import pdb


# from models.attractions import Attraction
# from models.countries import Country
# from models.cities import City
# from models.notes import Note

import repositories.country_repository as country_repository
import repositories.city_repository as city_repository
import repositories.attractions_repository as attractions_repository
import repositories.notes_repository as notes_repository




andorra = country_repository.country_name_exists('Andorra')
select_andora = country_repository.select_country_by_name('Andorra')
select_andora_id = country_repository.select(1)
# belgium = country_repository.country_name_exists('Belgium')

num_notes = notes_repository.get_number_of_notes()
num_cities = city_repository.get_number_of_cities()
num_countries = country_repository.get_number_of_countries()
num_attractions = attractions_repository.get_number_of_attractions()
visited_attractions = attractions_repository.get_visited_attractions()
unvisited_attractions = attractions_repository.get_unvisited_attractions()


for visited in visited_attractions:
    print(visited)

pdb.set_trace()
