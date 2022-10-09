import unittest
from main import Perevod


class TestPerevod(unittest.TestCase):
    def setUp(self):
        self.per = Perevod()

    def test_FutVMetr(self):
        self.assertEqual(self.per.FutVMetr(1), 0.3)

    def test_DumVMetr(self):
        self.assertEqual(self.per.DumVMetr(1), 0.025)


if __name__ == "__main__":
    unittest.main()
