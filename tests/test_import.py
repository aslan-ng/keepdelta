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
            import keepdelta.types.primitives
            import keepdelta.types.primitives.delta_bool
            import keepdelta.types.primitives.delta_complex
            import keepdelta.types.primitives.delta_float
            import keepdelta.types.primitives.delta_int
            import keepdelta.types.primitives.delta_str
        except ImportError as e:
            raise AssertionError(f"Import failed: {e}")
        

if __name__ == "__main__":
    unittest.main()