import unittest

import keepdelta as kd


class TestTypeConversionNone(unittest.TestCase):

    def test_none_to_bool(self):
        old = None
        new = True
        delta = True
        self.assertEqual(kd.create(old, new), delta)
        self.assertEqual(kd.apply(old, delta), new)

    def test_none_to_complex(self):
        old = None
        new = 1 + 1j
        delta = 1 + 1j
        self.assertEqual(kd.create(old, new), delta)
        self.assertEqual(kd.apply(old, delta), new)

    def test_none_to_float(self):
        old = None
        new = 1.1
        delta = 1.1
        self.assertEqual(kd.create(old, new), delta)
        self.assertEqual(kd.apply(old, delta), new)

    def test_none_to_int(self):
        old = None
        new = 1
        delta = 1
        self.assertEqual(kd.create(old, new), delta)
        self.assertEqual(kd.apply(old, delta), new)

    def test_none_to_str(self):
        old = None
        new = "hello"
        delta = "hello"
        self.assertEqual(kd.create(old, new), delta)
        self.assertEqual(kd.apply(old, delta), new)


if __name__ == "__main__":
    unittest.main()