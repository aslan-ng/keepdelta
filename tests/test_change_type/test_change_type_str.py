import unittest

import keepdelta as kd


class TestChangeTypeStr(unittest.TestCase):

    def test_str_to_bool(self):
        old = "hello"
        new = True
        delta = True
        self.assertEqual(kd.create(old, new), delta)
        self.assertEqual(kd.apply(old, delta), new)

    def test_str_to_complex(self):
        old = "hello"
        new = 1 + 1j
        delta = 1 + 1j
        self.assertEqual(kd.create(old, new), delta)
        self.assertEqual(kd.apply(old, delta), new)

    def test_str_to_float(self):
        old = "hello"
        new = 1.1
        delta = 1.1
        self.assertEqual(kd.create(old, new), delta)
        self.assertEqual(kd.apply(old, delta), new)

    def test_str_to_int(self):
        old = "hello"
        new = 1
        delta = 1
        self.assertEqual(kd.create(old, new), delta)
        self.assertEqual(kd.apply(old, delta), new)


if __name__ == "__main__":
    unittest.main()