"""
Test for catching packaging issues.
"""

import unittest


class TestImport(unittest.TestCase):

    def test_import(self):
        try:
            import keepdelta
            import keepdelta.types
            import keepdelta.types.collections
        except ImportError as e:
            raise AssertionError(f"Import failed: {e}")
        

if __name__ == "__main__":
    unittest.main()