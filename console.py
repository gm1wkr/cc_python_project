import pdb


from models.attractions import Attraction
from models.countries import Country
from models.cities import City
from models.notes import Note

import repositories.country_repository as country_repository
import repositories.city_repository as city_repository
import repositories.attractions_repository as attractions_repository
import repositories.notes_repository as notes_repository



# # COUNTRIES
# country_repository.delete_all()
# scotland = Country("Scotland", "UK",None, None, None)
# country_repository.save(scotland)
# wales = Country("Wales", "UK",None, None, None)
# country_repository.save(wales)
# country_list = country_repository.select_all()



# # CITIES
# city_1 = City("Edinboro", scotland,)
# city_repository.save(city_1)
# city_2 = City("Glasgow", scotland)
# city_repository.save(city_2)

# city_1_updated = City("Edinburgh", scotland, city_1.id)
# city_repository.update(city_1_updated)
# city_1_select = city_repository.select(city_1.id)
# city_repository.delete(city_1.id)
# city_list = city_repository.select_all()



# # ATTRACTIONS
# datetime_now = "2022-04-26"
# attraction_1 = Attraction("CodeClan HQ", "CodeClan HQ is must visit", city_2, datetime_now)
# attractions_repository.save(attraction_1)
# attraction_2 = Attraction("Glasgow Hydro", "Things really happen here and they are groovy", city_2, datetime_now)
# attractions_repository.save(attraction_2)
# attraction_2_id = attractions_repository.select(city_2.id)
# attraction_1_updated = Attraction("CodeClan_ HQ", "Yay, CodeClan HQ is must visit", city_2, datetime_now, attraction_1.id, True)
# # attractions_repository.delete(attraction_1.id)
# # attractions_repository.delete_all()
# attraction_list = attractions_repository.select_all()



# # NOTES
# notes_repository.delete_all()
# notes_list_after_delete = notes_repository.select_all()
# note_1 = Note("note", "2022-01-01", attraction_2, "the note")
# notes_repository.save(note_1)
# note_2 = Note("note 2", "2022-01-01", attraction_2, "Visit the CodeClan_ world HQ")
# notes_repository.save(note_2)
# notes_list = notes_repository.select_all()

# note_2_updated = Note("CC_ HQ", "2022-02-02", attraction_2, "Amazing CodeClan_ World HQ", note_2.id)
# notes_repository.update(note_2_updated)
# note_2_select = notes_repository.select(note_2.id)


pdb.set_trace()
