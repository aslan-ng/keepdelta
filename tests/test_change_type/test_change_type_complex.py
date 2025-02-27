import unittest

import keepdelta as kd


class TestChangeTypeComplex(unittest.TestCase):

    def test_complex_to_bool(self):
        old = 1 + 1j
        new = True
        delta = True
        self.assertEqual(kd.create(old, new), delta)
        self.assertEqual(kd.apply(old, delta), new)

    def test_complex_to_float(self):
        old = 1 + 1j
        new = 1.1
        delta = 1.1
        self.assertEqual(kd.create(old, new), delta)
        self.assertEqual(kd.apply(old, delta), new)

    def test_complex_to_int(self):
        old = 1 + 1j
        new = 1
        delta = 1
        self.assertEqual(kd.create(old, new), delta)
        self.assertEqual(kd.apply(old, delta), new)

    def test_complex_to_str(self):
        old = 1 + 1j
        new = "hello"
        delta = "hello"
        self.assertEqual(kd.create(old, new), delta)
        self.assertEqual(kd.apply(old, delta), new)


if __name__ == "__main__":
    unittest.main()