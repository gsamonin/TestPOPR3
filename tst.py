import unittest
from main import Perevod


class TestPerevod(unittest.TestCase):
    def setUp(self):
        self.per = Perevod()

    def test_FutVMetr(self):
        self.assertEqual(self.per.FutVMetr(1), 0.3)

    def test_DumVMetr(self):
        self.assertEqual(self.per.DumVMetr(1), 0.025)

    def test_YardVMetr(self):
        self.assertEqual(self.per.YardVMetr(1), 0.91)

    def test_VershVMetr(self):
        self.assertEqual(self.per.VershVMetr(1), 0.044)

    def test_PyadVMetr(self):
        self.assertEqual(self.per.PyadVMetr(1), 0.18)

if __name__ == "__main__":
    unittest.main()
