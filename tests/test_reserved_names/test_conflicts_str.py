import unittest

import keepdelta as kd
from keepdelta.config import keys


class TestReservedNamesStr(unittest.TestCase):

    def test_from_conflict_to_normal(self):
        """
        Change a conflicting variable to a normal variable.
        """
        for key in keys:
            conflict = keys[key]
            old = conflict
            new = "hello"
            delta = "hello"
            self.assertEqual(kd.create(old, new), delta)
            self.assertEqual(kd.apply(old, delta), new)

    def test_from_normal_to_conflict(self):
        """
        Change a normal variable to a conflicting variable.
        This operation is NOT allowed.
        """
        for key in keys:
            conflict = keys[key]
            old = "hello"
            new = conflict
            with self.assertRaises(ValueError):
                kd.create(old, new)

    def test_change_type_from_conflict_to_normal(self):
        """
        Change a conflicting variable to a normal variable with type change.
        This operation is NOT allowed.
        """
        for key in keys:
            conflict = keys[key]
            old = None
            new = conflict
            with self.assertRaises(ValueError):
                kd.create(old, new)
    
    def test_change_type_from_normal_to_conflict(self):
        """
        Change a normal variable to a conflicting variable with type change.
        This operation is NOT allowed.
        """
        for key in keys:
            conflict = keys[key]
            old = conflict
            new = None
            with self.assertRaises(ValueError):
                kd.create(old, new)


if __name__ == "__main__":
    unittest.main()
