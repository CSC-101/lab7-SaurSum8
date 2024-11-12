import unittest
import convert

class TestCases(unittest.TestCase):
    def test_convert_1(self):
        t = 26532.4620
        self.assertEqual(t, convert.str_to_float(str(t)))

    def test_convert_2(self):
        self.assertEqual(None, convert.str_to_float("26532.4620.505.5"))

    def test_convert_3(self):
        self.assertEqual(None, convert.str_to_float("100,0"))

if __name__ == '__main__':
    unittest.main()
