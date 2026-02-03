"""
# Descrição

Arquivo relacionado à atividade 11.2 da parte 1.
"""

import unittest

from city_functions import city_country

class TestAddress(unittest.TestCase):

    def setUp(self):
        self.city = "santiago"
        self.country = "chile"
        self.population = 5_000_000

    def test_city_country(self):
        self.assertEqual(
            city_country(self.city, self.country), "Santiago, Chile"
        )
    
    def test_city_country_population(self):
        self.assertEqual(
            city_country(self.city, self.country, population=self.population),
            "Santiago, Chile - população 5000000"
        )


if __name__ == "__main__":
    unittest.main()