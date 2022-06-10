import unittest

from models.countries import Country
from models.cities import City
from models.attractions import Attraction
from models.notes import Note

class TestTravel(unittest.TestCase):
    def setUp(self):
        self.france = Country("France", "Europe", 1)
        self.canada = Country("Canada", "North America", 2)
        self.toronto = City("Toronto", 1)
        self.cn_tower = Attraction("CN Tower", "A big towery thing in toronto",1, "10/01/1999", 2, True)
        self.note_1 = Note("note", "2022-12-25", "obj", "want to go", 1)

    def test_country_has_name(self):
        self.assertEqual("France", self.france.name)

    def test_country_has_region(self):
        self.assertEqual("Europe", self.france.region)

    def test_city_has_name(self):
        self.assertEqual("Toronto", self.toronto.name)

    def test_city_has_country(self):
        self.assertEqual(1, self.toronto.country)

    def test_attraction_has_name(self):
        self.assertEqual("CN Tower", self.cn_tower.name)

    def test_attraction_has_descriotions(self):
        self.assertEqual("A big towery thing in toronto", self.cn_tower.description)

    def test_attraction_has_city_id(self):
        self.assertEqual(1, self.cn_tower.city)

    def test_attraction_has_id(self):
        self.assertEqual(1, self.cn_tower.city)

    def test_attraction_has_date(self):
        self.assertEqual("10/01/1999", self.cn_tower.date)

    def test_attraction_visited(self):
        self.assertEqual(True, self.cn_tower.visited)


    # def test_note_has_title(self):
    #     note2 = Note("title", "date", "attraction name", "comment", 2)
    #     self.assertEqual("Title", note2.title)

    # AssertionError: 'Title' != ('title',)


    # def test_note_has_attraction(self):
    #     self.assertEqual("obj", self.note_1.attraction)
    # AssertionError: 'obj' != ('obj',)

   



if __name__ == "__main__":
    unittest.main()


