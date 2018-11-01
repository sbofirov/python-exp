import unittest

class TestUM(unittest.TestCase):

    def setUp(self):
        pass

    def test_numbers_3(self):
        self.assertEqual(3, 4)

if __name__ == '__main__':
    unittest.main()
