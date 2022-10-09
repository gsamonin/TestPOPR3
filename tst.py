import unittest
from main import Perevod

class TestPerevod(unittest.TestCase):
    def setUp(self):
        self.per = Perevod()

    def test_FutVMetr(self):
        self.assertEqual(self.per.FutVMetr(1), 0.3)

if __name__ == "__main__":
    unittest.main()