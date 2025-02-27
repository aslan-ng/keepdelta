import unittest

import keepdelta as kd


class TestChangeTypeFloat(unittest.TestCase):

    def test_float_to_bool(self):
        old = 1.1
        new = True
        delta = True
        self.assertEqual(kd.create(old, new), delta)
        self.assertEqual(kd.apply(old, delta), new)

    def test_float_to_complex(self):
        old = 1.1
        new = 1 + 1j
        delta = 1 + 1j
        self.assertEqual(kd.create(old, new), delta)
        self.assertEqual(kd.apply(old, delta), new)

    def test_float_to_int(self):
        old = 1.1
        new = 1
        delta = 1
        self.assertEqual(kd.create(old, new), delta)
        self.assertEqual(kd.apply(old, delta), new)

    def test_float_to_str(self):
        old = 1.1
        new = "hello"
        delta = "hello"
        self.assertEqual(kd.create(old, new), delta)
        self.assertEqual(kd.apply(old, delta), new)


if __name__ == "__main__":
    unittest.main()