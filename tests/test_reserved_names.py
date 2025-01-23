import unittest

import keepdelta as kd
from keepdelta.config import keys


class TestReservedNamesPrimitives(unittest.TestCase):

    def test_str_0(self):
        old = keys['nothing']  # Conflict
        new = 'hello'
        delta = 'hello'
        self.assertEqual(kd.create(old, new), delta)
        self.assertEqual(kd.apply(old, delta), new)

    def test_str_1(self):
        old = 'hello'
        new = keys['nothing']  # Conflict
        delta = keys['nothing']  # Conflict
        with self.assertRaises(ValueError):
            self.assertEqual(kd.create(old, new), delta)
            self.assertEqual(kd.apply(old, delta), new)

    def test_str_2(self):
        """
        Change variable
        """
        old = None
        new = keys['nothing']  # Conflict
        delta = keys['nothing']  # Conflict
        with self.assertRaises(ValueError):
            self.assertEqual(kd.create(old, new), delta)
            self.assertEqual(kd.apply(old, delta), new)


class TestReservedNamesCollections(unittest.TestCase):

    def test_dict_0(self):
        old = {
            'str': keys['delete'],  # Conflict
            'bool': True,
        }
        new = {
            'str': 'hello',
            'bool': True,
        }
        delta = {
            'str': 'hello',
        }
        self.assertEqual(kd.create(old, new), delta)
        self.assertEqual(kd.apply(old, delta), new)

    def test_dict_1(self):
        old = {
            'str': 'hello',
            'bool': True,
        }
        new = {
            'str': keys['delete'],  # Conflict
            'bool': True,
        }
        delta = {
            'str': keys['delete'],  # Conflict
            'bool': True,
        }
        with self.assertRaises(ValueError):
            self.assertEqual(kd.create(old, new), delta)
            self.assertEqual(kd.apply(old, delta), new)

    def test_dict_2(self):
        """
        Rewrite None with conflicting dict
        """
        old = None
        new = {
            'str': keys['delete'],  # Conflict
            'bool': True,
        }
        delta = {
            'str': keys['delete'],  # Conflict
            'bool': True,
        }
        with self.assertRaises(ValueError):
            self.assertEqual(kd.create(old, new), delta)
            self.assertEqual(kd.apply(old, delta), new)

    def test_list_0(self):
        old = [
            keys['delete'],  # Conflict
            True,
        ]
        new = [
            'hello',
            True,
        ]
        delta = {
            0: 'hello',
        }
        self.assertEqual(kd.create(old, new), delta)
        self.assertEqual(kd.apply(old, delta), new)

    def test_list_1(self):
        old = [
            'hello',
            True,
        ]
        new = [
            keys['delete'],  # Conflict
            True,
        ]
        delta = {
            0: keys['delete'],  # Conflict
        }
        with self.assertRaises(ValueError):
            self.assertEqual(kd.create(old, new), delta)
            self.assertEqual(kd.apply(old, delta), new)


if __name__ == '__main__':
    unittest.main()