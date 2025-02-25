import unittest


def run():
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir="tests", pattern="test_*.py")
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    run()
