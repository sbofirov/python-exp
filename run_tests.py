import sys
import unittest
loader = unittest.TestLoader()
start_dir = 'tests/'
suite = loader.discover(start_dir)

runner = unittest.TextTestRunner()
ret = not runner.run(suite).wasSuccessful()
sys.exit(ret)
