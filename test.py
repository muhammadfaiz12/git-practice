import unittest
from logic import *

class TestLogicMethods(unittest.TestCase):

    def test_total_bus(self):
        self.assertEqual(calculate_total_bus_stop(["JKT", "YK"]), 6)

    def test_isupper(self):
        self.assertEqual(calculate_total_bus_stop(["JKT", "HEL"]), 5)

if __name__ == '__main__':
    unittest.main()