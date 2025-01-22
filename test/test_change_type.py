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
        new = 'hello'
        delta = 'hello'
        self.assertEqual(kd.create(old, new), delta)
        self.assertEqual(kd.apply(old, delta), new)


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
        new = 'hello'
        delta = 'hello'
        self.assertEqual(kd.create(old, new), delta)
        self.assertEqual(kd.apply(old, delta), new)


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
        new = 'hello'
        delta = 'hello'
        self.assertEqual(kd.create(old, new), delta)
        self.assertEqual(kd.apply(old, delta), new)


class TestChangeTypeInt(unittest.TestCase):

    def test_int_to_bool(self):
        old = 1
        new = True
        delta = True
        self.assertEqual(kd.create(old, new), delta)
        self.assertEqual(kd.apply(old, delta), new)

    def test_int_to_complex(self):
        old = 1
        new = 1 + 1j
        delta = 1 + 1j
        self.assertEqual(kd.create(old, new), delta)
        self.assertEqual(kd.apply(old, delta), new)

    def test_int_to_float(self):
        old = 1
        new = 1.1
        delta = 1.1
        self.assertEqual(kd.create(old, new), delta)
        self.assertEqual(kd.apply(old, delta), new)

    def test_int_to_str(self):
        old = 1
        new = 'hello'
        delta = 'hello'
        self.assertEqual(kd.create(old, new), delta)
        self.assertEqual(kd.apply(old, delta), new)


class TestChangeTypeStr(unittest.TestCase):
    
    def test_str_to_bool(self):
        old = 'hello'
        new = True
        delta = True
        self.assertEqual(kd.create(old, new), delta)
        self.assertEqual(kd.apply(old, delta), new)

    def test_str_to_complex(self):
        old = 'hello'
        new = 1 + 1j
        delta = 1 + 1j
        self.assertEqual(kd.create(old, new), delta)
        self.assertEqual(kd.apply(old, delta), new)

    def test_str_to_float(self):
        old = 'hello'
        new = 1.1
        delta = 1.1
        self.assertEqual(kd.create(old, new), delta)
        self.assertEqual(kd.apply(old, delta), new)

    def test_str_to_int(self):
        old = 'hello'
        new = 1
        delta = 1
        self.assertEqual(kd.create(old, new), delta)
        self.assertEqual(kd.apply(old, delta), new)


if __name__ == '__main__':
    unittest.main()