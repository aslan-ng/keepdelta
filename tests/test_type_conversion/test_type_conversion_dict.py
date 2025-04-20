import unittest

import keepdelta as kd


class TestTypeConversionDict(unittest.TestCase):

    def test_none_to_dict(self):
        old = None
        new = {
            "str": "hello",
            "bool": True,
        }
        delta = {
            "str": "hello",
            "bool": True,
        }
        self.assertEqual(kd.create(old, new), delta)
        self.assertEqual(kd.apply(old, delta), new)

    def test_dict_to_none(self):
        old = {
            "str": "hello",
            "bool": True,
        }
        new = None
        delta = None
        self.assertEqual(kd.create(old, new), delta)
        self.assertEqual(kd.apply(old, delta), new)


if __name__ == "__main__":
    unittest.main()