import unittest

import keepdelta as kd
from keepdelta.config import keys


class TestReservedNamesDict(unittest.TestCase):

    def test_from_conflict_to_normal_value(self):
        """
        Conflicting value in a dict receives change.
        """
        for key in keys:
            conflict = keys[key]
            old = {
                "key_1": conflict,
                "key_2": True,
            }
            new = {
                "key_1": "hello",
                "key_2": True,
            }
            delta = {
                "key_1": "hello",
            }
            self.assertEqual(kd.create(old, new), delta)
            self.assertEqual(kd.apply(old, delta), new)

    def test_from_normal_to_conflict_value(self):
        """
        A normal dict value is changed to a conflicting value.
        This operation is NOT allowed.
        """
        for key in keys:
            conflict = keys[key]
            old = {
                "key_1": "hello",
                "key_2": True,
            }
            new = {
                "key_1": conflict,
                "key_2": True,
            }
            with self.assertRaises(ValueError):
                kd.create(old, new)

    def test_change_type_from_conflict_to_normal_value(self):
        """
        Dict containing a conflicting value has format changed.
        This operation is NOT allowed.
        """
        for key in keys:
            conflict = keys[key]
            old = {
                "key_1": conflict,
                "key_2": True,
            }
            new = None
            with self.assertRaises(ValueError):
                kd.create(old, new)

    def test_change_type_from_normal_to_conflict_value(self):
        """
        Change format to a dict containing a conflicting value.
        This operation is NOT allowed.
        """
        for key in keys:
            conflict = keys[key]
            old = None
            new = {
                "key_1": conflict,
                "key_2": True,
            }
            with self.assertRaises(ValueError):
                kd.create(old, new)

    def test_from_conflict_to_normal_key(self):
        """
        Conflicting key in a dict receives a value change.
        This operation is NOT allowed.
        """
        for key in keys:
            conflict = keys[key]
            old = {
                conflict: "hello",
                "key_2": True,
            }
            new = {
                conflict: "world",
                "key_2": True,
            }
            with self.assertRaises(ValueError):
                kd.create(old, new)

    def test_from_normal_to_conflict_key(self):
        """
        Conflicting key in a dict is changed to a normal key.
        """
        for key in keys:
            conflict = keys[key]
            old = {
                conflict: "hello",
                "key_2": True,
            }
            new = {
                "key_1": "hello",
                "key_2": True,
            }
            delta = {
                "key_1": "hello",
                conflict: keys["delete"],
            }
            self.assertEqual(kd.create(old, new), delta)
            self.assertEqual(kd.apply(old, delta), new)


if __name__ == "__main__":
    unittest.main()