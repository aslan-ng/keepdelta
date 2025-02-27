import unittest

import keepdelta as kd
from keepdelta.config import keys


class TestReservedNamesTuple(unittest.TestCase):

    def test_from_conflict_to_normal(self):
        """
        Change a conflicting variable to a normal variable.
        """
        for key in keys:
            conflict = keys[key]
            old = (
                conflict,
                True,
            )
            new = (
                "hello",
                True,
            )
            delta = {
                0: "hello",
            }
            self.assertEqual(kd.create(old, new), delta)
            self.assertEqual(kd.apply(old, delta), new)

    def test_from_normal_to_conflict(self):
        """
        Change a normal variable to a conflicting variable.
        This operation is NOT allowed.
        """
        for key in keys:
            conflict = keys[key]
            old = (
                "hello",
                True,
            )
            new = (
                conflict,
                True,
            )
            with self.assertRaises(ValueError):
                kd.create(old, new)

    def test_change_type_from_conflict_to_normal(self):
        """
        Tuple's conflicting element has format changed.
        This operation is NOT allowed.
        """
        for key in keys:
            conflict = keys[key]
            old = (
                conflict,
                True,
            )
            new = (
                1,
                True,
            )
            with self.assertRaises(ValueError):
                kd.create(old, new)

    def test_change_type_from_normal_to_conflict(self):
        """
        Tuple's normal element has format changed to a conflicting value.
        This operation is NOT allowed.
        """
        for key in keys:
            conflict = keys[key]
            old = (
                1,
                True,
            )
            new = (
                conflict,
                True,
            )
            with self.assertRaises(ValueError):
                kd.create(old, new)


if __name__ == "__main__":
    unittest.main()