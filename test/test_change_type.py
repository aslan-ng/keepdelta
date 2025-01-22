import unittest

import keepdelta as kd


class TestChangeTypeBool(unittest.TestCase):

    def test_bool_to_int(self):
        old = True
        new = 10
        delta = 10
        self.assertEqual(kd.create(old, new), delta)
        self.assertEqual(kd.apply(old, delta), new)

    def test_bool_to_float(self):
        old = True
        new = 10.1
        delta = 10.1
        self.assertEqual(kd.create(old, new), delta)
        self.assertEqual(kd.apply(old, delta), new)

    def test_bool_to_complex(self):
        old = True
        new = 10 + 10j
        delta = 10 + 10j
        self.assertEqual(kd.create(old, new), delta)
        self.assertEqual(kd.apply(old, delta), new)

    def test_bool_to_string(self):
        old = True
        new = 'hello'
        delta = 'hello'
        self.assertEqual(kd.create(old, new), delta)
        self.assertEqual(kd.apply(old, delta), new)


class TestChangeTypeComplex(unittest.TestCase):
    pass


class TestChangeTypeFloat(unittest.TestCase):

    def test_float_to_int(self):
        old = 10.1
        new = 11
        delta = 11
        self.assertEqual(kd.create(old, new), delta)
        self.assertEqual(kd.apply(old, delta), new)


class TestChangeTypeInt(unittest.TestCase):

    def test_int_to_bool(self):
        old = 10
        new = True
        delta = True
        self.assertEqual(kd.create(old, new), delta)
        self.assertEqual(kd.apply(old, delta), new)

    def test_int_to_float(self):
        old = 10
        new = 11.1
        delta = 11.1
        self.assertEqual(kd.create(old, new), delta)
        self.assertEqual(kd.apply(old, delta), new)


class TestChangeTypeStr(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()