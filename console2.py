import pdb


# from models.attractions import Attraction
# from models.countries import Country
# from models.cities import City
# from models.notes import Note

import repositories.country_repository as country_repository




andorra = country_repository.country_name_exists('Andorra')
select_andora = country_repository.select_country_by_name('Andorra')
select_andora_id = country_repository.select(1)
# belgium = country_repository.country_name_exists('Belgium')



pdb.set_trace()
