import unittest


def run():
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir='test', pattern='test_*.py')
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == '__main__':
    run()