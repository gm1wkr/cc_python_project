import unittest

from models.countries import Country
from models.cities import City
from models.attractions import Attraction

class TestTravel(unittest.TestCase):
    def setUp(self):
        self.france = Country("France", "Europe", 1)
        self.canada = Country("Canada", "North America", 2)
        self.toronto = City("Toronto", 1)
        self.cn_tower = Attraction("CN Tower", "A big towery thing in toronto",1, "10/01/1999", 2, True)


    def test_country_has_name(self):
        self.assertEqual("France", self.france.name)

    def test_country_has_region(self):
        self.assertEqual("Europe", self.france.region)

    def test_city_has_name(self):
        self.assertEqual("Toronto", self.toronto.name)

    def test_city_has_country(self):
        self.assertEqual(1, self.toronto.country_id)

    def test_attraction_has_name(self):
        self.assertEqual("CN Tower", self.cn_tower.name)

    def test_attraction_has_descriotions(self):
        self.assertEqual("A big towery thing in toronto", self.cn_tower.description)

    def test_attraction_has_city_id(self):
        self.assertEqual(1, self.cn_tower.city_id)

    def test_attraction_has_id(self):
        self.assertEqual(1, self.cn_tower.city_id)

    def test_attraction_has_date(self):
        self.assertEqual("10/01/1999", self.cn_tower.date)

    def test_attraction_visited(self):
        self.assertEqual(True, self.cn_tower.visited)