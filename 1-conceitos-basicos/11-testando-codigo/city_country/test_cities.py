"""
# Descrição

Arquivo relacionado à atividade 11.1 da parte 1.
"""

import unittest

from city_functions import address

class TestAddress(unittest.TestCase):

    def test_address(self):
        city = "santiago"
        country = "chile"
        
        self.assertEqual(address(city, country), "Santiago, Chile")


if __name__ == "__main__":
    unittest.main()