import unittest

import keepdelta as kd


class TestChangeTypeBool(unittest.TestCase):

    def test_bool_to_complex(self):
        old = True
        new = 1 + 1j
        delta = 1 + 1j
        self.assertEqual(kd.create(old, new), delta)
        self.assertEqual(kd.apply(old, delta), new)

    def test_bool_to_float(self):
        old = True
        new = 10.1
        delta = 10.1
        self.assertEqual(kd.create(old, new), delta)
        self.assertEqual(kd.apply(old, delta), new)

    def test_bool_to_int(self):
        old = True
        new = 10
        delta = 10
        self.assertEqual(kd.create(old, new), delta)
        self.assertEqual(kd.apply(old, delta), new)

    def test_bool_to_str(self):
        old = True
        new = "hello"
        delta = "hello"
        self.assertEqual(kd.create(old, new), delta)
        self.assertEqual(kd.apply(old, delta), new)


if __name__ == "__main__":
    unittest.main()