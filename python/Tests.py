import unittest
import Utils


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        utils = Utils()
        self.assertEqual('foo'.upper(), 'FOO')
        utils.binarySearcy()

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())


if __name__ == '__main__':
    unittest.main()
