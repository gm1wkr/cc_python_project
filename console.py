import pdb
from models.attractions import Attraction

from models.countries import Country
from models.cities import City
import repositories.country_repository as country_repository
import repositories.city_repository as city_repository
import repositories.attractions_repository as attractions_repository

country_repository.delete_all()
scotland = Country("Scotland", "UK")
country_repository.save(scotland)

wales = Country("Wales", "UK")
country_repository.save(wales)

country_list = country_repository.select_all()


city_1 = City("Edinboro", scotland)
city_repository.save(city_1)

city_2 = City("Glasgow", scotland)
city_repository.save(city_2)



city_1_updated = City("Edinburgh", scotland, city_1.id)
city_repository.update(city_1_updated)

city_1_select = city_repository.select(city_1.id)

city_repository.delete(city_1.id)
city_list = city_repository.select_all()


attraction_1 = Attraction("CodeClan HQ", "CodeClan HQ is must visit", city_2, "")
attractions_repository.save(attraction_1)
attraction_2 = Attraction("Glasgow Hydro", "Things really happen here and they are groovy", city_2, "")
attractions_repository.save(attraction_2)
attraction_list = attractions_repository.select_all()



pdb.set_trace()
